from django.urls import path
from user import api

urlpatterns = [
        path('createuser/', api.createuser, name="createuser"),
        path("login/", api.LoginAPI.as_view()),
        path('logoutall/', api.logoutall, name="logoutall"),
        path('logout/', api.logout, name="logout"),
        path('resetpassword/', api.resetpassword, name="resetpassword"), 
        
]   