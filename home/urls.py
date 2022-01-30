from django.urls import include, path

from . import views

# from django.contrib.auth import views as auth_views
# from allauth.account.views import SignupView

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('', views.index, name='index'),
]
