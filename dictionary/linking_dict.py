def get_regional_settings(computer_settings, user_settings):
  defaults = {'language': 'English', 'currency': 'USD', 'timezone': 'PST'}
  new = defaults.copy() #copy default values into the new dict
  new.update(computer_settings)
  new.update(user_settings)
  return new


# sample data for tests
computer_input = {'language': 'Polish'}
user_input = {'timezone': 'UTC'}
print(get_regional_settings(computer_input, user_input))