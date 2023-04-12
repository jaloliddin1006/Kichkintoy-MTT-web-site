from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


def home(request):
    # banner = Banner.objects.get(0)
    banner = Banner.objects.all()[0]
    classes = Group.objects.all()
    ctg = Teacher_category.objects.get(category="teacher")
    teachers = Teacher.objects.filter(category_id=ctg.pk)[:4]
    print(ctg)
    izohlar = Testimonial.objects.all()
    articles = Article.objects.order_by("-date")[:3]
    contacts = Contacts.objects.all()[0]

    context = {
        'banner': banner,
        'classes': classes,
        'teachers': teachers,
        'izohlar': izohlar,
        'articles': articles,
        'contacts': contacts,

    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/' )
    else:
        return render(request, 'index.html', context)


def about(request):
    banner = Banner.objects.all()[0]
    contacts = Contacts.objects.all()[0]
    ctg = Teacher_category.objects.get(category="teacher")
    teachers = Teacher.objects.filter(category=ctg.pk)[:4]
    print(len(teachers))
    context = {
        'banner':banner,
        'contacts': contacts,
        'teachers': teachers,
    }
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/about/' )
    else:
        return render(request, 'about.html', context)


def classes(request):
    classes = Group.objects.all()
    contacts = Contacts.objects.all()[0]
    context = {
       
        'classes': classes,
        'contacts': contacts,
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/class/' )
    else:
        return render(request, 'class.html', context)


def team(request):
    teachers = Teacher.objects.all()
    contacts = Contacts.objects.all()[0]
    izohlar = Testimonial.objects.all()
    context = {
        'teachers': teachers,
        'izohlar': izohlar,
        'contacts': contacts,
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/team/' )
    else:

        return render(request, 'team.html', context)


def galery(request):
    photos = Photo.objects.all()
    # print(Photo.objects.values_list('category', flat=True))
    contacts = Contacts.objects.all()[0]
    categories = Photo_categories.objects.all()
    
    category_filter = request.GET.get('category')
    if category_filter:
        ctg = Photo_categories.objects.get(category=category_filter)
        photos = Photo.objects.filter(category=ctg.pk)
    

    context = {
        'photos': photos,
        'contacts': contacts,
        'categories': categories,
        'category_filter': category_filter,
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/galery/' )
    else:
        return render(request, 'gallery.html', context)



def contact(request):
    
    contacts = Contacts.objects.all()[0]
    context = {
        'contacts': contacts,
    }

    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            my_model_obj = Message(
                name=name,
                email=email,
                subject=subject,
                message=message
                )
            my_model_obj.save()
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
        except:
            name = request.POST['name']
            phone = request.POST['phone']
            group = "Ma'lumot olish uchun"
            # print(name)
            my_model_obj = Booking_grop(
                name=name,
                phone=phone,
                group=group
                )
            my_model_obj.save()
        return redirect('/contact/' )
        
    else:
        return render(request, 'contact.html', context)
    # return render(request, 'contact.html', context)


def article(request):
    contacts = Contacts.objects.all()[0]
    articles = Article.objects.order_by("-date")
    category = Article_category
    # print(articles[0].photo.open())
    context = {
        'articles': articles,
        'contacts': contacts,
        'category': category,
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/article/' )
    else:
        return render(request, 'article.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    last_articles = Article.objects.order_by("-date")[:5]
    contacts = Contacts.objects.all()[0]
    context = {
        'article': article,
        'last_articles': last_articles,
        'contacts': contacts,
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        group = "Ma'lumot olish uchun"
        # print(name)
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        return redirect('/article/' )
    else:
        return render(request, 'article_detail.html', context)


def booking(request, pk):
    group = get_object_or_404(Group, pk=pk)
    all_gr = Group.objects.all()
    contacts = Contacts.objects.all()[0]
    context = {
        'group': group,
        'all_gr': all_gr,
        'contacts': contacts,
    }

    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        phone = request.POST['phone']
        print(phone)
        group = request.POST.get('group')
        print(group)
        if group != "":
            group = "Ma'lumot olish uchun"
        my_model_obj = Booking_grop(
            name=name,
            phone=phone,
            group=group
            )
        my_model_obj.save()
        messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi! \n Tez orada siz bilan a`loqaga chiqamiz')
        return redirect('/class/' )
    else:
        return render(request, 'booking.html', context)
    # return render(request, "booking.html", context)