import random
import math
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

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
