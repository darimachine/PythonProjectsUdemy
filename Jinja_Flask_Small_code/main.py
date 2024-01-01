from flask import Flask,render_template
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',)
@app.route('/guess/<string:name>')
def guess(name):
    response = requests.get(f'https://api.genderize.io?name={name.lower()}')
    data_gender = response.json()
    print(data_gender)
    response = requests.get(f'https://api.agify.io?name={name.lower()}')
    data_age = response.json()
    return render_template("guess.html",name=name,gender=data_gender['gender'],age=data_age['age'])
@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/66ead361ad4e8d5a8c19'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html',posts=all_posts)
if __name__ == '__main__':
    app.run(debug=True)