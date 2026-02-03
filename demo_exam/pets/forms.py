from django import forms
from .models import Service, Pet, Order, OrderService

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name', 'description', 'price', 'discount'
        ]
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(),
            'discount': forms.NumberInput()
        }
        
        
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name', 'type_of_pet', 'breed', 'weight', 'birth_date', 'owner'
        ]
        widgets = {
            'name': forms.TextInput(),
            'type_of_pet': forms.Select(),
            'breed': forms.Select(),
            'weight': forms.NumberInput(),
            'birth_date': forms.DateField(),
            'owner': forms.Select()
        }
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user', 'order_date', 'total_amount'
        ]
        widgets = {
            'user': forms.Select(),
            'order_date': forms.DateField(),
            
        }
        
class OrderServiceForm(forms.ModelForm):
    class Meta:
        model = OrderService
        fields = [
            'order', 'service', 'quantity', 'price'
        ]
        widgets = {
            'order': forms.Select(),
            'service': forms.Select(),
            'quantity': forms.NumberInput(),
            'price': forms.NumberInput()
        }