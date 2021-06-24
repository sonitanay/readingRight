from django import forms

STATUS_CHOICE = (
    ("bought", "bought"),
    ("pending","pending"),
    ("not availiable", "not avaliable")
)

class AddItemForm(forms.Form):
    item_name = forms.CharField(max_length=120, label="Item Name", required=True)
    item_qty = forms.IntegerField(min_value=0, label="Item quantity", required=True)
    item_status = forms.ChoiceField(choices=STATUS_CHOICE,label="Item Status", required=True)