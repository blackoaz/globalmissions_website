from django.shortcuts import render

# Create your views here.
# Home page view
def home(request):

    return render(request, 'home/home.html')

# What We Do page view
def what_we_do(request):

    return render(request, 'home/what_we_do.html')

# About Us page view
def about(request):

    return render(request, 'home/about.html')

# Partners page view
def partners(request):

    return render(request, 'home/partners.html')

# Contacts page view
def contacts(request):

    return render(request, 'home/contacts.html')

# Blogs page view
def blogs(request):

    return render(request, 'blogs/blogs_home.html')
