from django.contrib import admin
from .models import User, Author, Books, Publisher

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Publisher)


