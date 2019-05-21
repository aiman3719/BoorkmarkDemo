from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date infomation', {'fields':['pub_date']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently') # method field도 출력할 수 있다.

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceInline)   # Inline타입은 별도로 Question처럼 임포터할 수 없다.
