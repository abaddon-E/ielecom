from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class Subscribe(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class FollowF(forms.Form):
    serial = forms.IntegerField(min_value=100000,max_value=999999,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))