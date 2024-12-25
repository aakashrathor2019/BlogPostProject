from django.urls import path
from .views import Signup, Login, CreatePost, Logout, Dashboard

urlpatterns = [
    path('', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('createpost/', CreatePost.as_view(), name='createpost'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]