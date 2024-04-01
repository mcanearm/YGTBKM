import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.pipeline import FunctionTransformer, Pipeline
from sklearn.preprocessing import StandardScaler

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
    "KIQ026": "kidney_had_stones",
    "KIQ029": "kidney_passed_stone",
    "KIQ022": "kidney_weak_failing",
    "RIAGENDR": "demo_gender",
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
    df["KIQ026"] = 0 or df["KIQ026"] == 1

    df["ALQ130"] = max_val_null(df["ALQ130"], 16)
    df["PAD660"] = max_val_null(df["PAD660"], 7777)
    df["PAD675"] = max_val_null(df["PAD675"], 7777)
    df["PAD680"] = max_val_null(df["PAD680"], 7777)
    df["PAQ605"] = df["PAQ605"] == 1
    df["PAQ620"] = df["PAQ620"] == 1
    df["OCQ180"] = max_val_null(df["OCQ180"], 7777)

    df = df.rename(column_map, axis=1)
    df = df[df["demo_age"] >= 18]

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

    preprocessor = ColumnTransformer(
        [
            (
                "knn_impute",
                KNNImputer(),
                [
                    "bmi_total",
                    "demo_age",
                    "activity_sed_min",
                    # "activity_vig_min",  # 80% missing - probably remove
                    # "activity_mod_min",  # 60% missing - probably remove
                ],
            ),
            (
                "simple_impute",
                SimpleImputer(strategy="median"),
                ["alcohol_nmbr_drinks", "poverty_num"],
            ),
            ("static_impute", SimpleImputer(fill_value=40), ["occ_hours_worked"]),
            (
                "zero_impute",
                SimpleImputer(fill_value=0),
                ["activity_vig_min", "activity_mod_min"],
            ),
            ("passthrough", FunctionTransformer(lambda x: x), ["any_caffeine"]),
            ("log_caff", FunctionTransformer(lambda x: np.log1p(x)), ["any_caffeine"]),
        ]
    )

    transformed_data = preprocessor.fit_transform(df)
    transformed_data = pd.DataFrame(
        transformed_data,
        columns=[
            "bmi_total",
            "demo_age",
            "activity_sed_min",
            "alcohol_nmbr_drinks",
            "poverty_num",
            "occ_hours_worked",
            "activity_vig_min",
            "activity_mod_min",
            "caffeine_mg",
            "caffeine_mg_log",
        ],
        index=df.index.values,
    )

    transformed_data.to_csv("./prepared_data.csv")
