from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChangeProfilePicture
from django.contrib import messages
from Accounts.models import Account
from .models import MyProfile
from Gig.models import MyGig
# Create your views here.


@login_required
def userprofile(request):
    profile = MyProfile.objects.get(user_id=request.user.id)
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request,'userprofile.html',context = {'form':form})
    else:

        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            data = form.save()
            userinfo = Account.objects.get(id=request.user.id)
            userinfo.is_profile_set = True
            try:
                data.save()
                userinfo.save()
                print(userinfo.is_profile_set)
                userinfo = MyProfile.objects.get(user_id=request.user.id)
                messages.success(request,'Your Profile is Set')
                return render(request,'userprofile/complete_userprofile.html',context={'userinfo':userinfo})
            except:
                pass
        else:
        	return render(request,'userprofile.html',context = {'form':form})

    return render(request,'userprofile.html',context={'form':form})




@login_required
def completeuserprofile(request,id):

    userinfo = MyProfile.objects.get(user_id=request.user.id)
    user_info = Account.objects.get(id=request.user.id)
    print(user_info.is_profile_set)
    return render(request,'userprofile/complete_userprofile.html',context={'userinfo':userinfo,'id':id})




@login_required
def changeprofilepic(request):
    user_id = request.user.id
    userinfo = MyProfile.objects.get(user_id=user_id)
    useracc = Account.objects.get(id=user_id)
    if request.method == 'POST':
        userinfo = MyProfile.objects.get(user_id=user_id)
        image = request.FILES.get('profile_image')
        print(userinfo.full_name)
        userinfo.profile_image = image
        userinfo.save()
        if useracc.first_gig :
            messages.success(request,message='Your Profile Image Has Been Changed.')
            return redirect('compuserprofile')
        else:
            messages.success(request,message='Your Profile Image Has Been Changed.')
            return redirect('mygig')
            
    return render(request,'userprofile/change_profile_picture.html',context={'userinfo':userinfo})




@login_required
def editProfile(request):

    userinfo = MyProfile.objects.get(user_id=request.user.id)
    form = ProfileForm(request.POST or None,request.FILES or None,instance=userinfo) #Her request.POST or None and req.Files or None is done so that the new data that we entered stays even when we refresh the page
    
    if form.is_valid():
        form.save();
        messages.success(request,"Your Profile Has Been Updated Successfully.")
        return redirect('mygig')
    context = {
        'form' : form,
        'userinfo': userinfo
    }
    return render(request,'userprofile/editprofile.html',context)


def myProfile(request,id):
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    gigs = MyGig.objects.filter(user_id=request.user.id)

    context = {
        'userinfo' : userinfo,
        'gigs' : gigs,
        'id' : id
    }
    return render(request,'userprofile/mygigpage.html',context)



def userProfile(request,id):

    userinfo = MyProfile.objects.get(user_id=id)
    gig  = MyGig.objects.filter(user_id=id)


    context ={
        'userinfo' : userinfo,
        'gig' : gig ,

    }
    return render(request,'userprofile/profile_visit.html',context=context)