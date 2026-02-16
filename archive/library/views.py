from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection, Book
from django.contrib.auth.decorators import login_required

@login_required
def collection_list(request):

    collections = Collection.objects.filter(user=request.user)
    return render(request, 'library/users-home.html', {'collections': collections})


@login_required
def add_collection(request):
    if request.method == "POST":
        name = request.POST.get('name')
        wishlist = request.POST.get('wishlist') == 'on'
        Collection.objects.create(name=name, wishlist=wishlist, user=request.user)
        return redirect('collection_list')
    return render(request, 'library/users-home.html')


@login_required
def delete_collection(request, pk):
    collection = get_object_or_404(Collection, pk=pk, user=request.user)
    collection.delete()
    return redirect('collection_list')
