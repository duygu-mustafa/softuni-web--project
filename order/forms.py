from django import forms

from accounts.models import Address
from order.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['address'].queryset = Address.objects.filter(
            profile_id=kwargs['initial']['profile_id'])
