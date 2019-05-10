from flask import render_template
from mypage import app


@app.route("/")
@app.route("/index")
def index():
	return "This is the index page"
