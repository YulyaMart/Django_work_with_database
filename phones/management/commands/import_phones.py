import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                name=phone['name'], 
                image = phone['image'], 
                price = phone['price'],
                release_date = phone['release_date'], 
                lte_exists = phone['lte_exists'],
                slug=phone['name'].lower().replace(' ', '-'),
            )
           




    # phones_data = []
    # with open('phones.csv', 'r', newline='', encoding='utf-8') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         phones_data.append(row)