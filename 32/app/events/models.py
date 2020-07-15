from django.db import models

from events.functions import get_dates_for_range


class Event(models.Model):
    title = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._create_dates()

    def _create_dates(self):
        """
        Delete all related instances of EventDate
        create instances for dates between events start & end
        """
        self.dates.all().delete()
        for date in get_dates_for_range(self.date_from, self.date_to):
            EventDate.objects.create(date=date, event=self)


class EventDate(models.Model):
    date = models.DateField()
    event = models.ForeignKey("Event", related_name="dates", on_delete=models.CASCADE)
