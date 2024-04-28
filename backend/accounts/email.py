
from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'accounts/mail_activation.html'


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'accounts/mail_confirmation.html'

 
class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'accounts/mail_password_reset.html'


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = 'accounts/mail_password_changed_confirmation.html'
