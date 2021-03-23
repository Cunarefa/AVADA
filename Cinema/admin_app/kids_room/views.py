from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import VIPHall, VIPHallGallery


class AdminVipHallListView(ListView):
    model = VIPHall
    template_name = 'vip_hall/vip_halls_list.html'
    context_object_name = 'vip_halls'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminVipHallListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Vip-залы'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = VIPHallGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateVipHallAdmin(CreateWithInlinesView):
    model = VIPHall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать Vip-зал'}
    success_url = reverse_lazy('vip_halls_list')


class DetailVipHallAdmin(UpdateWithInlinesView):
    model = VIPHall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailVipHallAdmin, self).get_context_data(**kwargs)
        ctx['title'] = VIPHall.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cafe_delete = VIPHall.objects.get(pk=self.kwargs['pk'])
            cafe_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('vip_halls_list'))
