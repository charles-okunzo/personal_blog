from datetime import datetime
import unittest
from app.models import User, BlogPost,Comment


class TestUser(unittest.TestCase):


  def setUp(self) -> None:
      self.new_user = User(password = 'my_password')

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_code is not None)

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password


  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('my_password'))


  def test_user_instance(self):
    self.assertTrue(isinstance(self.new_user, User))


class TestBlogPost(unittest.TestCase):

  def setUp(self) -> None:
      self.new_blog_post = BlogPost(id=1, title='My blog', category='Lifestyle', post='This blog is great', date=datetime.now)



  def test_instance(self):
    self.assertTrue(isinstance(self.new_blog_post, BlogPost))


class TestComment(unittest.TestCase):

  def setUp(self) -> None:
      self.new_comment = Comment(id=1, comment='Nice post')



  def test_instance(self):
    self.assertTrue(isinstance(self.new_comment, Comment))


if __name__ == '__main__':
  unittest.main()