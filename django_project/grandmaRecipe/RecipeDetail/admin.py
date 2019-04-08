from django.contrib import admin
from RecipeDetail.models import Recipe, Comment, Specialgroup

# Register your models here.
#from unesco.models import Site, Category, States, Region, Iso

admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Specialgroup)
#admin.site.register(States)
#admin.site.register(Iso)
#admin.site.register(Region)
