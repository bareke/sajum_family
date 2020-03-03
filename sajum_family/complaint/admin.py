from django.contrib import admin
from .models import Citizen
from .models import Officer
from .models import Vereda
from .models import Municipality
from .models import Department

# Register your models here.

admin.site.register([Citizen, Officer, Vereda, Municipality, Department])