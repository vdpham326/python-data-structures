monthly_spendings = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
first_half = 0
second_half = 0

for month, spend in enumerate(monthly_spendings):
  if 0 <= month <= 5:
    first_half += spend
    print(month)
    print(spend)
    print(first_half)

  else:
    second_half += spend
    print(month)
    print(spend)
    print(second_half)

print(f'Average expense Jan-June: {first_half / 6}')
print(f'Average expense July-Dec: {second_half / 6}')