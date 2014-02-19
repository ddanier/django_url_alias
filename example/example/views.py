from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'example/test.html'


test = TestView.as_view()
