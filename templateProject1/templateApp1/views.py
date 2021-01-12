from django.shortcuts import render
def Employee_detail(request):
    Ename=input("enter the name:")
    Edesignation=input("enter the designation:")
    Eexp=float(input("enter the experience:"))
    Esalary=int(input("enter the slary:"))
    d={'name':Ename,'desig':Edesignation,'exp':Eexp,'salary':Esalary}
    return render(request,'templateApp1/1.html',d)
