from django.urls import path
from authentication.views import LOGIN, LOGOUT, REGISTER
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("LOGIN", LOGIN, name="LOGIN"),
    path("LOGOUT", LOGOUT, name="LOGOUT"),
    path("REGISTER", REGISTER, name="REGISTER"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='auth/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='auth/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
         template_name='auth/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
]
