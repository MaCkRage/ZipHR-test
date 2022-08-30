from django.core.management.base import BaseCommand
from app.scripst import fill_db


class Command(BaseCommand):
    help = 'Fill Database.'

    def handle(self, *args, **options):
        fill_db()
        print("--- "
              "FILLING DATABASE DONE"
              "___")
