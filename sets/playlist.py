songs_in_order = {
  'John': ['Girls Like You', 'Shallow', 'Faded', 'Sugar', 'Girls Like You', 'Dancing With A Stranger', 'Happy', 'Happy', 'Happy'], 
  'Mark': ['Shallow', 'Freaky', 'I can\'t get enough', 'A thousand years', 'A thousand years', 'Rolling in the Deep', 'Someone Like You', 'Rolling in the Deep', 'Halo', 'On The Floor', 'Hello', 'Shallow'], 
  'Stephanie': ['Dua Lipa', 'Shallow', 'Dua Lipa', 'Taki Taki', 'Chandelier', 'Chandelier', 'Blank Space', 'Blank Space', 'Counting Stars', 'Wake Me Up', 'Dua Lipa']
}

playlists = {}

for key, value in songs_in_order.items():
    playlists[key] = list(set(value))

print(playlists)