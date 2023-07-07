from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact

def Index(request):
    return render(request,"index.html")
def submit(request):
    
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        message=request.POST['message']
        con=Contact(name=name,email=email,desc=message)
        con.save()
    return redirect('/')    
    

