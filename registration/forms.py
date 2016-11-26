from django import forms
from .tasks import send_reg_email_task, send_to_telegram_task


class RegForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=200)
    email = forms.EmailField(label='Your Email')
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        if self.cleaned_data['honeypot']:
            return False
        send_reg_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email']
        )
        send_to_telegram_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email']
        )
