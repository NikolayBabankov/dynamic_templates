from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'


    list_inflation = []
    with open(settings.CSV_INF, newline='') as File:
        reader = csv.DictReader(File,delimiter = ';')
        for row in reader:
            tmp = {}
            for k,v in row.items():
                tmp.setdefault(k,v)
            list_inflation.append(tmp)
    
    # чтение csv-файла и заполнение контекста
    context = {'static': list_inflation}



    return render(request, template_name,
                  context)