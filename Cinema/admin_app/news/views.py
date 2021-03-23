from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from admin_app.news.forms import NewsAdminForm
from movie_app.models import News, NewsGallery


class AdminNewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AdminNewsListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Новости'
        return ctx


class GalleryInline(InlineFormSetFactory):
    model = NewsGallery
    fields = ['image']
    factory_kwargs = {'max_num': 3}


class CreateNewsAdmin(CreateWithInlinesView):
    model = News
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/create_news.html'
    extra_context = {'title': 'Создать новость'}
    success_url = reverse_lazy('news')


class DetailNewsAdmin(UpdateWithInlinesView):
    model = News
    inlines = [GalleryInline]
    fields = '__all__'
    template_name = 'news/update_news.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs):
        ctx = super(DetailNewsAdmin, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

    def form_valid(self, request):
        form = NewsAdminForm(self.request.POST, self.request.FILES, instance=self.object)
        formset = GalleryInline(self.request.POST, self.request.FILES, instance=self.object)
        if 'Удалить' in self.request.POST:
            cinema_delete = News.objects.get(pk=self.kwargs['pk'])
            cinema_delete.delete()
        else:
            self.object = form.save()
            formset.instance = self.object
            self.object = request.save()
        return HttpResponseRedirect(reverse_lazy('news'))
