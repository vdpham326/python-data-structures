'''
Change the order of elements in the monthly_spendings list by swapping pairs of neighboring elements. In other words, if the monthly_spendings list was:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
the expected result would be:

[2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11]
'''

monthly_spendings = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

for i in range(len(monthly_spendings) - 1):
    if i % 2 == 0:
        temp = monthly_spendings[i]
        monthly_spendings[i] = monthly_spendings[i+1]
        monthly_spendings[i+1] = temp

print(monthly_spendings)