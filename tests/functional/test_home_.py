from application.database import db
from application.models import User, Article, ArticleAuthors
from bs4 import BeautifulSoup

class TestArticles:
    def test_no_articles_home(self, client, init_database):
        response = client.get('/')
        assert b"<title>All Articles</title>" in response.data
        assert not ( b"ratings-icon" in response.data )

    def test_check_one_article_home(self, client, init_database):
        ## Insert User
        u = User(username='testUser', email='test@example.com', password="password", active=1)
        db.session.add(u)
        db.session.commit()

        ## Insert Article
        a = Article(title="My Aricle", content="My Content")
        db.session.add(a)
        db.session.commit()

        ## Author
        aa = ArticleAuthors(user_id=u.id, article_id=a.article_id)
        db.session.add(aa)
        db.session.commit()

        response = client.get('/')
        assert b"<title>All Articles</title>" in response.data
        assert b"ratings-icon" in response.data 
        soup = BeautifulSoup(response.data, "html.parser")
        ratings = soup.find_all("i", {"class": "ratings-icon"})
        assert len(ratings) == 1

    def test_404(self, client):
        response = client.get('/823749823764862387')
        assert response.status_code == 404
        assert b"<title>Application | 404 Not Found</title>" in response.data

