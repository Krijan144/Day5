from django.contrib import admin
from .models import QuestionModel, AnswerModel,CategoryModel

admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
admin.site.register(CategoryModel)
