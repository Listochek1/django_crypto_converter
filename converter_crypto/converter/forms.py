from django import forms

class MainForm(forms.Form):
    quantity = forms.FloatField()
    from_coin = forms.CharField()
    to_coin = forms.CharField()
    output = forms.FloatField()
