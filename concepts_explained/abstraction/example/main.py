from api import API

# Set the urls for the cat and dog api
catapi = "https://api.thecatapi.com/v1/images/search"
dogapi = "https://api.thedogapi.com/v1/images/search"

# Initialize the API class
api = API()

# Call the get_image method from the API class
cat_img = api.get_image(catapi)
dog_img = api.get_image(dogapi)
print(cat_img)
print(dog_img)