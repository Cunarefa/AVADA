from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admin_app.cinema.forms import CinemaAdminForm, CinemaFormset, CinemaFormsetHall
from movie_app.models import Cinema


class AdminCinemaListView(ListView):
    model = Cinema
    template_name = 'cinema/cinema_list.html'
    context_object_name = 'cinemas'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminCinemaListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Наши кинотеатров'
        return ctx


class CreateCinemaAdmin(CreateView):
    form_class = CinemaAdminForm
    template_name = 'cinema/create_cinema.html'
    success_url = reverse_lazy('cinemas')

    def get_context_data(self, **kwargs):
        ctx = super(CreateCinemaAdmin, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавить кинотеатр'
        if self.request.POST:
            ctx['form'] = CinemaAdminForm(self.request.POST, self.request.FILES)
            ctx['formset'] = CinemaFormset(self.request.POST, self.request.FILES)
        else:
            ctx['form'] = CinemaAdminForm()
            ctx['formset'] = CinemaFormset()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = None
        form = CinemaAdminForm(request.POST, request.FILES)
        formset = CinemaFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateCinemaAdmin(UpdateView):
    model = Cinema
    form_class = CinemaAdminForm
    template_name = 'cinema/cinema_update.html'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateCinemaAdmin, self).get_context_data(**kwargs)
        ctx['title'] = Cinema.objects.get(slug=self.kwargs['slug'])
        ctx['formset_hall'] = CinemaFormsetHall(instance=self.object)
        if self.request.POST:
            ctx['form'] = CinemaAdminForm(self.request.POST, self.request.FILES, instance=self.object)
            ctx['formset'] = CinemaFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            ctx['form'] = CinemaAdminForm(instance=self.object)
            ctx['formset'] = CinemaFormset(instance=self.object)
        return ctx

    def form_valid(self, request):
        form = CinemaAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = CinemaFormset(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cinema_delete = Cinema.objects.get(slug=self.kwargs['slug'])
            cinema_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('cinemas'))


class DeleteCinemaAdmin(DeleteView):
    model = Cinema
    success_url = reverse_lazy('cinemas')
