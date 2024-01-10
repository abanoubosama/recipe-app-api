"""
Django command to wait for DB to start
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django command to wait for DB """

    def handle(self, *args, **options):
        """Entry point of command"""
        self.stdout.write("Waiting for DB")

        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError) as e:
                self.stdout.write(f'DB unavailable, waiting for 1 second. {e}')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Database available"))
