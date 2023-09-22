from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:post_id>', views.blog_post, name="blog_post"),
    path('feedbacks', views.feedbacks, name="feedbacks"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
