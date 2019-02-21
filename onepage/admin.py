from django.contrib import admin
from .models import General, AboutDescription, AboutProfileDescription
# Register your models here.


class AdminGeneral(admin.ModelAdmin):
    class Meta:
        model = General
        fields = ('banner_home',)

admin.site.register(General, AdminGeneral)
admin.site.register(AboutDescription)
admin.site.register(AboutProfileDescription)
