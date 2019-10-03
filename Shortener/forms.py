from django import forms


HOSTS = (
	('Bitly', 'Bit.ly'),
	('Isgd', 'Is.gd'),
	('Madwire', 'm360.us'),
	('Osdb', 'Osdb.link'),
	('Rebrandly', 'Rebrand.ly'),
        )

class Urlform(forms.Form):
    url = forms.CharField(initial='http://',required=True)
    host = forms.ChoiceField(choices=HOSTS)
