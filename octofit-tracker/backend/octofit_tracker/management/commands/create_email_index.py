from django.core.management.base import BaseCommand
from djongo import connection

class Command(BaseCommand):
    help = 'Ensure a unique index on the email field for the user collection.'

    def handle(self, *args, **kwargs):
        db = connection.cursor().db_conn.client['octofit_db']
        result = db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS(f'Created unique index on email: {result}'))
