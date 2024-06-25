from django.shortcuts import render


# Create your views here.
def Login(request):
    return render(request, 'paginas/Login.html')

def Nosotros(request):
    return render(request, 'paginas/Nosotros.html')
