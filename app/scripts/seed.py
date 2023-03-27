from app.app import create_app
from app.articles.models import Article
from app.extensions.database import db


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()


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

for slug, article in blog_articles.items():
    new_article = Article(
        slug=slug, title=blog_articles[slug]["title"], text=blog_articles[slug]["text"]
    )
    db.session.add(new_article)

db.session.commit()
