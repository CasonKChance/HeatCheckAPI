from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.http import HttpResponse

# List users


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# User detail


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

# Create user


def user_create(request):
    if request.method == "POST":
        # Process form data
        # Note: This is a simplified example. In a real application,
        # you should use Django forms to validate data.
        user = User.objects.create(
            emailAddress=request.POST.get('email'),
            firstName=request.POST.get('firstName'),
            lastName=request.POST.get('lastName'),
            # Consider using set_password here
            password=request.POST.get('password'),
            # Set other fields as needed
        )
        return redirect('user_detail', pk=user.pk)
    return render(request, 'users/user_edit.html', {})

# Edit user


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # Similar to user_create, update the user instance with form data
        user.firstName = request.POST.get('firstName')
        user.lastName = request.POST.get('lastName')
        # Update other fields as needed
        user.save()
        return redirect('user_detail', pk=user.pk)
    return render(request, 'users/user_edit.html', {'user': user})

# Delete user


def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
