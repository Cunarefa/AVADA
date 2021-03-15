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
    template_name = 'admin_app/hall_create.html'
    extra_context = {'title': 'Создать новый зал'}
    success_url = reverse_lazy('cinemas')

    def get_context_data(self, **kwargs):
        ctx = super(CreateHallView, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавить кинотеатр'
        if self.request.POST:
            ctx['form'] = HallForm(self.request.POST, self.request.FILES)
            ctx['formset'] = HallGalleryFormset(self.request.POST, self.request.FILES)
        else:
            ctx['form'] = HallForm()
            ctx['formset'] = HallGalleryFormset()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = None
        form = HallForm(request.POST, request.FILES)
        formset = HallGalleryFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateHallView(UpdateWithInlinesView):
    model = Hall
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'admin_app/hall_update.html'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateHallView, self).get_context_data(**kwargs)
        ctx['title'] = Hall.objects.get(pk=self.kwargs['pk'])
        if self.request.POST:
            ctx['form'] = HallForm(self.request.POST, self.request.FILES, instance=self.object)
            ctx['formset'] = HallGalleryFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            ctx['form'] = HallForm(instance=self.object)
            ctx['formset'] = HallGalleryFormset(instance=self.object)
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = HallForm(request.POST, request.FILES, instance=self.object)
        formset = HallGalleryFormset(request.POST, request.FILES, instance=self.object)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(reverse_lazy('cinemas'))


class DeleteHall(DeleteView):
    model = Hall
    template_name = 'admin_app/delete.html'
    success_url = reverse_lazy('cinemas')
