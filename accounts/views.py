from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from accounts.forms import RegisterForm, ProfileForm
from accounts.models import Profile


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
def delete_profile(request):
    user = request.user
    if request.method == 'GET':
        return render(request, 'accounts/delete_profile.html')
    else:
        user.delete()
        return redirect('index')