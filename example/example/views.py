from django.views.generic import TemplateView, DetailView
from django.contrib.flatpages.models import FlatPage


class TestView(TemplateView):
    template_name = 'example/test.html'


test = TestView.as_view()


class FlatpagesView(DetailView):
    queryset = FlatPage.objects.all()
    template_name = 'example/flatpage.html'


flatpage = FlatpagesView.as_view()
