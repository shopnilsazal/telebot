from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegForm

# Create your views here.


class RegView(FormView):
    template_name = 'index.html'
    form_class = RegForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(RegView, self).form_valid(form)


def thanks(request):
    return render(request, 'thanks.html')

