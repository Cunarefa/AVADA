from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import ChildrenRoom, ChildrenRoomGallery


class AdminKidsRoomListView(ListView):
    model = ChildrenRoom
    template_name = 'kids_room/kids_rooms_list.html'
    context_object_name = 'kids_rooms'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminKidsRoomListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Детские комнаты'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = ChildrenRoomGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateKidsRoomAdmin(CreateWithInlinesView):
    model = ChildrenRoom
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать Детскую комнату'}
    success_url = reverse_lazy('kids_rooms_list')


class DetailKidsRoomAdmin(UpdateWithInlinesView):
    model = ChildrenRoom
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'

    def get_context_data(self, **kwargs):
        ctx = super(DetailKidsRoomAdmin, self).get_context_data(**kwargs)
        ctx['title'] = ChildrenRoom.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cafe_delete = ChildrenRoom.objects.get(pk=self.kwargs['pk'])
            cafe_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('kids_rooms_list'))
