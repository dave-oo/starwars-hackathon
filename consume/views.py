from django.views.generic import TemplateView
import swapi
from .models import Person


class HomeView(TemplateView):
    """
    The home page
    """
    template_name = 'consume/Home.html'

    def get_context_data(self, **kwargs):
        """
        Get people from the api and save them to the database after
        truncating all data
        """
        data = super().get_context_data(**kwargs)

        Person.objects.all().delete()

        # Person with id of 1
        person_1 = swapi.get_person(1)

        Person.objects.create(
            name=person_1.name,
            eye_color=person_1.eye_color,
            height=person_1.height,
            birth_year=person_1.birth_year,
            gender='hidden'
        )

        people = swapi.get_all('people')
        people_with_blue_eyes = []

        for person in people.items:
            if person.eye_color == 'blue':
                people_with_blue_eyes.append(person)

        # People with blue eyes
        for person in people_with_blue_eyes:
            if person.name != person_1.name:
                Person.objects.create(
                    name = person.name if person.name else 'hidden',
                    eye_color = 'hidden',
                    height = person.height if person.height else 'hidden',
                    birth_year = 'hidden',
                    gender = person.gender if person.gender else 'hidden'
                )

        data.update({'people': Person.objects.all()})
        return data

