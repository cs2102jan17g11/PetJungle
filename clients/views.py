from braces import views
from django.views.generic import TemplateView

from clients.models import Pet


class PetListView(views.LoginRequiredMixin,
                  TemplateView):
    template_name = 'petlist.html'
    model = Pet

    def get_context_data(self, **kwargs):
        ctx = super(PetListView, self).get_context_data(**kwargs)

        pets = Pet.objects.all()
        ctx.update({'pets': pets})
        print ctx
        return ctx
