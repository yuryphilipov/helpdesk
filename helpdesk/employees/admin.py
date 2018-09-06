from django.contrib import admin
from .models import Person, Department

#admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'tabn', 'job_position', 'department')
    list_filter = ('department',)
    
    fieldsets = (
        (None, {
            'fields': ('last_name', 'first_name', 'middle_name', 'birthdate')
        }),
        ('Данные о сотруднике', {
            'fields': ('department', 'job_position', 'tabn')
        }),
    )            


admin.site.register(Department)
