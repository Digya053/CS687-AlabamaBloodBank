from django.contrib import admin

from .models import RegisteredUsers
from .models import Blood

# Register your models here.
admin.site.register(RegisteredUsers)
admin.site.register(Blood)
