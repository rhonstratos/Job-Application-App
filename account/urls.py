from django.urls import include, path
from account import views

app_name = "account"

urlpatterns = [
    # employee url
    path('employee/', include([
        path('register/', views.employee_registration,
             name='employee-registration'),
        path('<int:id>/profile/edit',
             views.employee_edit_profile, name='edit-profile'),
    ])),

    # employer url
    path('employer/', include([
        path('register/', views.employer_registration,
             name='employer-registration'),
        path('<int:id>/profile/edit',
             views.employer_edit_profile, name='employer-profile')
    ])),

    # general url
    path('account/', include([
        path('<int:id>/password/edit', views.employee_edit_password,
             name='employee-edit-password')
    ])),

    # path('profile/edit/password/<int:id>/',
    #      views.employee_edit_password, name='employee-edit-password'),
    
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
