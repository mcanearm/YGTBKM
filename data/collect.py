import io

import pandas as pd
import requests

# Y

# DONE Demographic: Demographic Variables and Sample Weights – Participant gender, age, race
# DONE Dietary: Dietary Supplement Use 30-Day - Individual and Total Dietary Supplements – Caffeine (mg)
# DONE Examination: Body Measures - Weight (kg)
# DONE Questionnaire: Alcohol Use, Diabetes, Income,  Occupation, Physical Activity, Smoking - Cigarette Use, Kidney Conditions - Urology


def read_sas_url(url):
    r = requests.get(url)
    return pd.read_sas(io.BytesIO(r.content), format="xport")


column_mapping = {
    "demographics": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DEMO.XPT",
        "columns": [
            "RIAGENDR",  # gender (sex)
            "RIDRETH3",  # race including Asian
            "RIDEXAGM",  # age in months
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
    "caff_supplement1": {
        "url": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DS2TOT_J.XPT",
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


# pre-existing conditions:
