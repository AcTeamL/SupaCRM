# Register your models here.
from django.contrib import admin

from HelloApp.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('2Ololoshenki-lolo', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)