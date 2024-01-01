
from flask import Flask, render_template
from post import Post

blog = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=blog.all_post())
@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    requested_post=None
    for post in blog.all_post():
        if blog_id==post['id']:
            requested_post = post
            break
    return render_template('post.html', post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
