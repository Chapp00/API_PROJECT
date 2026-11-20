
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Item
from .forms import ItemForm, ClaimForm


def home(request):
    return render(request, 'home.html')


def item_list(request):
    items = Item.objects.filter(
        status='ACTIVE'
    ).order_by('-created_at')

    return render(
        request,
        'items/item_list.html',
        {'items': items}
    )


@login_required
def report_item(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.reporter = request.user
            item.save()

            messages.success(
                request,
                'Your item has been reported successfully!'
            )

            return redirect('item_list')

    else:
        form = ItemForm()

    return render(
        request,
        'items/item_form.html',
        {'form': form}
    )


@login_required
def claim_item(request, item_id):

    item = get_object_or_404(
        Item,
        id=item_id,
        item_type='FOUND',
        status='ACTIVE'
    )

    if item.reporter == request.user:
        messages.error(
            request,
            "You cannot claim an item you reported."
        )
        return redirect('item_list')

    if request.method == 'POST':
        form = ClaimForm(request.POST)

        if form.is_valid():
            claim = form.save(commit=False)
            claim.item = item
            claim.claimant = request.user
            claim.save()

            messages.success(
                request,
                'Your claim has been submitted.'
            )

            return redirect('item_list')

    else:
        form = ClaimForm()

    return render(
        request,
        'items/claim_form.html',
        {
            'form': form,
            'item': item
        }
    )
