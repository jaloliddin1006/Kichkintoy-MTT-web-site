from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'group', 'date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_name', 'phone')

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')

admin.site.register(Contacts)
admin.site.register(Banner)
admin.site.register(Group)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Article_category)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Teacher_category)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Photo)
admin.site.register(Photo_categories)
admin.site.register(Message, MessageAdmin)
admin.site.register(Booking_grop, BookingAdmin)
