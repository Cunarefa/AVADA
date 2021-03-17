from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.hall.forms import HallForm, HallGalleryFormset
from movie_app.models import Hall, HallGallery


class GalleryInline(InlineFormSetFactory):
    model = HallGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateHallView(CreateWithInlinesView):
    model = Hall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'hall/hall_create.html'
    extra_context = {'title': 'Создать новый зал'}
    success_url = reverse_lazy('cinemas')

    def get_context_data(self, **kwargs):
        ctx = super(CreateHallView, self).get_context_data(**kwargs)
        ctx['title'] = 'Создать новый зал'
        return ctx


class UpdateHallView(UpdateWithInlinesView):
    model = Hall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'hall/hall_update.html'
    success_url = reverse_lazy('cinemas')

    def get_context_data(self, **kwargs):
        ctx = super(UpdateHallView, self).get_context_data(**kwargs)
        ctx['title'] = Hall.objects.get(pk=self.kwargs['pk'])
        return ctx


class DeleteHall(DeleteView):
    model = Hall
    template_name = 'admin_app/delete.html'
    success_url = reverse_lazy('cinemas')
