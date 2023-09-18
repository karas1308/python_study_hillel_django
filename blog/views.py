import datetime

from django.shortcuts import redirect, render

from animal.models import Animal
from blog.models import Blog, Feedback
from user.models import User


# Create your views here.

def index(request):
    posts = Blog.objects.all()
    return render(request, template_name="blog/index.html", context={"posts": posts})


def blog_post(request, post_id=1):
    post = Blog.objects.get(id=post_id)
    return render(request, template_name="blog/blog_post.html", context={"post": post})


def feedbacks(request):
    if request.method == "POST":
        animal_id = request.POST.get("animal_name")
        animal = Animal.objects.get(id=animal_id)
        user = User.objects.get(id=1)
        new_feedback = Feedback(title=request.POST["title"],
                                text=request.POST["text"],
                                media=request.POST["media"],
                                user=user,
                                date=datetime.datetime.date(datetime.datetime.utcnow()),
                                animal=animal)
        new_feedback.save()
        return redirect("/blog/feedbacks")

    else:
        animals = Animal.objects.all()
        animal_id = request.GET.get("animal_id")
        all_feedbacks = Feedback.objects.all()
        if animal_id:
            all_feedbacks = all_feedbacks.filter(animal_id=animal_id)
        results = all_feedbacks.all()
    return render(request, template_name="blog/feedbacks.html", context={"all_feedbacks": results,
                                                                         "animals": animals})
