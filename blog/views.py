from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, template_name="blog/index.html")


def blog_post(request):
    return render(request, template_name="blog/blog_post.html")


def feadbacks(request):
    return render(request, template_name="blog/feadbacks.html")
