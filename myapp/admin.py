from django.contrib import admin
from .models import Feature, Service, Portfolio, Team, Review, Faq, UserForm, SpForm, UserProfile, Contact
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Feature)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Team)
admin.site.register(Review)
admin.site.register(Faq)
admin.site.register(UserForm)
admin.site.register(SpForm)
admin.site.register(Contact)

admin.site.unregister(User)

class UserProfileInline(admin.TabularInline):
    model = UserProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)