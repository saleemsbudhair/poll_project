from django.db import models


class Poll(models.Model):
    question = models.TextField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class PollOption(models.Model):

    name = models.CharField(max_length=30)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='votes')
    poll_option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name='votes')
