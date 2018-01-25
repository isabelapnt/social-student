from django.core.exceptions import PermissionDenied
from core.rh.models import Usuario, Curso, Unidade
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from dashboard.forms import LoginForm, RegisterForm
from core.rh.forms import RecoverForm


def login_required_custom(function):
    def wrap(request, *args, **kwargs):
        if "email" in request.session or not request.user.is_anonymous:
            return function(request, *args, **kwargs)
        else:
            template = loader.get_template('registration/login.html')
            context = {
                'cursos': Curso.objects.all(),
                'unidades': Unidade.objects.all(),
                'form_login': LoginForm,
                'form_register': RegisterForm,
                'form_recover': RecoverForm
            }
            return HttpResponse(template.render(context, request))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap