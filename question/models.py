import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(default=timezone.now())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1)

    def check_answer(self, user_answer):
        if self.answer == user_answer:
            return True
        else:
            return False

    def __str__(self):
        return f"Question:{self.question_text} , date:{self.pub_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
