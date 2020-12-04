from django.urls import path, include

from accounts.views import user_profile, signup_user, signout_user, edit_profile, delete_profile

urlpatterns = [
    path('profile/', user_profile, name='user profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('', include('django.contrib.auth.urls')),
    path('signup/', signup_user, name='signup user'),
    path('signout/', signout_user, name='signout user'),
]