from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render

from animal.models import Animal
from blog.forms import FeedbackForm
from blog.models import Blog, Feedback


# Create your views here.

def index(request):
    posts = Blog.objects.all()
    return render(request, template_name="blog/index.html", context={"posts": posts})


def blog_post(request, post_id=1):
    post = Blog.objects.get(id=post_id)
    return render(request, template_name="blog/blog_post.html", context={"post": post})


def feedbacks(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = FeedbackForm(request.POST, request.FILES)
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            if feedback is not None:
                response_text = "ok"
                return HttpResponse(response_text)
            else:
                response_text = "fail"
                return HttpResponse(response_text)
        else:
            return redirect("/login")
    else:
        animals = Animal.objects.all()
        animal_id = request.GET.get("animal_id")
        all_feedbacks = Feedback.objects.all()
        if animal_id:
            all_feedbacks = all_feedbacks.filter(animal_id=animal_id)
        results = all_feedbacks.all()
    form = FeedbackForm()
    return render(request, template_name="blog/feedbacks.html", context={"all_feedbacks": results,
                                                                         "animals": animals, "form": form})
