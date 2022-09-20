from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class IndexView(TemplateView, LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
