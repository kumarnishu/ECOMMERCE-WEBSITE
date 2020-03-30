from django.contrib import admin
from app.models import *

admin.site.register(User)
admin.site.register(Contacts)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Order)