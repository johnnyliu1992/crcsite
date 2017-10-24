# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    Q_ID=models.AutoField(primary_key=True)
    Q_type=models.CharField(null=False, max_length=400)
    Q_category=models.CharField(null=False, max_length=400)
    Q_text=models.CharField(null=True, max_length=400)
    def __str__(self):
        return '%d %s %s %s' % (self.Q_ID, self.Q_type, self.Q_category, self.Q_text)
        
class Answer(models.Model):
    A_ID=models.AutoField(primary_key=True)
    Q_ID=models.ForeignKey(Question, on_delete=models.CASCADE)
    A_text=models.CharField(null=True, max_length=400)
    def __str__(self):
        return '%d %s %s \n' % (self.A_ID, self.Q_ID, self.A_text)
