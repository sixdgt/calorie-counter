from django.contrib import admin

from ccapp.models import AppUser, HealthStatus, Diet

# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'contact',\
         'email', 'gender', 'dob', 'blood_group', 'password', \
            'created_at')
    list_filter = ('first_name', 'created_at')
    search_fields = ('first_name', 'last_name')

class HealthStatusAdmin(admin.ModelAdmin):
    list_display = ('health_issue', 'description', 'created_at')

# class DietAdmin(admin.ModelAdmin):
#     list_display = ('diet_title', 'diet_plan', 'diet_duration',\
#         'medicine_details', 'created_at')

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(HealthStatus, HealthStatusAdmin)
# admin.site.register(Diet, DietAdmin)

admin.site.site_title = "Dashboard"
admin.site.site_header = "Admin"
admin.site.index_title = "Admin"
admin.site.app_index = "CCAPP"
