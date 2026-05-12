from django import forms
from .models import Review, ClientProfile, Movie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'text'] # поля, которые мы дадим заполнить юзеру
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
            'text': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;', 'rows': 4}),
            'rating': forms.Select(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
        }

class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="Имя")
    last_name = forms.CharField(max_length=100, label="Фамилия")
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'}) #  календарик
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # cписок полей, которые мы разрешим менять на сайте
        fields = ['title', 'description', 'data', 'duration', 'budget', 'country', 'genre', 'rating', 'poster', 'actors']
        # делаем поле даты удобным (выбор из календаря)
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'style': 'width: 100%; padding: 8px;'}),
        }