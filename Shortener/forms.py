from django import forms


HOSTS = (
        ('Tinyurl', 'Tinyurl'),
#        ('Isgd', 'Is.gd'),      # not recognized by pyshorteners, fix it
	('Bitly', 'Bit.ly'),
        ('Rebrandly', 'Rebrand.ly'),
        ('Madwire', 'm360.us'),
        ('Osdb', 'Osdb.link')
#        ('Soogd', 'Soo.gd')
    )

class Urlform(forms.Form):
    url = forms.CharField(initial='http://',required=True)
    host = forms.ChoiceField(choices=HOSTS)
