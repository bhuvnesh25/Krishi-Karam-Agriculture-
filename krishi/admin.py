from django.contrib import admin
# Register your models here.
from .models import *


admin.site.register(User)
admin.site.register(Address)
admin.site.register(Data)
admin.site.register(Mandi)