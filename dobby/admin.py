from django.contrib import admin

from .models import Skill, Login, User, UserSkill, CompletedTransaction, PendingTransaction, OngoingTransaction

admin.site.register(Skill)
admin.site.register(Login)
admin.site.register(User)
admin.site.register(UserSkill)
admin.site.register(CompletedTransaction)
admin.site.register(PendingTransaction)
admin.site.register(OngoingTransaction)