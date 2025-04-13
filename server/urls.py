from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login,name="login"),
    path('signup/', views.signup,name="signup"),
    path('test_token/', views.test_token,name="test_token"),
]
