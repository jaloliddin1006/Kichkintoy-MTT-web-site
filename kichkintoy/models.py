from django.db import models
from django.forms import TextInput
from django.core.validators import validate_email
from ckeditor.fields import RichTextField
from django import forms

class Contacts(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    mini_description = RichTextField(null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField()
    phone_1 = models.CharField(max_length=20, null=True, blank=True)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)
    work_days = models.CharField(max_length=50, null=True, blank=True)
    work_time = models.CharField(max_length=50, null=True, blank=True)

    insta_lik = models.CharField(max_length=400, null=True, blank=True)
    telegram_link = models.CharField(max_length=400, null=True, blank=True)
    facebook_link = models.CharField(max_length=400, null=True, blank=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Email xato kiritilgan")
        return email
    
    def __str__(self) -> str:
        return "Our Contacts"

class Banner(models.Model):
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    header_subtitle = models.CharField(max_length=250, null=True, blank=True)
    header_title = models.CharField(max_length=120, null=True, blank=True)
    header_description = RichTextField( null=True, blank=True)
    header_photo = models.ImageField(upload_to="photos/",null=True, blank=True)

    about_title = models.CharField(max_length=120, null=True, blank=True)
    header_description_full = RichTextField( null=True, blank=True)


    def __str__(self) -> str:
        return self.header_title

        

class Group(models.Model):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    name = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField( null=True, blank=True)
    ages = models.CharField(max_length=200, null=True, blank=True, )
    seats = models.IntegerField()
    time = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=50,null=True, blank=True)
    photo = models.ImageField(upload_to="photos/",null=True, blank=True)


    def __str__(self):
        return self.name
    

class Article_category(models.Model):
    class Meta:
        verbose_name = "Article_category"
        verbose_name_plural = "Articles_category"
    category = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self) -> str:
        return self.category

class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=400, null=True, blank=True)
    desc = RichTextField(null=True, blank=True)
    photo = models.ImageField(upload_to="photos/",null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    categoryID = models.ForeignKey(Article_category, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.title
    
class Teacher_category(models.Model):
    class Meta:
        verbose_name = "Teacher_category"
        verbose_name_plural = "Teachers_categories"
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category

class Teacher(models.Model):
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('Teacher_category',  on_delete=models.CASCADE, null=True, blank=True)
    job_name = models.CharField(max_length=200, null=True, blank=True)
    work_time = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    insta = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="photos/",null=True, blank=True)
    # date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    class Meta: 

        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    name = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    description = RichTextField( null=True, blank=True)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)


    def __str__(self) -> str:
        return self.name
    



class Photo_categories(models.Model):
    class Meta:

        verbose_name = "Photo_category" 
        verbose_name_plural = "Photos_category" 

    category = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.category

class Photo(models.Model):
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
    category = models.ForeignKey('Photo_categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to="photos/gallery/", null=True, blank=True)
    
    def __str__(self):
       return self.title
   

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Booking_grop(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name