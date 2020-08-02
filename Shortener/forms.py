from django import forms

# formated in alphabetical order
HOSTS = (
        ('Bitly', 'Bit.ly'),
        ('Bitdo, Bit.do'),
        ('Google', 'Google URL Shortener'),
        ('Isgd', 'Is.gd'),
        ('Madwire', 'm360.us'),
        ('Osdb', 'Osdb.link ')
        ('Rebrandly', 'Rebrand.ly'),
        ('Tinyurl', 'Tinyurl'),
        )

class Urlform(forms.Form):
    url = forms.CharField(initial='http://',required=True)
    host = forms.ChoiceField(choices=HOSTS)
