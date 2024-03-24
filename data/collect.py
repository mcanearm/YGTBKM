import io
from functools import partial, reduce
from multiprocessing.pool import ThreadPool
from pathlib import Path
from time import sleep

import pandas as pd
import requests
from numpy.random import uniform

# Y

# DONE Demographic: Demographic Variables and Sample Weights – Participant gender, age, race
# DONE Dietary: Dietary Supplement Use 30-Day - Individual and Total Dietary Supplements – Caffeine (mg)
# DONE Examination: Body Measures - Weight (kg)
# DONE Questionnaire: Alcohol Use, Diabetes, Income,  Occupation, Physical Activity, Smoking - Cigarette Use, Kidney Conditions - Urology


def read_sas_url(url, **kwargs):

    r = requests.get(url)
    return pd.read_sas(io.BytesIO(r.content), format="xport", **kwargs)


def retrieve_file(mapping_tuple, output_dir=None, wait_min=1, wait_max=3):
    dataset_name, metadata = mapping_tuple
    output_file = Path(output_dir) / f"{dataset_name}.csv"
    if output_dir:
        try:
            assert not output_file.exists()
        except AssertionError:
            Warning("{output_file} already exists!")
            return None

    sleep(uniform(low=wait_min, high=wait_max))
    df = read_sas_url(metadata["url"])
    df["SEQN"] = df["SEQN"].astype(pd.Int64Dtype())
    df = df.set_index("SEQN")[metadata["columns"]]

    if output_dir:
        df.to_csv(output_dir / f"{dataset_name}.csv")
        return None
    else:
        return df


column_mapping = {
    "demographics": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DEMO.XPT",
        "columns": [
            "RIAGENDR",  # gender (sex)
            "RIDRETH3",  # race including Asian
            "RIDAGEYR",  # age in months
        ],
    },
    "caff_intake1": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR1IFF_J.XPT",
        "columns": ["DR1ICAFF"],  # caffeine in mg
    },
    "caff_intake2": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DR2IFF_J.XPT",
        "columns": ["DR2ICAFF"],  # caffeine in mg
    },
    "caff_nutrient1": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DR1TOT.xpt",
        "columns": ["DR1TCAFF"],  # caffeine in mg
    },
    "caff_nutrient2": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DR2TOT.xpt",
        "columns": ["DR2TCAFF"],  # caffeine in mg
    },
    "caff_supplement1": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DSQTOT.XPT",
        "columns": ["DSQTCAFF"],  # caffeine in mg
    },
    "body_measures": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BMX.XPT",
        "columns": ["BMXBMI", "BMXWAIST"],  # BMI  # waist circumference
    },
    "alcohol": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_ALQ.XPT",
        "columns": ["ALQ130"],  # avg # of drinks last year
    },
    "diabetes": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DIQ.XPT",
        "columns": [
            "DIQ010",  # doctor told you you have diabetes,
            "DIQ050",  # taking insulin
            "DIQ280",  # last A1C level
        ],
    },
    "income": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_INQ.XPT",
        "columns": [
            "INDFMMPI",  # multiple of poverty level,
            "INDFMMPC",  # poverty level category
        ],
    },
    "kidney": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_KIQ_U.XPT",
        "columns": [
            "KIQ026",  # ever had kidney stones
            "KIQ029",  # passed kidney stone in 12/mo
            "KIQ022",  # weak or failing kidneys
        ],
    },
    "employment": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_OCQ.XPT",
        "columns": ["OCQ180", "OCQ670"],  # hours worked in last week  # work schedule
    },
    "physical_act": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_PAQ.XPT",
        "columns": [
            "PAQ605",  # vigorous work activity
            "PAQ620",  # moderate work activity
            "PAQ635",  # walk or use a bicycle to get places at least 10 minutes
            "PAD645",  # minutes walk/bicycle for transportation
            "PAD660",  # minutes of vigorous physical activities
            "PAD675",  # minutes moderate physical activities
            "PAD680",  # minutes sedentary activity
        ],
    },
    "smoking": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_SMQ.XPT",
        "columns": [
            "SMQ020",  # smoked at least 100 cigarettes in life
            "SMD650",  # avg cigarettes/day smoked in the last 30 days
        ],
    },
}

if __name__ == "__main__":

    output_dir = Path("./raw_data/")
    output_dir.mkdir(exist_ok=True, parents=True)

    with ThreadPool(8) as pool:
        file_download = partial(retrieve_file, output_dir=output_dir)
        pool.map(file_download, column_mapping.items())

    file_names = output_dir.glob("*.csv")

    def read_file(a, fp):
        try:
            return a.merge(
                pd.read_csv(fp, index_col="SEQN"),
                how="left",
                left_index=True,
                right_index=True,
            )
        except AttributeError:
            return pd.read_csv(fp, index_col="SEQN")

    full_df = reduce(read_file, file_names, None)
    full_df.to_csv("./full_data.csv")
