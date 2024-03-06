import io

import pandas as pd
import requests

# Y

# body measures: weight, BMI at waist https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BMX.XPT
# Bone mineral density: measure of bone health https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DXXFEM.XPT
# Blood presure: systolic and diastolic https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BPXO.XPT

# body measures: weight, BMI at waist https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BMX.XPT
# Bone mineral density: measure of bone health https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DXXFEM.XPT
# Blood presure: systolic and diastolic https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BPXO.XPT
# physical activity: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_PAQ.XPT (among adults)
# alcohol use: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_ALQ.XPT
# Smoking: just do cigarettes/day: https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_SMQ.XPT
# pre-existing conditions:


def read_sas_url(url):
    r = requests.get(url)
    return pd.read_sas(io.BytesIO(r.content), format="xport")


{
    "demographics": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DEMO.XPT",
    "diet": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DBQ.XPT",
    "body_measures": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BMX.XPT",
    "bone_mineral_density": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_DXXFEM.XPT",
    "blood_presure": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_BPXO.XPT",
    "physical_activity": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_PAQ.XPT",
    "alcohol_use": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_ALQ.XPT",
    "smoking": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_SMQ.XPT",
    "income": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/P_INQ.htm",
}

# pre-existing conditions:
