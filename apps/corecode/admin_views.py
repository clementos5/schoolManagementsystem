# admin_views.py
from django.contrib import messages
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.vary import vary_on_headers
from django.views.generic import TemplateView, View
from .forms import CurrentSessionForm
from .models import AcademicSession, AcademicTerm

class CustomChangeList(ChangeList):
    def get_results(self, request):
        # Your custom logic here
        super().get_results(request)

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
@method_decorator(vary_on_headers('Cookie'), name='dispatch')
class CustomChangeListView(TemplateView):
    template_name = "admin/change_list.html"

    def get(self, request, *args, **kwargs):
        # Your custom logic here
        return super().get(request, *args, **kwargs)

# Other custom admin views go here...
