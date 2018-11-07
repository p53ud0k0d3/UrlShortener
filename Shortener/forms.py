from django import forms


HOSTS = (
    ('Tinyurl', 'Tinyurl'),
    ('Isgd', 'Is.gd'),
    ('Bitly', 'Bit.ly'),
    ('Rebrandly', 'Rebrand.ly'),
    ('Madwire', 'm360.us'),
    ('Osdb', 'Osdb.link'),
    ('Qpsru', 'Qps.ru'),
    ('Dagd', 'Da.gd'),
    ('Clckru', 'Clck.ru'),
    ('Chilpit', 'Chilp.it'),
)

class Urlform(forms.Form):
    url = forms.CharField(initial='http://',required=True)
    host = forms.ChoiceField(choices=HOSTS)
