from django.contrib import admin
from .models import Feature, Service, Portfolio, Team, Review

# Register your models here.
admin.site.register(Feature)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Team)
admin.site.register(Review)