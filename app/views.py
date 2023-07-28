from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'Vruta','age':14}
    return render(request,'data_render.html',context=d)
def condition(request):
    d={'a':15,'b':100,'c':80}
    return render(request,'condition.html',context=d)



