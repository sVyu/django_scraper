from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        try:
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')
        except BaseException as e:
            print('exception occured', e)
            return HttpResponseRedirect('/')

        # link_address = []
        # for link in soup.find_all('a'):
        #     link_address.append(link.get('href'))

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    # return render(request, 'myapp/result.html', {'link_adress': link_address})
    return render(request, 'myapp/result.html', {'data': data})

def clear(requests):
    Link.objects.all().delete()
    return render(requests, 'myapp/result.html')