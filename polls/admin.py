from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date infomation', {'fields':['pub_date']}),
    ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceInline)   # Inline타입은 별도로 Question처럼 임포터할 수 없다.
