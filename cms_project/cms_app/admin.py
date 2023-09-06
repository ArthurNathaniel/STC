# from django.contrib import admin
# # from .models import Church_Member
# # Register your models here.
# # admin.site.register(Church_Member)
from django.contrib import admin
from .models import ChurchMember
from .models import Payment
from .models import Document
# from .models import Parent

admin.site.register(ChurchMember)
admin.site.register(Payment)
admin.site.register(Document)
