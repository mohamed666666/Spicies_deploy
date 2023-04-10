from django import forms

from .models import order

class OrderForm(forms.Form):
    fullname=forms.CharField(label="Enter Full Name",max_length=100)
    address=forms.CharField(label="Address ",max_length=100,help_text="Required")
    City=forms.CharField(label="City ",max_length=100,help_text="Required")
    Phone=forms.CharField(label="Phone Number",max_length=11)

    class Meta:
        model=order
        fields=["fullname","address","City","Phone"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Customer Name'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Address', 'name': 'Address', 'id': 'id_Address'})
        self.fields['City'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'City'})
        self.fields['Phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'EX: 01122335511'})