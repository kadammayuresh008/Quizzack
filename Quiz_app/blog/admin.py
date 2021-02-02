from django.contrib import admin

# Register your models here.
from . models import quiz,Attempts,Test



admin.site.register(quiz)
admin.site.register(Attempts)
admin.site.register(Test)