from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    # employer url
    path('employer/register/', views.employer_registration, name='employer-registration'),
    path('employer/edit/<int:id>/', views.employer_edit_profile, name='employer-profile'),

    # employee url
    path('employee/register/', views.employee_registration, name='employee-registration'),
    path('profile/edit/<int:id>/', views.employee_edit_profile, name='edit-profile'),
    path('profile/edit/password/<int:id>/', views.employee_edit_password, name='employee-edit-password'),

    # general url
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
