from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('active_index/', views.active_index, name='active_index'),
    path('active_studentinfo_checkout/', views.active_studentinfo_checkout_view, name='active_studentinfo_checkout'),
    path('active_studystash_store/', views.active_studystash_store, name='active_studystash_store'),
    path('active_session_expired/', views.active_session_expired, name='active_session_expired'),
    path('active_session_membership/', views.active_session_membership, name='active_session_membership'),
    path('active_first_time_user/', views.active_first_time_user, name='active_first_time_user'),
    path('account-deactivated/', views.active_account_deactivated_view, name='active_account_deactivated'),
    # all the above are restricted
    path('accounts/login/', LoginView.as_view(), name='login'),
    # all the below are public
    path('', views.index_view, name='index'),
    path('statements/', views.statements_view, name='statements'),
    path('studystash/', views.normal_studystash_store, name='normal_studystash_store'),
    path('register/', views.normal_register, name='normal_register'),
    path('forgot_password/', views.normal_forgot_password, name='normal_forgot_password'),
    path('logout/', views.user_logout, name='logout'),
]
