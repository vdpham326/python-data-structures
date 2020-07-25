'''
Create a function named get_min_max_mean(numbers) that accepts a list of integer values and returns the smallest element, 
the largest element, and the average value respectively – all of them in the form of a tuple.
'''
def get_min_max_mean(numbers):
  smallest, largest, total = numbers[0], numbers[0], 0
  
  for number in numbers:
    total += number
    if number < smallest:
      smallest = number
    if number > largest:
      largest = number
  average = total / len(numbers)
  return (smallest, largest, average)
      
  

print(get_min_max_mean([1, 2, 3, -1, -2, -3])) #expect (-3, 3, 0.0)