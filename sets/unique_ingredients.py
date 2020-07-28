'''
You are given a restaurant menu in the template code. This menu is stored in tuples; each tuple consists of a dish name and a list of its ingredients.

We want to find out how many unique ingredients are used in this restaurant. Write a function named count_unique_ingredients(dishes) that accepts a dictionary 
(as shown in the template code). This function should return the total number of unique ingredients from all the dishes in the list.
'''

menu = {
  'Meat Pie': ['pork', 'potato', 'paprika', 'egg', 'cream'],
  'Broccoli Chicken': ['chicken', 'broccoli', 'cream'],
  'Eggy Chicken': ['chicken', 'egg'],
  'Tortilla Espanola': ['egg', 'onion', 'potato']
}


def count_unique_ingredients(dishes):
    unique = set()
    for value in dishes.values():
        for ingredient in value:
            if ingredient not in unique:
                unique.add(ingredient)
    return len(unique)
