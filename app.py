from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object("config")

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/blog/")
def blog():
    blog = blog_articles
    return render_template("blog.html", blog=blog)


# For different articles
# Currently only work if manually entered in URL
@app.route("/blog/<slug>")
def blogs(slug):
    if slug in blog_articles:
        title = blog_articles[slug]["title"]
        text = blog_articles[slug]["text"]
        return render_template("article.html", title=title, text=text)
    else:
        return "Article doesn't exist yet."


if __name__ == "__main__":
    app.run()
