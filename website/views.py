from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class AboutPageView(TemplateView):
    template_name = "about.html"

def redirect_to_r(request):
    return HttpResponseRedirect('/r')