from django.urls import path, include

from accounts.views import user_profile, signup_user, signout_user, edit_profile, delete_profile, user_addresses, \
    edit_address, delete_address, user_favorites, create_address, edit_phone

urlpatterns = [
    path('profile/', user_profile, name='user profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('phone/edit/', edit_phone, name='edit phone'),

    path('', include('django.contrib.auth.urls')),
    path('signup/', signup_user, name='signup user'),
    path('signout/', signout_user, name='signout user'),

    path('addresses/', user_addresses, name='user addresses'),
    path('address/create/', create_address, name='create address'),
    path('address/edit/<int:pk>', edit_address, name='edit address'),
    path('address/delete/<int:pk>', delete_address, name='delete address'),

    path('favorites/', user_favorites, name='user favorites'),
]
