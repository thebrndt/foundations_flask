from flask import Blueprint, render_template
from .models import Article

blog_articles = {
    "article_1": {
        "title": "Foundations of Web Dev",
        "text": "This is just some text for the article.",
    },
    "article_2": {
        "title": "Living in Berline",
        "text": "Some more text for the article.",
    },
    "article_3": {
        "title": "Bumble Bees are Dying",
        "text": "This is just some text for the article.",
    },
    "article_4": {"title": "Meow Meow Meow", "text": "Bananas are a-meow-zing!"},
}

blueprint = Blueprint("articles", __name__)


@blueprint.route("/blog/")
def blog():
    # blog = blog_articles.values()
    # blogs = blog_articles
    # print(blogs)
    all_blogs = Article.query.all()
    print("hello")
    print(all_blogs)
    # maybe change route
    return render_template("blog.html", blogs=all_blogs)


@blueprint.route("/blog/<slug>")
def blogs(slug):
    blog = Article.query.filter_by(slug=slug).first()
    print(blog)
    if blog:
        title = blog.title
        text = blog.text
        return render_template("articles/article.html", title=title, text=text)
    else:
        return "Article doesn't exist yet."
