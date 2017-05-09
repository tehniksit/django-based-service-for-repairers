
from .models import *
from django_select2.forms import *

class DeviceForm(forms.ModelForm):

    class Meta:

        model = Device
        fields = ('device_customer', 'brand', 'br_model', 'serial_num', 'total_count')
        exclude = [""]



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order

        exclude = [""]

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('operation_name', 'price')
        exclude = [""]

class RepaierForm(forms.ModelForm):
    class Meta:
        model = Repaier
        exclude = [""]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customerr

        fields = ('newcus_name', 'contact')
        exclude = [""]



class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name_part','part_number')
        exclude = [""]

class CategoryPartForm(forms.ModelForm):

    class Meta:
        model = PartCategory

        exclude = [""]