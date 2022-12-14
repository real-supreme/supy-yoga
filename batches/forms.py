from django import forms
from .models import Slots, Month
from users.models import ProfileModel


class BatchForm(forms.ModelForm):

    batch_slots = forms.ChoiceField(
        choices=Slots,
        required=True,
        widget=forms.Select(),
        label="Batch Slot for the Month",
    )
    batchmonth = forms.CharField(
        max_length=3,
        label="Month",
        initial="DEC",
        widget=forms.TextInput(
            attrs={"placeholder": "Month", "value": "DEC", "readonly": "readonly"}
        ),
    )  # To Implement automatic month selection
    batch_fee = forms.IntegerField(
        initial=500,
        widget=forms.TextInput(attrs={"placeholder": "Month", "readonly": "readonly"}),
    )

    class Meta:
        model = ProfileModel
        fields = ["batch_slots", "batchmonth", "batch_fee"]
