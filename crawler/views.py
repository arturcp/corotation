from django.shortcuts import render
from django.http import HttpResponse
from .models import Spider, Catalog

def crawlerView(request):
    # import pdb; pdb.set_trace()

    # spider = Spider()
    catalog = Catalog.all()
    # return render(request, "crawler.html", { 'clusters': spider.clusters, 'catalog': catalog })
    return render(request, "crawler.html", { 'catalog': catalog })
