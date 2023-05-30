from django.contrib import admin
from .models import Profile
# Register your models here.

# *In this class, the readonly_fields attribute is set to a tuple containing the field name 'id'.

# * By specifying 'id' as a readonly field, it means that the id field in the Profile model will be displayed as read-only in the admin interface. This prevents users from modifying the id field directly through the admin interface, making it read-only for viewing purposes only.
class ProfileAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)

