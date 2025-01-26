from django.urls import path


from . import views

app_name = 'userprofile'
urlpatterns = [
        path('sign-up/' ,views.signup ,name='signup'), 
        path('myaccount/',views.myaccount, name='myaccount'),
    
]
