import requests

class API ():
    def get_image(self, url):
        response = requests.get(url)
        return response.json()
