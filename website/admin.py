from django.contrib import admin

from .models import Yoga_Retreat


class YogaRetreatAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "from_date")
    search_fields = ("title", "from_date")
    list_filter = ("from_date", "to_date")


admin.site.register(Yoga_Retreat, YogaRetreatAdmin)
