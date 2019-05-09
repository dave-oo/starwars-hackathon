from django.test import TestCase
from .models import Person


class TestApiConsume(TestCase):
    def test_sanity(self):
        """
        Sanity check for the person model
        """
        Person.objects.create(
            name='test name',
            eye_color='blue',
            height='120',
            birth_year='2222',
            gender='hidden'
        )
        self.assertEqual(Person.objects.count(), 1)
