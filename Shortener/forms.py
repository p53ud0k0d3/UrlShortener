from django import forms


HOSTS = (
        ('Tinyurl', 'Tinyurl'),
        ('Isgd', 'Is.gd'),
        )

class Urlform(forms.Form):
    url = forms.CharField(label="Url", max_length=200)
    host = forms.ChoiceField(choices=HOSTS)