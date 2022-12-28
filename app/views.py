from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Главный шаблон для отображения списка меню"""
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
