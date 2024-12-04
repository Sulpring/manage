from django.shortcuts import render, get_object_or_404, redirect
from manage_main.models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_product/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        password = request.POST['password']
        User.objects.create(id=user_id, password=password)
        return redirect('user_list')
    return render(request, 'user_product/user_form.html')

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.id = request.POST['id']
        user.password = request.POST['password']
        user.save()
        return redirect('user_list')
    return render(request, 'user_product/user_form.html', {'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_product/user_confirm_delete.html', {'user': user})
