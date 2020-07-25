users = [
  ('Maria', 'Greek'), ('Jean', 'Maltese'),
  ('Juan', 'Spanish'), ('Dima', 'Ukrainian'),
  ('Agata', 'Thai'), ('Rafal', 'Polish'),
  ('Diego', 'Turkish'), ('Stan', 'Panamanian'),
  ('John', 'Australian'), ('Frank', 'Belgian'),
  ('Jane', 'Canadian'), ('Paul', 'Argentinian'),
  ('Taylor', 'Danish'), ('Kate', 'American'),
  ('Mark', 'Sri Lankan'), ('Jane', 'Japanese'),
  ('Ted', 'Indian'), ('Jean', 'Egyptian') 
]

nationality_to_continents = {
  'Greek': 'Europe', 'Maltese': 'Europe', 
  'Spanish': 'Europe', 'Ukrainian': 'Europe', 
  'Thai': 'Asia', 'Polish': 'Europe', 
  'Turkish': 'Asia', 'Panamanian': 'Central America', 
  'Australian': 'Australia', 'Belgian': 'Europe', 
  'Canadian': 'North America', 'Argentinian': 'South America', 
  'Danish': 'Europe', 'American': 'North America', 
  'Sri Lankan': 'Asia', 'Japanese': 'Asia', 
  'Indian': 'Asia', 'Egyptian': 'Africa'
}

users_continents = {}

for user in users:
    _, country = user
    if nationality_to_continents[country] not in users_continents:
        users_continents[nationality_to_continents[country]] = 1
    users_continents[nationality_to_continents[country]] += 1


# for key, value in nationality_to_continents.items():
#     for user in users:
#         _, country = user
#         if country not in key:
#             users_continents[value] = 0
#         users_continents[value] += 1

# for user in users:
#     _, country = user #unpacking user tuple
#     print(country)
#     for key, value in nationality_to_continents.items():
#         users_continents[value] = country
#         # if country == key:
#         #     users_continents[value] +=1
#         #     print(users_continents[value])
#         # #users_continents[value] += 1

print(users_continents)