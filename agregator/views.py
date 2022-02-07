from django.shortcuts import render
from .forms import search
import subprocess
import re

def default_page(request):
    if request.method == 'GET':
        form = search()
    else:
        form = search(request.POST)
        if form.is_valid():
            info = request.POST['info']
            urls = parsing(info)
            return render(request, 'agregator/default_page.html', {
                    'info': info,
                    #'times': [0,1,2,3,4],
                    'urls': urls
                    #'urls2': ['дром запчасти', 'авито', 'аста', 'би-би', 'автозапчастирф']
                    })
    return render(request, 'agregator/default_page.html', {
    'form': form,
  })


def parsing(info):
    info = re.sub(r' ', '+', info)
    urldrom = 'https://baza.drom.ru/sankt-peterburg/sell_spare_parts/?query=%s' % info
    urlavito = 'https://www.avito.ru/rossiya/zapchasti_i_aksessuary/zapchasti-ASgBAgICAUQKJA?q=%s' % info
    urlasta = 'https://www.astaworld.ru/search?q=%s&type=name' % info
    urlbibi = 'https://bi-bi.ru/search/?text=%s' % info
    urlrf = 'https://xn----7sbaagc9ak4cmdvcfg1f.xn--p1ai/detail-fulltext.html?text=%s' % info
    urls = { 'дром запчасти':urldrom,
    'авито':urlavito,
    'аста':urlasta,
    'би-би':urlbibi,
    'автозапчасти-спб':urlrf }
    return urls
#def script_function(info):
#    print info #optional,check what the function received from the submit;
#    return subprocess.check_call(['/path/to/your/script.py', info])
