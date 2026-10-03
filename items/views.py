from django.shortcuts import render


def item_list(request):
    return render(request, 'items/item_list.html')