from django.shortcuts import render
from .models import Category, Firm, History
from django.views.generic import ListView, DetailView
# Create your views here.

class CategoryListView(ListView):
    template_name = 'categ.html'

    def get(self, request):
        category = Category.objects.all()
        return render(request, self.template_name, {'category':category})


class FirmListView(ListView):
    template_name = 'firm.html'

    def get(self, request, id):
        firm = Category.objects.filter(pk=id)
        return render(request, self.template_name, {'id':id, 'firm':firm})

class FirmDetailView(DetailView):
    template_name = 'firm_detail.html'

    def get(self, request, id):
        firma = Firm.objects.get(pk=id)
        return render(request, self.template_name, {'firma':firma})
