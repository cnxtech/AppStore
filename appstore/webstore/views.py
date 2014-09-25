from django.views.generic import TemplateView

from appstoreitems.models import AppStoreItem


class ListView(TemplateView):
    template_name = "webstore/app-list.html"


class AppView(TemplateView):
    template_name = "webstore/app.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AppView, self).get_context_data(**kwargs)
        uuid = self.request.GET.get("id")
        context['app'] = AppStoreItem.objects.filter(uuid=uuid).get()
        return context