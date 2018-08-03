from django.contrib import admin

# Register your models here.
from cell.models import User
from cell.models import Offer
from cell.models import SimCard

admin.site.register(User)
admin.site.register(Offer)
admin.site.register(SimCard)