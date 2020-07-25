martha_monthly_spendings_2017 = [3890.45, 3328.2, 3267.12, 3182.2, 3147.3, 2770.38, 2689.56, 2545.72, 2462.61, 2394.04, 2099.91, 1746.83]
martha_monthly_spendings_2018 = [3883.04, 3727.18, 3453.42, 3367.66, 3328.55, 3073.93, 2442.75, 2395.7, 2340.49, 2025.84, 1651.91, 1585.41]

all_sorted_spendings = []

i, j = 0, 0

while i < len(martha_monthly_spendings_2017) and j < len(martha_monthly_spendings_2018):
    if martha_monthly_spendings_2017[i] < martha_monthly_spendings_2018[j]:
        all_sorted_spendings.append(martha_monthly_spendings_2017[i]) # add the smaller value
        i += 1
    else:
        all_sorted_spendings.append(martha_monthly_spendings_2018[j])
        j += 1

all_sorted_spendings += martha_monthly_spendings_2017[i:]
all_sorted_spendings += martha_monthly_spendings_2018[j:]

print(all_sorted_spendings)