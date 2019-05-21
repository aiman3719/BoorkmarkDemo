import datetime
from unittest import TestCase

from django.urls import reverse
from django.utils import timezone

from polls.models import Question


def create_question(question_text, days):
    """
    Create a question with the given 'question_text'' and published the given
    number of 'days' offset to no (negative for questions published
    in the past,  positive for question that have yet to be published
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class TestDetailView(TestCase):

    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        :return:
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

