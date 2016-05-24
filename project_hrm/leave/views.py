from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from .forms import EmployeeForm
# Create your views here.
def home(request):
    # title='Employee login !'
    # #if request.user.is_authenticated():
    # #	title="Welcome %s" %(request.user)
    # #form2=EmployeeForm()
    # context={
    # "title": title,
    # #"form": form2
    # }
    
    return render(request,"home.html",{})
@login_required(login_url='/login/')    
def profile(request):
    return render(request,"profile.html",{})    