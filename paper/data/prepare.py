import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.pipeline import FunctionTransformer, Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

column_map = {
    "INDFMMPI": "poverty_num",
    "INDFMMPC": "poverty_cat",
    "PAQ605": "activity_vig_work",
    "PAQ620": "activity_mod_work",
    "PAQ635": "activity_walk_or_use_bike",
    "PAD645": "activity_minutes_walk_bike",
    "PAD660": "activity_vig_min",
    "PAD675": "activity_mod_min",
    "PAD680": "activity_sed_min",
    "DSQTCAFF": "caffeine_sup_mg",
    "DR1ICAFF": "caffeine_intake1_mg",
    "DR2ICAFF": "caffeine_intake2_mg",
    "DR1TCAFF": "caffeine_nutrient1_mg",
    "DR2TCAFF": "caffeine_nutrient2_mg",
    "BMXBMI": "bmi_total",
    "BMXWAIST": "bmi_waist",
    "ALQ130": "alcohol_nmbr_drinks",
    "OCQ180": "occ_hours_worked",
    "OCQ670": "occ_work_shift",
    "DIQ010": "diabetes_diag",
    "DIQ050": "diabetes_insulin",
    "DIQ280": "diabetes_aic",
    "SMQ020": "smoking_100cigs",
    "SMD650": "smoking_cigs_pd",
    "KIQ022": "kidney_weak_failing",
    "KIQ026": "kidney_had_stones",
    "KIQ029": "kidney_passed_stone",
    "RIAGENDR": "is_male",
    "RIDRETH3": "demo_race",
    "RIDAGEYR": "demo_age",
}

hist_vars = [
    "poverty_num",
    "activity_vig_min",
    "activity_mod_min",
    "activity_sed_min",
    "any_caffeine_log",
    "demo_age",
    "bmi_total",
    "occ_hours_worked",
    "alcohol_nmbr_drinks",
    "any_caffeine",
    "demo_race",
    "demo_gender",
]


def max_val_null(x, max_val):
    return np.where(x >= max_val, np.nan, x)


if __name__ == "__main__":

    df = pd.read_csv("./full_data.csv", index_col="SEQN")

    # raw data cleaning steps; handle missing
    df["KIQ022"] = 0 or df["KIQ026"] == 1
    df["KIQ026"] = 0 or df["KIQ026"] == 1
    df["KIQ029"] = 0 or df["KIQ029"] == 1

    df["SMD650"] = max_val_null(df["SMD650"], 777)

    df["ALQ130"] = max_val_null(df["ALQ130"], 16)
    df["PAD660"] = max_val_null(df["PAD660"], 7777)
    df["PAD675"] = max_val_null(df["PAD675"], 7777)
    df["PAD680"] = max_val_null(df["PAD680"], 7777)
    df["PAQ605"] = df["PAQ605"] == 1
    df["PAQ620"] = df["PAQ620"] == 1
    df["OCQ180"] = max_val_null(df["OCQ180"], 7777)
    df["RIAGENDR"] = df["RIAGENDR"] == 1  # no missing

    def map_race(val):
        match val:
            case 1.0:
                return "hispanic"
            case 2.0:
                return "hispanic"
            case 3.0:
                return "white"
            case 4.0:
                return "black"
            case 6.0:
                return "asian_non_hisp"
            case 7.0:
                return "other_or_multi"
            case _:
                return "missing"

    df = df.rename(column_map, axis=1)
    df = df[df["demo_age"] >= 18]
    df["demo_race_str"] = df["demo_race"].apply(map_race)

    df["any_caffeine"] = (
        pd.concat(
            [
                df[
                    [
                        "caffeine_nutrient1_mg",
                        "caffeine_nutrient2_mg",
                    ]
                ].mean(axis=1),
                df[["caffeine_intake1_mg", "caffeine_intake2_mg"]].mean(axis=1),
                df[["caffeine_sup_mg"]],
            ],
            axis=1,
        )
        .max(axis=1)
        .fillna(0)
    )
    df["any_caffeine_log"] = np.log1p(df["any_caffeine"])

    preprocessor = ColumnTransformer(
        [
            (
                "knn_impute",
                KNNImputer(),
                [
                    "bmi_total",
                    "demo_age",
                    "activity_sed_min",
                ],
            ),
            (
                "simple_impute",
                SimpleImputer(strategy="median"),
                ["alcohol_nmbr_drinks", "poverty_num"],
            ),
            (
                "zero_impute",
                SimpleImputer(fill_value=0, strategy="constant"),
                ["activity_vig_min", "activity_mod_min", "smoking_cigs_pd"],
            ),
            (
                "static_impute",
                SimpleImputer(fill_value=40, strategy="constant"),
                ["occ_hours_worked"],
            ),
            (
                "passthrough",
                "passthrough",
                ["any_caffeine", "is_male", "any_caffeine_log"],
            ),
            (
                "one_hot",
                OneHotEncoder(sparse_output=False, drop=["white"]),
                ["demo_race_str"],
            ),
        ],
        remainder="drop",
    )

    transformed_data = preprocessor.fit_transform(df)
    post_processing_cols = preprocessor.get_feature_names_out()
    transformed_data = pd.DataFrame(
        transformed_data,
        columns=post_processing_cols,
        index=df.index,
    ).merge(
        df[
            [
                "kidney_had_stones",
                "kidney_passed_stone",
                "kidney_weak_failing",
            ]
        ],
        left_index=True,
        right_index=True,
    )

    transformed_data.to_csv("./prepared_data.csv")
