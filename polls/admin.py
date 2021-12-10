from django.contrib import admin
from .models import Person, Poll, Movie

# Register your models here.
admin.site.register(Person)
admin.site.register(Poll)
admin.site.register(Movie)