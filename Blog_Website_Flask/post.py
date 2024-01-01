import requests
class Post:
    def all_post(self):
        blog_url = 'https://api.npoint.io/66ead361ad4e8d5a8c19'
        response = requests.get(blog_url)
        all_post = response.json()
        return all_post