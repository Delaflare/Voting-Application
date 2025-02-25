from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Polsster Admin Area"
admin.site.index_title = "Welcome to Pollster Admin"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3 # number of extra fields

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), 
    ('Date Information', 
    {'fields': ['pub_date'], 
    'classes':['collapse']}), ]

    inlines = [ChoiceInLine]

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)


# Register your models here.
