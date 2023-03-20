from flask import Flask, render_template, request
import requests

POSTS_ENDPOINT = "https://api.npoint.io/7a3a2c178faddeb88683"

response = requests.get(POSTS_ENDPOINT)
posts_json = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts_json)

@app.route('/about')
def go_about():
    return render_template("about.html")

@app.route('/contact')
def go_contact():
    return render_template("contact.html")

@app.route('/login', methods=["POST"])
def receive_data():
    print(request.form["username"], request.form["email"], request.form["phone"], request.form["message"])
    return render_template("form-entry.html")

@app.route('/post/<int:num>')
def go_post(num):
    title = posts_json[num-1]["title"]
    subtitle = posts_json[num-1]["subtitle"]
    date = posts_json[num-1]["date"]
    author = posts_json[num-1]["author"]
    body = posts_json[num-1]["body"]
    image = posts_json[num-1]["image"]
    return render_template("post.html", title=title, subtitle=subtitle, date=date,
                           author=author, body=body, image=image)


if __name__ == '__main__': ### 또는 터미널에서 export FLASK_APP=main.py -> flask run
    app.run(port=8000)