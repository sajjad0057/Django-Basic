from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTest(TestCase):

    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.

    ** here f_q = future Question . 
    """
    def test_was_pub_recently_with_future_question(self):  #Methods are must be start with 'test' keyword . 
        time = timezone.now() + datetime.timedelta(days=30)
        print("Actual Time ----->",timezone.now())
        print("Future time -----> ",time)
        future_question = Question(published_date = time )
        self.assertIs(future_question.was_published_recently(),False)


    def test_was_pub_recently_with_old_question(self):  #Methods are must be start with 'test' keyword . 
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        print("Old time --------> ",time)
        old_question = Question(published_date = time )
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_pub_recently_with_recent_question(self):  #Methods are must be start with 'test' keyword . 
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        print("Recent time ------->",time)
        recent_question = Question(published_date = time )
        self.assertIs(recent_question.was_published_recently(),True)





