from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captainamerica@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='ironman@marvel.com', type='run', duration=30, date='2023-01-01'),
            Activity(user='batman@dc.com', type='cycle', duration=45, date='2023-01-02'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
