from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def aluno_required(function=None, login_url=settings.LOGIN_URL, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Decorator que verifica se o usuário da sessão é ou não um aluno.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.eh_aluno,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def professor_required(function=None, login_url=settings.LOGIN_URL, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Decorator que verifica se o usuário da sessão é ou não um aluno.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.eh_professor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def empresa_required(function=None, login_url=settings.LOGIN_URL, redirect_field_name=REDIRECT_FIELD_NAME):
    '''
    Decorator que verifica se o usuário da sessão é ou não um aluno.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.eh_empresa,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator