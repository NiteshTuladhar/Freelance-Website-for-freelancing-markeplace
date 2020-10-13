from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import GigForm
from django.contrib import messages
from Accounts.models import Account
from .models import MyGig
from Profile.models import MyProfile

# Create your views here.
@login_required
def creategig(request):
    if request.method == 'GET':
        form = GigForm()
        return render(request,'gigs/gigform.html',context = {'form':form})
    else:
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            userinfo = Account.objects.get(id=request.user.id)
            userinfo.first_gig = False
            try:
                data.save()
                userinfo.save()

                messages.success(request,'Your Gig Is Created.')
                return redirect('mygig')
            except:
                return render(request,'gigs/gigform.html',context = {'form':form}) 
        else:

            return render(request,'gigs/gigform.html',context = {'form':form})

    return render(request,'gigs/gigform.html',context={'form':form})


@login_required
def editGig(request,slug):

    giginfo = MyGig.objects.get(slug=slug)
    print(giginfo.time)
    if giginfo.user_id == request.user.id:
        form = GigForm(request.POST or None,request.FILES or None,instance=giginfo) #Her request.POST or None and req.Files or None is done so that the new data that we entered stays even when we refresh the page
    
        if form.is_valid():
            form.save();
            messages.success(request,"Your Gig Has Been Updated Successfully.")
            return redirect('mygig')
        context = {
            'form' : form,
        }
        return render(request,'gigs/editgig.html',context)
    else:
        return redirect('editgig')



def deleteGig(request,slug):

    gig = MyGig.objects.get(slug=slug)
    try:
        gig.delete()
        messages.success(request,'Your Gig Has Been Deleted.')
    except:
        mmessages.error(request,'Error Occurred')

    return redirect('mygig')
    


def gigDetails(request,slug):

    gig  = MyGig.objects.get(slug=slug)
    profile = MyProfile.objects.get(user_id=request.user.id)
    account = Account.objects.get(id=request.user.id)
    context ={
        'gig' : gig , 
        'profile' : profile,
        'account' : account
        
        
    }

    return render(request,'gigs/gigdetails.html',context=context)