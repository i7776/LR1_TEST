from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'text'] # поля, которые мы дадим заполнить юзеру
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
            'text': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;', 'rows': 4}),
            'rating': forms.Select(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
        }