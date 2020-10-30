from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from .forms import GigForm
from django.contrib import messages
from Accounts.models import Account, Follow
from .models import MyGig, Review, Likes, Saves
from Profile.models import MyProfile
from django.views.generic import RedirectView
from django.http import JsonResponse

'''For generating thumnail'''



@login_required
def creategig(request):
    if request.method == 'GET':
        form = GigForm()
        return render(request,'gigs/gigform.html',context = {'form':form})
    else:
        profile = MyProfile.objects.get(user_id=request.user.id)
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user

            data.profile = profile #This saves the data of the form along with the current user profile.
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
    if request.method =='GET':
        gig  = MyGig.objects.get(slug=slug) #Here no data of profile and acc is retrieve because we used the foreign key in MyGig.
        id  = gig.user_id
        review = Review.objects.filter(gigs=gig, reply=None).order_by('-comment_time')
        reply = Review.objects.filter()
        total_likes = Likes.objects.filter(user=id)
        followers = Follow.objects.filter(followed_to=id)
        following = Follow.objects.filter(followed_by=id)

        

        context ={
            'gig' : gig,
            'review' : review,
            'id' : id,
            'reply' : reply,
            'total_likes' : total_likes,
            'followers' : followers,
            'following' : following,
           
        }
        if request.user.is_authenticated:
            return render(request,'gigs/gigdetails.html',context=context)
        else:
            return render(request,'gigs/othergigdetails.html',context=context)

    else:
        gig = MyGig.objects.get(slug=slug)
        message = request.POST.get('message')
        reply_id = request.POST.get('review_id')
        review_qs = None
        if reply_id:
            review_qs = Review.objects.get(id=reply_id)
        profile = MyProfile.objects.get(user_id=request.user.id)
        review = Review.objects.create(message=message, gigs=gig,user=request.user,reply=review_qs,profile=profile)
        try:
            review.save()
            messages.add_message(request, messages.SUCCESS, "Comment Added")
            return HttpResponseRedirect(request.path_info)
        except:
            messages.add_message(request, messages.SUCCESS, "Error")
            return HttpResponseRedirect(request.path_info)







def othersgigDetails(request,slug):

    gig  = MyGig.objects.get(slug=slug) 

    context ={
        'gig' : gig , 
    }
    

    return render(request,'gigs/othergigdetails.html',context=context)



def userProfile(request,id):

    userinfo = MyProfile.objects.get(user_id=id)
    gig  = MyGig.objects.filter(user_id=id)

    context ={
        'userinfo' : userinfo,
        'gig' : gig ,
    }
    return render(request,'userprofile/profile_visit.html',context=context)



def like_gig(request):
    likes = Likes.objects.all()
    user = request.user
    if request.method == 'POST':
        gig_id = request.POST.get('gig_id')
        gig_obj = MyGig.objects.get(id=gig_id)

        if user in gig_obj.liked.all():
            gig_obj.liked.remove(user)

        else:
            gig_obj.liked.add(user)

        like, created = Likes.objects.get_or_create(user=user,gigs_id=gig_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save() 

        
    return redirect('homepage')




def save_gig(request):

    user = request.user
    if request.method == 'POST':
        gig_id = request.POST.get('gig_id')
        gig_obj = MyGig.objects.get(id=gig_id)
        

        if user in gig_obj.favourite.all():
            gig_obj.favourite.remove(user)
            
            print(Saves.objects.get(user=user,gigs_id=gig_id))
            print('---------------------------')
            
            Saves.objects.get(user=user,gigs_id=gig_id).delete()
            Saves.save()
            
        else:
            gig_obj.favourite.add(user)

        saved, created = Saves.objects.get_or_create(user=user,gigs_id=gig_id)

        saved.save() 

        
    return redirect('homepage')