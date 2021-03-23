from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import ActionGallery, Action


class AdminActionListView(ListView):
    model = Action
    template_name = 'actions/actions_list.html'
    context_object_name = 'actions'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminActionListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Акции'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = ActionGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateActionAdmin(CreateWithInlinesView):
    model = Action
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать акцию'}
    success_url = reverse_lazy('actions')


class DetailActionAdmin(UpdateWithInlinesView):
    model = Action
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailActionAdmin, self).get_context_data(**kwargs)
        ctx['title'] = Action.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cinema_delete = Action.objects.get(pk=self.kwargs['pk'])
            cinema_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('actions'))
