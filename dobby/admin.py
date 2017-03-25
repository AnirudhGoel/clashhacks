from django.contrib import admin

from .models import Skill, Login, User, Rating, Transaction

admin.site.register(Skill)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Transaction)