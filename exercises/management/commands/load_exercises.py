from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command

import json


class Command(BaseCommand):
    args = ''
    help = 'Loads the initial data of exercises into database'

    def handle(self, *args, **options):
        call_command('loaddata', 'exercises/fixtures/exercises.json', verbosity=1)
        result = {'message': "Successfully Loading initial data of exercises."}
        return json.dumps(result)