from django import forms
from price.models import *


class PriceForm(forms.ModelForm):

    class Meta:

        model = Device
        # fields = ('device_customer', 'brand', 'br_model', 'serial_num', 'total_count')
        exclude = [""]

class TypeOfWorkForm(forms.ModelForm):

    class Meta:

        model = TypeOfWork
        # fields = ('device_customer', 'brand', 'br_model', 'serial_num', 'total_count')
        exclude = [""]

class DeviceCategoryForm(forms.ModelForm):

    class Meta:

        model = DeviceCategory
        # fields = ('device_customer', 'brand', 'br_model', 'serial_num', 'total_count')
        exclude = [""]

class RelationsForm(forms.ModelForm):

    class Meta:

        model = Relations
        # fields = ('device_customer', 'brand', 'br_model', 'serial_num', 'total_count')
        exclude = [""]


