from django.utils.crypto import get_random_string


def generate_local_settings(file):
    """
    Generate local_settings file for deployment
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, chars)

    settings = (
        'SECRET_KEY = "{0}"'.format(secret_key),
        'DEBUG = False',
        'ALLOWED_HOSTS = ["idctest.pythonanywhere.com"]',
        'ADMINS = (("Pavel", "karateev.pavel@ya.ru"), )'
    )

    with open(file, 'w+') as local_settings:
        local_settings.write('"""\n Production settings\n"""\n\n')
        local_settings.write('\n'.join(settings) + '\n')
