'''
Create a function named count_stats(input_data), which accepts a 2-dimensional list with numerical elements and returns a tuple with the following three items:

(minimum list value, maximum list value, sum of all values)
You can use the sample data to test your function.
'''



def count_stats(input_data):
    min, max, sum = input_data[0][0],input_data[0][0], 0
    for row in input_data:
        for val in row:
            if val < min:
                min = val
            if val > max:
                max = val
            sum += val
    return (min, max, sum)


sample_data = [
  [342.3, -34.34, 3489.3, 8834.2],
  [6430.0, -123.8, 342.9]
]


print(count_stats(sample_data))