from django.shortcuts import render
from django.views.generic import FormView


class IndexHomeView(FormView):
    template_name = ''
    # form_class = RequestDemoForm

def index_home_view(request):
    return render(request, 'home/index.html', {})