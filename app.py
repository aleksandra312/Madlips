from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)

app.config['SECRET_KEY'] = "my-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Returns Home Page Form"""
    words = story.prompts
    return render_template("home.html", prompts = words)


@app.route('/story')
def story_page():
    """Returns Story Page"""
    text = story.generate(request.args)
    return render_template("story.html", story = text)



