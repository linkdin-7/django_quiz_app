from . import views
from django.urls import include, path


urlpatterns = [
    path('user/create',views.UserCreateAPIView.as_view()),
    path('user/login',views.UserloginViewset.as_view()),
]