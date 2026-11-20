
from django import forms
from .models import Item, Claim


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item

        fields = [
            'name',
            'category',
            'description',
            'location',
            'date_occurred',
            'item_type',
            'image'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the item'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where was it lost or found?'
            }),

            'date_occurred': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'item_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim

        fields = ['explanation']

        widgets = {
            'explanation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': (
                    'Explain why you believe this item belongs to you.'
                )
            })
        }
