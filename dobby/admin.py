from django.contrib import admin

from .models import Skill, Login, User, Rating, CompletedTransaction, PendingTransaction

admin.site.register(Skill)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(CompletedTransaction)
admin.site.register(PendingTransaction)