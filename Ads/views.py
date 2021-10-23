from .forms import ContactForm, NewItemForm
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import Category, Images, ItemName
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.db.models import Q
# Create your views here:


def About(request):
    return render(request, 'Adspages/about.html')


def HowTo(request):
    return render(request, 'Adspages/help.html')


class HomeItemList(ListView):
    model = ItemName
    template_name = 'Adspages/Home.html'
    ordering = '-add_date'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def FilterByCategory(request, pk):
    ads = ItemName.objects.filter(category=pk)
    category = Category.objects.all()
    context = {
        'pk': pk,
        'ads': ads,
        'category': category,
    }
    return render(request, 'Adspages/filter_by_category.html', context)


class FulldataView(TemplateView):
    template_name = 'Adspages/full_data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = ItemName.objects.get(pk=self.kwargs['pk'])
        return context


class AddImagesView(TemplateView):
    template_name = 'Adspages/add_images.html'

    def post(self, *args, **kwargs):
        try:
            images = self.request.FILES.getlist('images')
            itemname = ItemName.objects.get(pk=self.kwargs['pk'])
            for i in images:
                itemname_images = Images.objects.create(
                    itemname=itemname, images=i)
            return redirect('Ads:Home')
        except Exception as e:
            print(e)
            return HttpResponse('Ishlamadi')


class DeleteImg(DeleteView):
    model = Images
    success_url = '/personalAds/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ItemCreateView(CreateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'Adspages/add.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'Adspages/update_item.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False


class ItemDeleteView(DeleteView):
    model = ItemName
    success_url = '/personalAds/'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False


class OneUserAdsList(ListView):
    model = ItemName
    template_name = 'Adspages/oneUserAds.html'
    ordering = '-add_date'

    def get_queryset(self):
        return ItemName.objects.filter(creater=self.request.user).reverse()

#Ish-xizmatlari eloni qoshish:


class AdsCreateView(CreateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/add_servises.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class AdsUpdateView(UpdateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/update_servises.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False

# add ijara ads


class IjaraAdsCreateView(CreateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/add_ijara.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class IjaraAdsUpdateView(UpdateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/update_ijara.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False

# Adding education Ads


class EduAdsCreateView(CreateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/add_education.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class EduAdsUpdateView(UpdateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/update_edu.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False

# Adding IShlab chiqarish!


class ProductionCreateView(CreateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/add_production.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class ProductionUpdateView(UpdateView):
    model = ItemName
    form_class = NewItemForm
    template_name = 'otherPages/update_production.html'
    success_url = '/personalAds/'

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ads = self.get_object()
        if self.request.user == ads.creater:
            return True
        return False


# add contact section

def Contact_function(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Subject'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body['email'], [
                          settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Hato')
            return redirect('Ads:Contact')

    form = ContactForm
    return render(request, 'Adspages/contact.html', {"form": form})

# add search section


class SearchList(ListView):
    model = ItemName
    template_name = 'Adspages/search.html'
    ordering = '-add_date'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = ItemName.objects.filter(
            Q(name__icontains=query) | Q(region__icontains=query) | Q(
                campany_name__icontains=query) | Q(work_type__icontains=query)
            | Q(teaching_subject__icontains=query) | Q(
                center_or_teacher_name__icontains=query)
            | Q(narx__icontains=query) | Q(ijara_turi__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class FulldataUserView(TemplateView):
    template_name = 'Adspages/full_Data_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = ItemName.objects.get(pk=self.kwargs['pk'])
        return context
