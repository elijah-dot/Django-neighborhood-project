from django.contrib import admin
from .models import Profile,Neighbourhood,Business,Contacts,School,Posts

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Contacts)
admin.site.register(School)
admin.site.register(Posts)
admin.site.register(Neighbourhood)

