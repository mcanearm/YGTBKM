#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:21:39 2024

@author: rafal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

alcohol = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/alcohol.csv")
body_measures = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/body_measures.csv")
caff_intake_1 = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/caff_intake1.csv")
caff_intake_2 = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/caff_intake2.csv")
caff_supplement = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/caff_supplement1.csv")
demographics = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/demographics.csv")
diabetes = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/diabetes.csv")
employment = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/employment.csv")
income = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/income.csv")
kidney = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/kidney.csv")
physical_act = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/physical_act.csv")
smoking = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/smoking.csv")

caff_nutrient_1 = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/caff_nutrient1.csv")
caff_nutrient_2 = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/raw_data/caff_nutrient2.csv")

print("caff_supplement:")
print(f"Alcohol {len(caff_supplement.set_index('SEQN').join(alcohol.set_index('SEQN')).dropna())}")
print(f"body_measures {len(caff_supplement.set_index('SEQN').join(body_measures.set_index('SEQN')).dropna())}")
print(f"demographics {len(caff_supplement.set_index('SEQN').join(demographics.set_index('SEQN')).dropna())}")
print(f"diabetes {len(caff_supplement.set_index('SEQN').join(diabetes.set_index('SEQN')).dropna())}")
print(f"employment {len(caff_supplement.set_index('SEQN').join(employment.set_index('SEQN')).dropna())}")
print(f"income {len(caff_supplement.set_index('SEQN').join(income.set_index('SEQN')).dropna())}")
print(f"kidney {len(caff_supplement.set_index('SEQN').join(kidney.set_index('SEQN')).dropna())}")
print(f"physical_act {len(caff_supplement.set_index('SEQN').join(physical_act.set_index('SEQN')).dropna())}")
print(f"smoking {len(caff_supplement.set_index('SEQN').join(smoking.set_index('SEQN')).dropna())}")

print('\n')

print("caff_intake_1:")
print(f"Alcohol {len(caff_intake_1.set_index('SEQN').join(alcohol.set_index('SEQN')).dropna())}")
print(f"body_measures {len(caff_intake_1.set_index('SEQN').join(body_measures.set_index('SEQN')).dropna())}")
print(f"demographics {len(caff_intake_1.set_index('SEQN').join(demographics.set_index('SEQN')).dropna())}")
print(f"diabetes {len(caff_intake_1.set_index('SEQN').join(diabetes.set_index('SEQN')).dropna())}")
print(f"employment {len(caff_intake_1.set_index('SEQN').join(employment.set_index('SEQN')).dropna())}")
print(f"income {len(caff_intake_1.set_index('SEQN').join(income.set_index('SEQN')).dropna())}")
print(f"kidney {len(caff_intake_1.set_index('SEQN').join(kidney.set_index('SEQN')).dropna())}")
print(f"physical_act {len(caff_intake_1.set_index('SEQN').join(physical_act.set_index('SEQN')).dropna())}")
print(f"smoking {len(caff_intake_1.set_index('SEQN').join(smoking.set_index('SEQN')).dropna())}")

print('\n')

print("caff_intake_2:")
print(f"Alcohol {len(caff_intake_2.set_index('SEQN').join(alcohol.set_index('SEQN')).dropna())}")
print(f"body_measures {len(caff_intake_2.set_index('SEQN').join(body_measures.set_index('SEQN')).dropna())}")
print(f"demographics {len(caff_intake_2.set_index('SEQN').join(demographics.set_index('SEQN')).dropna())}")
print(f"diabetes {len(caff_intake_2.set_index('SEQN').join(diabetes.set_index('SEQN')).dropna())}")
print(f"employment {len(caff_intake_2.set_index('SEQN').join(employment.set_index('SEQN')).dropna())}")
print(f"income {len(caff_intake_2.set_index('SEQN').join(income.set_index('SEQN')).dropna())}")
print(f"kidney {len(caff_intake_2.set_index('SEQN').join(kidney.set_index('SEQN')).dropna())}")
print(f"physical_act {len(caff_intake_2.set_index('SEQN').join(physical_act.set_index('SEQN')).dropna())}")
print(f"smoking {len(caff_intake_2.set_index('SEQN').join(smoking.set_index('SEQN')).dropna())}")

print('\n')

print("caff_nutrient_1:")
print(f"Alcohol {len(caff_nutrient_1.set_index('SEQN').join(alcohol.set_index('SEQN')).dropna())}")
print(f"body_measures {len(caff_nutrient_1.set_index('SEQN').join(body_measures.set_index('SEQN')).dropna())}")
print(f"demographics {len(caff_nutrient_1.set_index('SEQN').join(demographics.set_index('SEQN')).dropna())}")
print(f"diabetes {len(caff_nutrient_1.set_index('SEQN').join(diabetes.set_index('SEQN')).dropna())}")
print(f"employment {len(caff_nutrient_1.set_index('SEQN').join(employment.set_index('SEQN')).dropna())}")
print(f"income {len(caff_nutrient_1.set_index('SEQN').join(income.set_index('SEQN')).dropna())}")
print(f"kidney {len(caff_nutrient_1.set_index('SEQN').join(kidney.set_index('SEQN')).dropna())}")
print(f"physical_act {len(caff_nutrient_1.set_index('SEQN').join(physical_act.set_index('SEQN')).dropna())}")
print(f"smoking {len(caff_nutrient_1.set_index('SEQN').join(smoking.set_index('SEQN')).dropna())}")

print('\n')

print("caff_nutrient_2:")
print(f"Alcohol {len(caff_nutrient_2.set_index('SEQN').join(alcohol.set_index('SEQN')).dropna())}")
print(f"body_measures {len(caff_nutrient_2.set_index('SEQN').join(body_measures.set_index('SEQN')).dropna())}")
print(f"demographics {len(caff_nutrient_2.set_index('SEQN').join(demographics.set_index('SEQN')).dropna())}")
print(f"diabetes {len(caff_nutrient_2.set_index('SEQN').join(diabetes.set_index('SEQN')).dropna())}")
print(f"employment {len(caff_nutrient_2.set_index('SEQN').join(employment.set_index('SEQN')).dropna())}")
print(f"income {len(caff_nutrient_2.set_index('SEQN').join(income.set_index('SEQN')).dropna())}")
print(f"kidney {len(caff_nutrient_2.set_index('SEQN').join(kidney.set_index('SEQN')).dropna())}")
print(f"physical_act {len(caff_nutrient_2.set_index('SEQN').join(physical_act.set_index('SEQN')).dropna())}")
print(f"smoking {len(caff_nutrient_2.set_index('SEQN').join(smoking.set_index('SEQN')).dropna())}")

print('\n')


#Is there a relationship between caffeine consumption and kidney stone occurrence?
#Does this relationship change based on different demographic features - 
#race, gender, occupation, income, and other socioeconomic variables?

#KIQ022, ever told of weak/failing kidneys? 1, 2, 7, 9, .
#KIQ026, ever had kidney stones? 1, 2, 7, 9, .
#KIQ029 - Pass kidney stone in past 12 months? 1, 2, 7, 9, .

kidney1 = caff_nutrient_1.set_index('SEQN').join(kidney.set_index('SEQN')).dropna()
kidney2 = caff_nutrient_2.set_index('SEQN').join(kidney.set_index('SEQN')).dropna()

#plt.plot(kidney1)
fig1 = sns.catplot(data=kidney1, x="KIQ022", y="DR1TCAFF", kind="box")
fig1.set(ylim=(0, 1000))

fig2 = sns.catplot(data=kidney2, x="KIQ022", y="DR2TCAFF", kind="box")
fig2.set(ylim=(0, 1000))

fig3 = sns.catplot(data=kidney1, x="KIQ026", y="DR1TCAFF", kind="box")
fig3.set(ylim=(0, 1000))

fig4 = sns.catplot(data=kidney2, x="KIQ026", y="DR2TCAFF", kind="box")
fig4.set(ylim=(0, 1000))


#PAQ605 - Vigorous work activity (factor)
#PAQ620 - Moderate work activity (factor)
#PAQ635 - Walk or bicycle (factor)
#PAQ680 - Minutes sedentary activity (cont)
#SMQ020 - Smoked at least 100 cigarettes in life (factor)
#ALQ130 - 
#OCQ180 - Hours worked last week in total all jobs (cont)
#OCQ670 - Overall work schedule past 3 months


data = pd.read_csv(r"/home/rafal/Desktop/Stats_503/YGTBKM-feature-mmcanear-dev(1)/data/full_data.csv")

#Add P680, some key error prevents selection
selected_sub_df = data.loc[:, ["KIQ022", "PAQ605", "PAQ620", "PAQ635", "SMQ020", "ALQ130", "OCQ180", "OCQ670", "DR1TCAFF", "DR2TCAFF"]]
print(len(selected_sub_df.dropna()))
#2931

selected_sub_df = data.loc[:, ["KIQ022", "PAQ605", "PAQ620", "PAQ635", "SMQ020", "DR1TCAFF", "DR2TCAFF"]]
print(len(selected_sub_df.dropna()))
#6961

fig5 = sns.scatterplot(data=selected_sub_df, x="KIQ022", y="PAQ605")
fig5.set(ylim=(0, 1000))

fig6 = sns.scatterplot(data=selected_sub_df.dropna(), x="KIQ022", y="PAQ620")

fig7 = sns.scatterplot(data=selected_sub_df.dropna(), x="KIQ022", y="PAQ635")

