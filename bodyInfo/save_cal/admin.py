from django.contrib import admin
from .models import FoodCal, ExerciseCal, UserCal

class FoodCalAdmin(admin.ModelAdmin):
    list_display = ('hamberger', 'pizza', 'chicken')  # 리스트에 표시할 필드
    search_fields = ('hamberger', 'pizza', 'chicken')  # 검색할 필드

class ExerciseCalAdmin(admin.ModelAdmin):
    list_display = ('walk', 'run', 'weight_training')  # 리스트에 표시할 필드
    search_fields = ('walk', 'run', 'weight_training')  # 검색할 필드

class UserCalAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'hamberger', 'pizza', 'chicken', 'walk', 'run', 'weight_training')  # 리스트에 표시할 필드
    search_fields = ('user', 'date', 'hamberger', 'pizza', 'chicken', 'walk', 'run', 'weight_training')  # 검색할 필드

admin.site.register(FoodCal, FoodCalAdmin)
admin.site.register(ExerciseCal, ExerciseCalAdmin)
admin.site.register(UserCal, UserCalAdmin)


