import datetime

from django.db import models
from django.utils import timezone

class Todo(models.Model) :
    todo = models.TextField()
    last_date = models.TextField( null=True)


class Last_Date(models.Model) :
    pub_date = models.DateTimeField(null=True, default=timezone.now())

 