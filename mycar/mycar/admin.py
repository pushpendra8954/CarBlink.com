from django.contrib import admin
from mycar.models import Contact,Car,User

admin.site.register(Contact), #Registers your model here.After doing this goto the apps.py file and copy the name of your app and paste it into settings.py in installed apps section with App_1.apps.Copied_name.
admin.site.register(Car),
#admin.site.register(User),
# admin.site.register(User),