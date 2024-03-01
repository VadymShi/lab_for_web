from django.contrib import admin
from .models import Office, Worker, Employment, Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
admin.site.register(Office)
admin.site.register(Worker)
admin.site.register(Employment)
