from django.contrib import admin
from .models import YogaClass, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


class YogaClassAdmin(admin.ModelAdmin):
    inlines = [BookingInline]
    fields = ("name", "date", "slots")


admin.site.register(YogaClass, YogaClassAdmin)
admin.site.register(Booking)
