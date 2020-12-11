from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, ProfileForm, AddressForm, PhoneForm
from accounts.models import Profile, Address
from shop.models import Item


@login_required
def user_profile(request):
    context = {
        'user': request.user,
        'profile': request.user.profile,
    }
    return render(request, 'accounts/user_profile.html', context)


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        #  &qy^a}ay4J\vpXeR
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile(
                user=user,
                phone=request.POST['phone']
            )
            profile.save()

            login(request, user)
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/signup.html', context)


@login_required
def signout_user(request):
    logout(request)
    return redirect('index')


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=user),
        }

        return render(request, 'accounts/edit_profile.html', context)
    else:
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user profile')
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/edit_profile.html', context)


@login_required
def edit_phone(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'form': PhoneForm(instance=user.profile),
        }

        return render(request, 'accounts/edit_phone.html', context)
    else:
        form = PhoneForm(request.POST, instance=user.profile)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.user = user
            phone.id = user.profile.id
            phone.save()
            return redirect('user profile')
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/edit_phone.html', context)

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'GET':
        return render(request, 'accounts/delete_profile.html')
    else:
        user.delete()
        return redirect('index')


@login_required
def user_addresses(request):
    user = request.user
    context = {
        'addresses': user.profile.address_set.all,
    }
    return render(request, 'accounts/user_addresses.html', context)


@login_required
def create_address(request):
    if request.method == 'GET':
        form = AddressForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/create_address.html', context)
    else:
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.profile_id = request.user.profile.id
            address.is_default = False
            address.save()
            return redirect('user addresses')
        context = {
            'form': form,
        }
        return render(request, 'accounts/create_address.html', context)


@login_required
def edit_address(request, pk):
    address = Address.objects.get(pk=pk)
    if request.method == 'GET':
        form = AddressForm(instance=address)
        context = {
            'form': form,
            'address': address,
        }
        return render(request, 'accounts/edit_address.html', context)
    else:
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.profile = request.user.profile
            address.is_default = False
            address.save()
            return redirect('user addresses')
        context = {
            'form': form,
            'address': address,
        }
        return render(request, 'accounts/edit_address.html', context)


@login_required
def delete_address(request, pk):
    address = Address.objects.get(pk=pk)
    form = AddressForm(instance=address)

    for _, field in form.fields.items():
        field.widget.attrs['disabled'] = True

    if request.method == 'GET':
        context = {
            'form': form,
            'address': address,
        }
        return render(request, 'accounts/delete_address.html', context)
    else:
        address.delete()
        return redirect('user addresses')

@login_required
def user_favorites(request):
    favorites = request.user.profile.favorite_set.filter(user_id=request.user.profile.id)
    items = [Item.objects.get(pk=f.item_id) for f in favorites]
    context = {
        'items': items,
    }
    return render(request, 'accounts/user_favorites.html', context)
