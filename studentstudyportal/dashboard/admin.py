from django.contrib import admin

from dashboard.models import Notes,Homework,Todo,AppUser,Step





# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
admin.site.register(AppUser)
admin.site.register(Step)

