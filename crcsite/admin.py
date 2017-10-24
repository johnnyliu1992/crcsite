# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3
    list_display=('A_text')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Q_text']}),
        ('Question information', {'fields': ['Q_category', 'Q_type']}),
    ]
    list_display=('Q_text','Q_category', 'Q_type')
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)

