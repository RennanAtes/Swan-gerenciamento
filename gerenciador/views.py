from django.shortcuts import render

# Create your views here.






def criarPagina(request):
    return render(request, 'create_page.html')