from django.shortcuts import render
from django.http import HttpResponse
from .models import Spider

def crawlerView(request):
    spider = Spider()
    print(spider.clusters())
    return render(request, "crawler.html", { 'cluster': spider.clusters })
