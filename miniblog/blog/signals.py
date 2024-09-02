from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('----------------------------')
    print('Logged in signal')
    # Take ip adddress from logged-in user
    ip = request.META.get('REMOTE_ADDR')
    print('Client IP: ', ip)

    # Store ip in session
    request.session['ip'] = ip
