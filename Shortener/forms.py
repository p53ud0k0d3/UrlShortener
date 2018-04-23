from django import forms


HOSTS = (
        ('Tinyurl', 'Tinyurl'),
        ('Isgd', 'Is.gd'),
		    ('Bitly', 'Bit.ly'),
        ('Google', 'Google URL Shortener'),
        ('Rebrandly', 'Rebrand.ly'),
        ('Madwire', 'm360.us'),
        ('Osdb', 'Osdb.link'),
        ('Dagd', 'DA.GD'),
        )

class Urlform(forms.Form):
    url = forms.CharField(initial='http://',required=True)
    host = forms.ChoiceField(choices=HOSTS)
