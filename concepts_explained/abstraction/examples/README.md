# (Layers of) Abstraction
The following is a short example of abstraction, visualised using a python script that makes an api call to `the cat api`. 

## An example of layers of abstraction
Say you write a python script that makes an api call to `the cat api`.  
```python
import requests

response = requests.get("https://api.thecatapi.com/v1/images/search")
print(response.json())
```
This code works, but if i want to make multiple api calls to `the cat api` i would have to copy and paste this code multiple times.  
Instead of doing that, i can write a function that makes the api call and then call that function whenever i want to make an api call.  
*main.py*  
```python
import requests

def get_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    return response.json()

img = get_cat_image()
print(img.json())
```
Now, this code works and does the same as the previous, however, if i want to make an api call to `the dog api` i would have to write another function that makes the api call to `the dog api`.
Instead of doing that, i can write a function that makes the api call and takes the url as an argument.  
*main.py*  
```python
import requests

def get_image(url):
    response = requests.get(url)
    return response.json()

cat_img = get_image("https://api.thecatapi.com/v1/images/search")
dog_img = get_image("https://api.thedogapi.com/v1/images/search")
print(cat_img.json())
print(dog_img.json())
```
Now, with this code we can use the `get_image` function to make api calls to any api we want.
However, if we have many different functions doing many different things, keeping them all in one file can get messy.
Instead of doing that, we can put the functions in a class and then call the functions from that class.    
*backends/api.py*
```python
import requests

class API ():
    def get_image(self, url):
        response = requests.get(url)
        return response.json()

```
*main.py*
```python
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
```
Please note that the main.py file does not need to import the "requests" module.  
This is because the api.py file already imports the "requests" module, and makes the request.  
Since the main.py file doesn't "see" what the api.py file does, it has abstracted the request making process.