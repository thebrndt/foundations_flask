from flask import Blueprint, render_template

blueprint = Blueprint("simple_pages", __name__)


@blueprint.route("/")
def index():
    return render_template("index.html")


@blueprint.route("/about/")
def about():
    return render_template("about.html")
