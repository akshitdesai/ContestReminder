from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SignUpView, ProfileView, DeleteUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('delete/', login_required(DeleteUserView.as_view()), name='delete'),
]
