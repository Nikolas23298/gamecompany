from django.contrib import admin
from .import models

class GamesAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Game, GamesAdmin)
admin.site.register(models.Award, GamesAdmin)

