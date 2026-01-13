from django.contrib import admin
from .models import *


class RatingAdmin(admin.ModelAdmin):
    list_display = ('meal', 'user', 'stars')
    list_filter = ('user' , 'meal')
    readonly_fields = ('id',)

class MealAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    readonly_fields = ('id',)
    


# بدلاً من الكود القديم، استخدم هذا:

admin.site.register(Meal, MealAdmin)  # هنا ربطنا الموديل بالكلاس الخاص به
admin.site.register(Rating, RatingAdmin) # وهنا نفس الشيء