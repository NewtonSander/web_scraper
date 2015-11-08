from django.core.management.base import BaseCommand
from djcelery.models import CrontabSchedule, PeriodicTask

class Command(BaseCommand):

    def handle(self, *args, **options):
        crontrab_schedule, created = CrontabSchedule.objects.get_or_create(minute="*/3")
        periodic_task, created = PeriodicTask.objects.get_or_create(name="scrap site")
        periodic_task.crontab = crontrab_schedule
        periodic_task.save()