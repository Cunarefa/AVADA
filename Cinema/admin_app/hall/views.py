from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.hall.forms import HallForm
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

    def get_context_data(self, **kwargs):
        ctx = super(UpdateHallView, self).get_context_data(**kwargs)
        ctx['title'] = Hall.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = HallForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            hall_delete = Hall.objects.get(pk=self.kwargs['pk'])
            hall_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('cinemas'))


class DeleteHall(DeleteView):
    model = Hall
    template_name = 'admin_app/delete.html'
    success_url = reverse_lazy('cinemas')
