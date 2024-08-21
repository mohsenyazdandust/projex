from django.contrib import admin

from .models import Student, Session, Exercise, Submitted

class ChannelAdmin(admin.StackedInline):
    model = Submitted
    fields = ['exercise', 'answer', 'feedback']
    readonly_fields = ['exercise', 'answer']
    extra = 0

class RuleAdmin(admin.ModelAdmin):
    model = Student
    fields = ['first_name', 'last_name']
    readonly_fields = ['first_name', 'last_name']
    inlines = [ChannelAdmin]
    
admin.site.register(Student, RuleAdmin)
admin.site.register(Session)
admin.site.register(Exercise)
admin.site.register(Submitted)