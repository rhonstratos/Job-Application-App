from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('employee/register/', views.employee_registration, name='employee-registration'),
    path('employer/register/', views.employer_registration, name='employer-registration'),
    path('profile/edit/<int:id>/', views.employee_edit_profile, name='edit-employee-profile'),
    path('profile/edit/employer/<int:id>/', views.employer_edit_profile, name='edit-employer-profile'),
    path('profile/edit/password/<int:id>/', views.edit_password, name='edit-password'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
    path('profile/delete/<int:id>/', views.delete_account, name='delete'),

	# url about reports
	path('reports/user/employees', views.user_report_employee, name='user-report-employee'),
	path('reports/user/employers', views.user_report_employer, name='user-report-employer'),
	path('reports/logs', views.log_report, name='log-report')
]
