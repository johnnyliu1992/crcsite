# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Question(models.Model):
    Q_ID=models.AutoField(primary_key=True)
    TYPE_CHOICES = (
        ('Choice', 'Choice'),
        ('Fill', 'Fill'),
    )
    Q_type=models.CharField(null=False, max_length=100, choices=TYPE_CHOICES)
    CATEGORY_CHOICES = (
        ('Heredity and medical history', 'Heredity and medical history'),
        ('Behavioral factors', 'Behavioral factors'),
        ('Factors decrease risks', 'Factors decrease risks'),
    )
    Q_category=models.CharField(null=False, max_length=100, choices=CATEGORY_CHOICES)
    Q_text=models.CharField(null=True, max_length=400)
    def __str__(self):
        return '%d %s %s %s' % (self.Q_ID, self.Q_type, self.Q_category, self.Q_text)


@python_2_unicode_compatible      
class Answer(models.Model):
    A_ID=models.AutoField(primary_key=True)
    Q_ID=models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    A_text=models.CharField(null=True, max_length=400)
    Value=models.DecimalField(decimal_places=1, max_digits=5, null=True)
    def __str__(self):
        return '%d %s %s \n %d' % (self.A_ID, self.Q_ID, self.A_text, self.Value)
