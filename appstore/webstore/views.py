from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = "webstore/app-list.html"


class AppView(TemplateView):
    template_name = "webstore/app.html"
