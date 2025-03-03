from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scrape(request):
    page = requests.get('https://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    print(link_address)

    return render(request, 'myapp/result.html', {'link_adress': link_address})