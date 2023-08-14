from django.shortcuts import render
from django.views.generic import FormView
from django.views import generic


class IndexHomeView(FormView):
    template_name = ''
    # form_class = RequestDemoForm

def index_home_view(request):
    return render(request, 'home/index.html', {})

class VueView(generic.TemplateView):
    template_name = 'vue/index.html'