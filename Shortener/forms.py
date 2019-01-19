from django import forms


HOSTS = (
    ('tinyurl', 'Tinyurl'),
    ('isgd', 'Is.gd'),
    ('Bitly', 'Bit.ly'),
    ('Google', 'Google URL Shortener'),
    ('Rebrandly', 'Rebrand.ly'),
    ('Madwire', 'm360.us'),
    ('osdb', 'Osdb.link	'),
    ('chilpit', 'chilp.it'),
    ('clckru', 'clck.ru'),
    ('dagd', 'da.gd'),
    ('qpsru', 'qps.ru'),
)


class Urlform(forms.Form):
    url = forms.CharField(initial='http://', required=True)
    host = forms.ChoiceField(choices=HOSTS)
