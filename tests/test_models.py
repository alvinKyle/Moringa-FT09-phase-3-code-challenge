import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author_id = 1
        author_name = "John Doe"
        author = Author(author_id, author_name)
        self.assertEqual(author.name, author_name)

    def test_article_creation(self):
        author = Author(1, "John Doe")  
        magazine = Magazine(1, "Tech Weekly", "Technology")  
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")


    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_get_author_by_id(self):
        new_author = Author.create('Jane Doe')
        author_id = new_author.id
        self.assertIsInstance(author_id, int)
        retrieved_author = Author.get_by_id(author_id)
        self.assertEqual(retrieved_author.name, 'Jane Doe')

    def test_reject_change_after_instantiation(self):
        author = Author(1, 'John Doe')
        author.name = 'Jane Doe'
        self.assertEqual(author._name, 'John Doe')

    def test_magazine_id_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        magazine.id = "invalid"  

    def test_magazine_name_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        magazine.name = 123  
        magazine.name = "A"  
        magazine.name = "A" * 17  

    def test_magazine_category_setter_getter(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.category, "Technology")
        magazine.category = "Science"
        self.assertEqual(magazine.category, "Science")

    def test_title_property(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.title, "Test Title")
        with self.assertRaises(AttributeError):
           article.title = "New Title"

    def test_article_title_constraints(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Valid Title", "Test Content")
        self.assertEqual(article.title, "Valid Title")
        with self.assertRaises(AttributeError):
            article.title = "New Title"
        with self.assertRaises(ValueError):
            Article(author, magazine, 12345, "Test Content")
        with self.assertRaises(ValueError):
            Article(author, magazine, "1234", "Test Content")
        with self.assertRaises(ValueError):
            Article(author, magazine, "T" * 51, "Test Content")


    def test_article_title_immutable(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(author, magazine, "Initial Title", "Test Content")
        self.assertEqual(article.title, "Initial Title")
        with self.assertRaises(AttributeError):
            article.title = "New Title"

    def test_get_author(self):
        author_name = "John Doe"
        author = Author(1, author_name) 
        magazine_name = "Tech Weekly"
        magazine_category = "Technology"
        magazine = Magazine(1, magazine_name, magazine_category)  
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.author.name, author_name)

    def test_get_magazine(self):
        author_name = "John Doe"
        author = Author(1, author_name) 
        magazine_name = "Tech Weekly"
        magazine_category = "Technology"
        magazine = Magazine(1, magazine_name, magazine_category)  
        article = Article(author, magazine, "Test Title", "Test Content")
        self.assertEqual(article.magazine.name, magazine_name)
        self.assertEqual(article.magazine.category, magazine_category)

    def test_articles(self):
        author = Author.create("John Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article1 = Article(author, magazine, "Article 1", "Content 1")
        article2 = Article(author, magazine, "Article 2", "Content 2")
        articles = author.articles()
        self.assertEqual(len(articles), 2)

    def test_magazines(self):
        author = Author.create("John Doe")
        magazine1 = Magazine.create("Tech Weekly", "Technology")
        magazine2 = Magazine.create("Science Monthly", "Science")
        article1 = Article(author, magazine1, "Article 1", "Content 1")
        article2 = Article(author, magazine2, "Article 2", "Content 2")
        magazines = author.magazines()
        self.assertEqual(len(magazines), 2)
        self.assertEqual(magazines[0][1], "Tech Weekly")
        self.assertEqual(magazines[1][1], "Science Monthly")

    def test_contributors(self):
        author = Author.create("John Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article1 = Article(author, magazine, "Article 1", "Content 1")
        article2 = Article(author, magazine, "Article 2", "Content 2")
        contributors = magazine.contributors()
        self.assertEqual(len(contributors), 2)

    def test_articles_2(self):
        author = Author.create("John Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article1 = Article(author, magazine, "Article 1", "Content 1")
        article2 = Article(author, magazine, "Article 2", "Content 2")
        articles = magazine.articles()
        self.assertEqual(len(articles), 2)

    def test_article_titles_no_articles(self):
        magazine = Magazine.create('Empty Magazine', 'Category')
        titles = magazine.article_titles()
        self.assertIsNone(titles)

    def test_contributing_authors(self):
        author1 = Author.create("John Doe")
        author2 = Author.create("Jane Doe")
        magazine = Magazine.create("Tech Weekly", "Technology")
        article1 = Article(author1, magazine, "Article 1", "Content 1")
        article2 = Article(author2, magazine, "Article 2", "Content 2")
        contributing_authors = magazine.contributing_authors()
        self.assertEqual(len(contributing_authors), 0)


        
if __name__ == "__main__":
    unittest.main()
