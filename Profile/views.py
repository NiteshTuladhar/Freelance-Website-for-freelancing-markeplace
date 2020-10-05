from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChangeProfilePicture
from django.contrib import messages
from Accounts.models import Account
from .models import MyProfile
# Create your views here.
@login_required
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


@login_required
def completeuserprofile(request):

    userinfo = MyProfile.objects.get(user_id=request.user.id)
    return render(request,'userprofile/complete_userprofile.html',context={'userinfo':userinfo})


@login_required
def changeprofilepic(request):
    user_id = request.user.id
    userinfo = MyProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        userinfo = MyProfile.objects.get(user_id=user_id)
        image = request.FILES.get('profile_image')
        print(userinfo.full_name)
        userinfo.profile_image = image
        userinfo.save()
        return redirect('compuserprofile')
    return render(request,'userprofile/change_profile_picture.html',context={'userinfo':userinfo})


@login_required
def editProfile(request):

    p = MyProfile.objects.get(user_id=request.user.id)
    form = ProfileForm(request.POST or None,request.FILES or None,instance=p) #Her request.POST or None and req.Files or None is done so that the new data that we entered stays even when we refresh the page
    
    if form.is_valid():
        form.save();
        messages.success(request,"Your Profile Has Been Updated Successfully.")
        return redirect('compuserprofile')
    context = {
        'form' : form,
        'p': p
    }
    return render(request,'userprofile/editprofile.html',context)


