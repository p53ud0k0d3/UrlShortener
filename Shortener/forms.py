from django import forms


HOSTS = (
        ('Tinyurl', 'Tinyurl'),
        ('Isgd', 'Is.gd'),
		('Bitly', 'Bit.ly'),
        ('Google', 'Google URL Shortener'),
        ('Osdb', 'Osdb.link')
        )

class Urlform(forms.Form):
    url = forms.CharField(label="Url", max_length=200)
    host = forms.ChoiceField(choices=HOSTS)