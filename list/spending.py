martha_monthly_spendings = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
tim_monthly_spendings = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
household_monthly_spendings = []

for i in range(len(tim_monthly_spendings)):
  household_monthly_spendings.append(round(martha_monthly_spendings[i] + tim_monthly_spendings[i]))
  
print(household_monthly_spendings)