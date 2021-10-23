from django.urls import path
from .views import (
    Profile, 
    SignUp_function, 
    LogIn_function,
    Logout_function,
    Update_function,
) 

app_name = 'Users'

urlpatterns = [
    path('', Profile, name='Profile'),
    path('signup/', SignUp_function, name='SignUp'),
    path('login/', LogIn_function, name='LogIn'),
    path('logout/', Logout_function, name='Logout'),
    path('update/', Update_function, name='Update'),
]


