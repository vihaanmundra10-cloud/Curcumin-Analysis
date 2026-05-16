import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.write("""













A Conceptual Model of Curcumin Infused Nicotine Therapy, Predicting Cardiovascular Damage
Vihaan Rajesh Mundra
						






















Abstract
In this study, a conceptual simulation is created to observe the impact of curcumin infused NRT on CAD. Unfortunately, NRT is not entirely safe as the patient is still consuming nicotine in small doses throughout treatment. These small doses can still cause atherosclerosis, which is one of the leading causes of CAD. The simulation tracks 4 groups of people on a risk index: regular smokers, non-smokers, smoker on curcumin infused NRT, and a smoker on regular NRT. The results of this paper found that curcumin infused NRT can cause a slight difference in CAD risk. However, this cannot be established clearly as this is a conceptual simulation. 


Introduction
Smoking is one of the leading causes of Cardiovascular Disease (CVD). Approximately one in every four cases are caused by smoking1. All Cigarettes and e-cigarettes contain a chemical compound called Nicotine, which is highly addictive. Nicotine has several effects on the cardiovascular system and contributes to the development of CVD. 
Nicotine causes hypertension (increased blood pressure), thrombosis, inflammation, insulin resistance, and dyslipidemia, which all promote atherosclerosis2. 
Atherosclerosis is the buildup of fats, cholesterol, and other substances on artery walls known as plaque. This plaque causes arteries to narrow and block blood flow leading to Coronary Artery Disease (CAD), the most common type of CVD3. 
Once nicotine is consumed, it enters the blood stream and enters the brain. The nicotine causes the brain to release dopamine, which causes a nicotine buzz or Euphoria. This process is instantaneous as soon as someone consumes it through tobacco. Over time, the brain begins to crave the dopamine released through nicotine consumption, causing several to become addicted4. According to the National Institute on Drug Abuse5 (NIDA), almost 62 million people disclosed they used nicotine or tobacco products in the past thirty days in 2021, demonstrating its addictive nature. 
In recent times, scientists have developed treatments that help others stop consuming nicotine. NRT (Nicotine Replacement Therapy) involves using nicotine patches or gum which will help patients eliminate their cravings for nicotine. Patients who recently quit smoking– or consuming nicotine– are given nicotine patches or gum that contain small doses of nicotine. Over time doses are strategically lowered, helping patients quit nicotine. However, this method is not cardiovascularly risk free. As mentioned above, these patches and gum contain nicotine, which still harms the cardiovascular system6. Given the cardiovascular risks of NRT, this raises a question as to how NRT can be modified to eliminate these risks. 
It is hypothesized that if Curcumin is paired with NRT, CAD risks can be reduced because Curcumin will stop atherosclerosis from occurring. Curcumin is found in turmeric and contains anti-atherosclerosis properties. A study states that Curcumin is transdermal (it can be injected into skin and absorbed into the bloodstream), which means it is compatible to use with NRT7. The aim is to significantly reduce CVD, particularly CAD, risk while ensuring that patients get rid of nicotine addiction. 

Materials and Methods 
	To simulate Curcumin infused NRT, a graph was constructed. The graph tracks a regular smoker for ten years, non-smoker, smoker for the past ten years on NRT, and a smoker for the past 10 years on Curcumin infused NRT. These groups are tracked over a 12 month period. These groups were chosen to be graphed to effectively compare and contrast Curcumin infused NRT over a 12 month period with regular NRT. Control groups like non-smokers and regular smokers were chosen to illustrate the profound impact smoking has on CVD risk. A period of 12 months was chosen as it is a clinical norm when conducting cardiovascular tests. The period was also most logical to highlight a clear difference between curcumin infused NRT and regular NRT. The values used to simulate these variables over the 12 month period was a risk index or risk score, not clinical percentage values.  
	This graph was made with an online software called google sheets.
	A baseline risk score of 100 was assigned to the non-smoker. This remained constant all season because the non-smoker is not consuming any nicotine, thus keeping their risk score stagnant. A study shows that a smoker that has been smoking for a decade has a CVD risk of 15-20% higher than the baseline8. Given this, all smokers– no matter the treatment- were given a baseline risk score of 120. A regular smoker's risk score was incremented by 2 each month as they are continuously smoking, thus increasing their risk. Even though this will surpass the 15-20% increase cited above, this is a modeling choice to clearly illustrate the difference. NRT generally lasts 8-12 weeks, so for the smokers taking NRT, the score increases by 1.5 the first month, 0.75 the second month, and 0.25 the third month. These values are chosen because the smokers on NRT therapy are still consuming nicotine, thus increasing their CVD risk over time. The amount of CVD risk added is being gradually decreased each month as the nicotine consumption of the smoker is being gradually decreased each month. This only happens for the first three months as they are only consuming nicotine for 3 months, given that NRT lasts for 3 months. For curcumin infused NRT treatment, the risk score does not decrease or increase for the first three months, representing the hypothesized effect of curcumin. After the treatment for both smokers, their risk score decreases by 1 each month as cessation reduces CVD risk9
	To generate the graph, linear functions were used. Specifically, for the non-smoker, the equation was b(x)=100 as the risk remained constant throughout the simulation, where b(x) is the risk percentage. The smokers equation was g(x)=120+2x where 120 represents the starting risk and 2 represents the risk added per month, x, and g(x) is the risk score. For the smoker on regular NRT, the risk score f(x) is: 
120 + 1.5 × x for 0 < x ≤ 1 month


120 + 1.5 + 0.75 × (x − 1) for 1 < x ≤ 2 months


120 + 1.5 + 0.75 + 0.25 × (x − 2) for 2 < x ≤ 3 months


122.5 − 1 × (x − 3) for 3 < x ≤ 12 months
 The smoker with Curcumin infused NRT, the risk score r(x) is:
120 for 0 < x ≤ 3 months


120 − 1 × (x − 3) for 3 < x ≤ 12 months 
A linear model for the graph was chosen given its simplicity. Linear models are effective at graphing trends over a certain period of time, which was the purpose of this graph. 



Results
	The results of this experiment were found in simulating four groups of people over a 12 month period: regular smoker for ten years, non-smoker, smoker for the past ten years on NRT, and a smoker for the past 10 years on Curcumin infused NRT. The data was recorded into a table and visualized into a graph. 

	In table and figure 1, the non-smoker had a constant risk score of 100 throughout the course of the simulation. To the contrast, the smoker of 10 years was constantly increasing in its risk score shown through the graph and– as shown in the table–had a risk score of 144 at month 12, which is 24 more than the score at month 0. In other words, the risk score for the smoker without any treatment was increasing by 2 every month. As shown by table 1, the smoker on regular NRT had a change of -7.5 in CVD risk while the smoker on curcumin infused NRT had a change of -9 in risk score. By the end of the simulation, the difference of risk score between these two groups was 1.5 as the smoker with regular NRT had 1.5 points more. 

	As shown in table one, the smoker on regular NRT increased by 0.75 in risk score for the first three months and then decreased by 1 every month after. However, the smoker on curcumin infused NRT did not increase in risk score at all from start to finish. Rather, the smoker on curcumin infused NRT was decreasing by 1 in risk score every month for the entirety of the simulation. 




Discussion
	It was hypothesized that curcumin infused NRT will reduce all the risks of CAD by preventing atherosclerosis from occurring. The data of the simulation illustrated that the curcumin infused NRT allowed for CAD risk to stay stagnant and slowly decrease after the three month period. With regular NRT, there was a slight increase in CAD risk and slow decrease after the three month period. Smokers without treatment increased throughout the simulation and non-smokers stayed stagnant at their baseline risk. 
	The results of the simulation occurred because Curcumin contains anti-atherosclerosis properties. Moreover, it is found to have anti-inflammatory effects. It stops plaque from building up on the artery walls, thus, eliminating atherosclerosis from occurring and stopping CAD10. These findings align with previous studies as nano-curcumin lowered Malondialdehyde, Nitric oxide, C-reactive protein levels in smokers11. All of these substances are biomarkers for high oxidative stress and oxidative stress leads to atherosclerosis. This suggests that with NRT, curcumin can eliminate CAD risk from smoking while NRT reduces nicotine cravings. 

	However, this study was conducted using mathematical equations and the simulation was not based on any clinical studies or evidence. This study is a conceptual simulation that uses risk scores that are assumed. To investigate this further, humans can be tested using curcumin infused NRT, allowing for an accurate depiction of the treatment. Moreover, this graph does not aim to map precise values. In fact, this is one limitation of the model as it does not account for individual variation. To elaborate, many factors cause CVD risk to fluctuate. For instance, things like diet, age, ethnicity, and physical activity can all affect CVD risk. A person who has a diet high in saturated fats, trans fat, and cholesterol, has little to no physical activity, is older, and is American Indian or African American, has a higher chance of developing CVD 12. This graph being a linear model cannot account for these factors and is not completely accurate.













References

1. Health effects of cigarettes: cardiovascular disease. Smoking and Tobacco Use. 2024, https://www.cdc.gov/tobacco/about/cigarettes-and-cardiovascular-disease.html.

2. J. Lee, J. P. Cooke. The role of nicotine in the pathogenesis of atherosclerosis. Atherosclerosis. Vol. 215, pg. 281–283, 2011, https://doi.org/10.1016/j.atherosclerosis.2011.01.003.

3. Arteriosclerosis / atherosclerosis - symptoms and causes. Mayo Clinic. https://www.mayoclinic.org/diseases-conditions/arteriosclerosis-atherosclerosis/symptoms-causes/syc-20350569.

4. Heart disease facts. Heart Disease. 2024, https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html.

5. Nicotine: it’s why smoking is so addictive. Health and Social Services. https://www.hss.gov.nt.ca/en/services/health-effects-tobacco/nicotine-it%E2%80%99s-why-smoking-so-addictive.

6. Nicotine replacement therapy (NRT). Cleveland Clinic. 2025, https://my.clevelandclinic.org/health/treatments/nicotine-replacement-therapy-nrt.

7. O. Pelikh, S. R. Pinnapireddy, C. M. Keck. Dermal penetration analysis of curcumin in an ex vivo porcine ear model using epifluorescence microscopy and digital image processing. Skin Pharmacology and Physiology. Vol. 34, pg. 281–299, 2021, https://doi.org/10.1159/000514498.

8. Curcumin as a natural remedy for atherosclerosis: a pharmacological review. National Library of Medicine. 2021, https://pubmed.ncbi.nlm.nih.gov/34279384/.

9. K. A. Gallagher et al. Current status and principles for the treatment and prevention of diabetic foot ulcers in the cardiovascular patient population: a scientific statement from the American Heart Association. Circulation. Vol. 149, 2024, https://doi.org/10.1161/cir.0000000000001192.

10. Smoking cessation and benefits to cardiovascular health: a review of literature. National Library of Medicine. 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10082935/.

11. P. Mamsharifi et al. Nano-curcumin effects on nicotine dependence, depression, anxiety and metabolic parameters in smokers: a randomized double-blind clinical study. Heliyon. Vol. 9, 2023, https://doi.org/10.1016/j.heliyon.2023.e21249.

12. Heart disease risk factors. Heart Disease. 2024, https://www.cdc.gov/heart-disease/risk-factors/index.html.
 """)

n = 200        
months = 13    

g = 0.5

def simulate_non_smoker():
    return [100 for _ in range(months)]


def simulate_smoker():
    person = [120]
    for m in range(1, months):
        change = 2 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def simulate_nrt():
    person = [120]
    for m in range(1, months):
        if m == 1:
            change = 1.5 + random.gauss(0, g)
        elif m == 2:
            change = 0.75 + random.gauss(0, g)
        elif m == 3:
            change = 0.25 + random.gauss(0, g)
        else:
            change = -1 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def simulate_curcumin():
    person = [120]
    for m in range(1, months):
        if m <= 3:
            change = 0 + random.gauss(0, g)
        else:
            change = -1 + random.gauss(0, g)
        person.append(person[-1] + change)
    return person


def run_many_last(sim_func, runs):
    all_runs = []
    last_num = []
    for _ in range(runs):
        all_runs.append(sim_func())
        last_num.append(all_runs[-1][-1])
        
    st.write(sum(last_num) / len(last_num))
        
    return all_runs


run_many_last(simulate_curcumin, 100000)
run_many_last(simulate_nrt, 100000)
run_many_last(simulate_smoker, 100000)
run_many_last(simulate_non_smoker, 100000)

st.write("\n\n\n")


def run_many_1(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[1])
    
    return sum(nums) / len(nums)


def run_many_2(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[2])
    
    return sum(nums) / len(nums)


def run_many_3(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[3])
    
    return sum(nums) / len(nums)


def run_many_4(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[4])
    
    return sum(nums) / len(nums)


def run_many_5(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[5])
    
    return sum(nums) / len(nums)


def run_many_6(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[6])
    
    return sum(nums) / len(nums)


def run_many_7(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[7])
    
    return sum(nums) / len(nums)


def run_many_8(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[8])
    
    return sum(nums) / len(nums)


def run_many_9(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[9])
    
    return sum(nums) / len(nums)


def run_many_10(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[10])
    
    return sum(nums) / len(nums)


def run_many_11(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[11])
    
    return sum(nums) / len(nums)


def run_many_12(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[12])
    
    return sum(nums) / len(nums)


def run_many_13(sim_func, runs):
    all_runs = []
    nums = []
    for _ in range(runs):
        all_runs.append(sim_func())
    for run in all_runs:
        nums.append(run[13])
    
    return sum(nums) / len(nums)


run_many_1(simulate_curcumin, 100000)


avg_list_curcumin = [
    run_many_1(simulate_curcumin, 100000),
    run_many_2(simulate_curcumin, 100000),
    run_many_3(simulate_curcumin, 100000),
    run_many_4(simulate_curcumin, 100000),
    run_many_5(simulate_curcumin, 100000),
    run_many_6(simulate_curcumin, 100000),
    run_many_7(simulate_curcumin, 100000),
    run_many_8(simulate_curcumin, 100000),
    run_many_9(simulate_curcumin, 100000),
    run_many_10(simulate_curcumin, 100000),
    run_many_11(simulate_curcumin, 100000),
    run_many_12(simulate_curcumin, 100000),
]

avg_list_smoker = [
    run_many_1(simulate_smoker, 100000),
    run_many_2(simulate_smoker, 100000),
    run_many_3(simulate_smoker, 100000),
    run_many_4(simulate_smoker, 100000),
    run_many_5(simulate_smoker, 100000),
    run_many_6(simulate_smoker, 100000),
    run_many_7(simulate_smoker, 100000),
    run_many_8(simulate_smoker, 100000),
    run_many_9(simulate_smoker, 100000),
    run_many_10(simulate_smoker, 100000),
    run_many_11(simulate_smoker, 100000),
    run_many_12(simulate_smoker, 100000),
]

avg_list_non_smoker = [
    run_many_1(simulate_non_smoker, 100000),
    run_many_2(simulate_non_smoker, 100000),
    run_many_3(simulate_non_smoker, 100000),
    run_many_4(simulate_non_smoker, 100000),
    run_many_5(simulate_non_smoker, 100000),
    run_many_6(simulate_non_smoker, 100000),
    run_many_7(simulate_non_smoker, 100000),
    run_many_8(simulate_non_smoker, 100000),
    run_many_9(simulate_non_smoker, 100000),
    run_many_10(simulate_non_smoker, 100000),
    run_many_11(simulate_non_smoker, 100000),
    run_many_12(simulate_non_smoker, 100000),
]

avg_list_nrt = [
    run_many_1(simulate_nrt, 100000),
    run_many_2(simulate_nrt, 100000),
    run_many_3(simulate_nrt, 100000),
    run_many_4(simulate_nrt, 100000),
    run_many_5(simulate_nrt, 100000),
    run_many_6(simulate_nrt, 100000),
    run_many_7(simulate_nrt, 100000),
    run_many_8(simulate_nrt, 100000),
    run_many_9(simulate_nrt, 100000),
    run_many_10(simulate_nrt, 100000),
    run_many_11(simulate_nrt, 100000),
    run_many_12(simulate_nrt, 100000),
]

df1 = pd.DataFrame(avg_list_curcumin, columns=["Simulating with Curcumin Treatment "])
df1.index = range(1, len(df1) + 1)

df2 = pd.DataFrame(avg_list_non_smoker, columns=["Simulating with Non-Smoker "])
df2.index = range(1, len(df2) + 1)

df3 = pd.DataFrame(avg_list_smoker, columns=["Simulating with Smoker "])
df3.index = range(1, len(df3) + 1)

df4 = pd.DataFrame(avg_list_nrt, columns=["Simulating with NRT "])
df4.index = range(1, len(df4) + 1)

st.write(df1)
st.write(df2)
st.write(df3)
st.write(df4)

# Creating the Graph
plt.plot(df1.index, df1["Simulating with Curcumin Treatment "], label="Curcumin Treatment", marker='o')
plt.plot(df2.index, df2["Simulating with Non-Smoker "], label="Non-Smoker", marker='s')
plt.plot(df3.index, df3["Simulating with Smoker "], label="Smoker", marker='^')
plt.plot(df4.index, df4["Simulating with NRT "], label="NRT", marker='D')

plt.title("Simulation Comparison")
plt.xlabel("Simulation Run")
plt.ylabel("Average Value")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

st.pyplot(plt)
