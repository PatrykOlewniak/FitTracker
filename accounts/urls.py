from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path('register', views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]

#
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # other paths...
# ]