from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user_info/<int:pk>',views.user_info,name='user_info'),
    path('join/',views.join,name='join'),
    path('update/<int:pk>',views.update,name='update'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('password_change/<int:pk>',views.password_change,name='password_change')
]
