from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib import messages
from Accounts.models import Account
from .models import MyProfile
# Create your views here.

def userprofile(request):
    if request.method == 'GET':
        form = ProfileForm()
        return render(request,'userprofile.html',context = {'form':form})
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)

            data.user = request.user
            try:
                data.save()
                userinfo = MyProfile.objects.get(user_id=request.user.id)
                messages.success(request,'Your Profile is Set')
                return render(request,'userprofile/complete_userprofile.html',context={'userinfo':userinfo})
            except:
                pass
        else:
        	return render(request,'userprofile.html',context = {'form':form})

    return render(request,'userprofile.html',context={'form':form})


def completeuserprofile(request):

    userinfo = MyProfile.objects.get(user_id=request.user.id)
    return render(request,'userprofile/complete_userprofile.html',context={'userinfo':userinfo})