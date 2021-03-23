from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import CafeGallery, Cafe


class AdminCafeListView(ListView):
    model = Cafe
    template_name = 'cafe/cafe_list.html'
    context_object_name = 'cafe'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminCafeListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Кафе-бары'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = CafeGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateCafeAdmin(CreateWithInlinesView):
    model = Cafe
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать кафе-бар'}
    success_url = reverse_lazy('cafe_list')


class DetailCafeAdmin(UpdateWithInlinesView):
    model = Cafe
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailCafeAdmin, self).get_context_data(**kwargs)
        ctx['title'] = Cafe.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cafe_delete = Cafe.objects.get(pk=self.kwargs['pk'])
            cafe_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('cafe_list'))
