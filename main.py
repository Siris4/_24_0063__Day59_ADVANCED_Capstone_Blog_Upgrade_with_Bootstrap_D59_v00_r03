from flask import Flask, render_template, url_for
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    this_year = dt.datetime.now().year
    MY_NAME = "Gavin"
    # 'posts' is fetched from somewhere, here is a placeholder
    posts = [{'id': 1, 'title': 'First Post', 'subtitle': 'Welcome to the first post'},
             {'id': 2, 'title': 'Second Post', 'subtitle': 'Here is the second one'}]
    return render_template('index.html', greeting_string='Hello Jinja!',
                           num=random_number, CURRENT_YEAR=f'Copyright {this_year} - Built by {MY_NAME}',
                           posts=posts)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_response.raise_for_status()  # good practice to check for request success
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
