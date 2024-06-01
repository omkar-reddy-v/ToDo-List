from django.urls import path
from . import views

urlpatterns = [
    path('add',views.addtasks,name='addtaskadd'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('alltasks',views.alltasks,name='alltasks'),
    path('edit/<id>',views.edittask,name='edit'),
    path('deleteall',views.deteleall,name='deleteall'),
    path('delete/<id>',views.deleteone,name='deleteone'),
]
