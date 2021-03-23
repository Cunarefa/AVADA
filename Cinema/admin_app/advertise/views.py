from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import Advertise, AdvertiseGallery


class AdminAdvertiseListView(ListView):
    model = Advertise
    template_name = 'advertise/advertise_list.html'
    context_object_name = 'advertise'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminAdvertiseListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Реклама'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = AdvertiseGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateAdvertiseAdmin(CreateWithInlinesView):
    model = Advertise
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать рекламу'}
    success_url = reverse_lazy('advertise_list')


class DetailAdvertiseAdmin(UpdateWithInlinesView):
    model = Advertise
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailAdvertiseAdmin, self).get_context_data(**kwargs)
        ctx['title'] = Advertise.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cafe_delete = Advertise.objects.get(pk=self.kwargs['pk'])
            cafe_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('advertise_list'))
