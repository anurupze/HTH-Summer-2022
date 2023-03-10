"""" EXIT TICKET """
# Rename this file here & call it week4_exit.py

## Part I: Create a dictionary

# Create your food table here via key:value pairs
# (input the food & prices from lines 73-76):
food_prices = {
  "chicken": 1.59,
  "beef": 1.56,
  "cheese": 1.59,
  "milk": 1.29,
  "egg": .99,           
  "carrot": 2.99,
  "tomato": 2.49,
  "cauliflower": 2.29
  }
print(food_prices)            

# Retrieve any value from the food prices dictionary by using its corresponding key along with the bracket notation
# For example, to get the price for milk, run this:
milk_price = food_prices["milk"]
print(milk_price)

# Access the prices for each item & store into their own variable, just like the milk example.  
chicken_price = food_prices["chicken"]
print(chicken_price)

beef_price = food_prices["beef"]
print(beef_price)

cheese_price = food_prices["cheese"]
print(cheese_price)

egg_price = food_prices["egg"]
print(egg_price)

carrot_price = food_prices["carrot"]
print(carrot_price)

tomato_price = food_prices["tomato"]
print(tomato_price)

cauliflower_price = food_prices["cauliflower"]
print(cauliflower_price)

# Even though the task in hand asks you to create a variable to store the values of prices within the variable 
# If you just need to print the key values pair there is a code that can be used in two lines 
for food, price in food_prices.items():
  print(f"{food} : {price}") # these values are stored as string 
  
# If you need to just print the prices of food the following code can also be applied 
for price in food_prices.values():
  print(f"{price}")

## Part II. Create a list of the Spotify playlist

# First, add the songs in your section's list in 
playlist = [
  "Oliver Tree - Life Goes On",      
  "Conan Gray - Maniac",
  "Post Malone - Wow",
  "Weekend - Blinding Lights"
]

# Print the playlist in the line below:
print(playlist)

first_song = playlist[0] # playlist[-4] also works       
print(first_song)

# Lists have an index, which is a number assigned to each item in the list based on the oder in which they appear in the list, starting at 0. 
# What's the first song on your list?
#Oliver Tree - Life goes on

# Pick your top 2 favorite songs from the list & print them using the list's index to access them
fave_songs = playlist[1:3]  
print(fave_songs)

# Update your playlist by changing the last song to something else
playlist[3] = "J cole - Middle Child"
# print the playlist to show that you have updated it
print(playlist)

# Add another song to the end of the list using append()
playlist.append(" Post Malone: Candy Paint ")
# print the playlist to show that you added a new song
print(playlist)

# You changed your mind & want to delete the last song you just added
playlist.pop()
# Print the playlist to show that you deleted the last song
print(playlist)

# How many songs are in your list? Use len()
print(len(playlist))
# Write here how many songs are in your playlist = 4

# Sort your playlist in alphabetical order using sorted()
print(sorted(playlist))
# Write here the order of the songs in your playlist:
# ['Conan Gray - Maniac', 'J cole - Middle Child', 'Oliver Tree - Life Goes On', 'Post Malone - Wow']
