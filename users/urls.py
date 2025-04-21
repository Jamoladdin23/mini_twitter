from django.urls import path

from .views import RegisterViews, login_view, log_out

urlpatterns = [
    path('sign-up/', RegisterViews.as_view(), name="register"),
    path('login/', login_view, name='login'),
    path('logout/', log_out, name='logout')
]
