from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet
# Register your models here.

# unregister Groups
admin.site.unregister(Group)

# mix prifile into user
class ProfileInline(admin.StackedInline):
	model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
	model = User
	# just display username field on admin page
	fields = ["username"]
	inlines = [ProfileInline]

# unregister initial User
admin.site.unregister(User)
# register user and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

# register tweet
admin.site.register(Tweet)