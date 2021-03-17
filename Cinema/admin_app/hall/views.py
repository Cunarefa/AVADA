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


class UpdateHallView(UpdateWithInlinesView):
    model = Hall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'hall/hall_update.html'
    success_url = reverse_lazy('cinemas')


class DeleteHall(DeleteView):
    model = Hall
    template_name = 'admin_app/delete.html'
    success_url = reverse_lazy('cinemas')
