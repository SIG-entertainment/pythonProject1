from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django.core.mail import send_mail, EmailMultiAlternatives, mail_managers

#
# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label='Email')
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#         )


class CustomSignUpForm(SignupForm):

        # common_users = Group.objects.get(name='common users')
        # user.groups.add(common_users)

    def save(self, request):
        user = super().save(request)

        mail_managers(
            subject='New User!',
            message=f'User {user.username} just join the community!'
        )

        subject = 'Welcome to our newspaper!'
        text = f'{user.username}, your registration is success!'
        html = (
            f'<b>{user.username}</b>, yor registration is succsess on '
            f'<a href="http://127.0.0.1:8000/news">website<a/>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text,
            from_email=None,
            to=[user.email]
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()

        return user
