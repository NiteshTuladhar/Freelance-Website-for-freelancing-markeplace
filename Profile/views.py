from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChangeProfilePicture
from django.contrib import messages
from Accounts.models import Account, Follow
from .models import MyProfile
from Gig.models import MyGig, Likes, Saves
from Order.models import MyOrder
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

@login_required
def myProfile(request,id):
    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    gigs = MyGig.objects.filter(user_id=request.user.id)

    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price

    context = {
        'userinfo' : userinfo,
        'gigs' : gigs,
        'id' : id,
        'acc' : acc,
        'available_for_withdrawal' : available_for_withdrawal,
    }
    return render(request,'userprofile/mygigpage.html',context)



def userProfile(request,id):

    acc = Account.objects.get(id=id)
    userinfo = MyProfile.objects.get(user_id=id)
    gig  = MyGig.objects.filter(user_id=id)
    is_alreadyfollowed = False
    try:
        is_follwed = Follow.objects.get(followed_to=id,followed_by=request.user.id)
        is_alreadyfollowed = True
        print('follow---------------------------------------------------------------')
    except:
        is_alreadyfollowed = False

    context ={
        'userinfo' : userinfo,
        'gig' : gig ,
        'is_alreadyfollowed' : is_alreadyfollowed,
        'acc' : acc,
    }
    return render(request,'userprofile/profile_visit.html',context=context)


def followUser(request,id):
    f = Follow(followed_to=id, followed_by=request.user.id)
    userinfo = Account.objects.get(id=id)
    try:
        f.save()

    except:
        pass

    ff = Follow.objects.filter(followed_to=id)

    print(userinfo.user_verified)

    if ff.count()>=2:
        userinfo.user_verified = True

    userinfo.save()

    print(userinfo.user_verified)


    return redirect('visitprofile',id)


def unfollowUser(request,id):
    f = Follow.objects.get(followed_to=id, followed_by=request.user.id)
    try:
        f.delete()
    except:
        pass
    return redirect('visitprofile',id)


@login_required
def liked_gigs(request):

    liked = Likes.objects.filter(user=request.user.id, value='Like')
    context = {
        'liked'  : liked,
    }

    return render(request,'gigs/liked_gigs.html',context)

@login_required
def saved_gigs(request):

    favourite = Saves.objects.filter(user=request.user.id)

    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
        
        

    context = {
        'favourite'  : favourite,
        'available_for_withdrawal' : available_for_withdrawal,
    }

    return render(request,'gigs/saved_gigs.html',context)

@login_required
def availability(request):

    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    gigs = MyGig.objects.filter(user_id=request.user.id)

    if acc.is_available == True:
        acc.is_available = False
        
    else:
        acc.is_available = True

    acc.save()
    context = {
        'userinfo' : userinfo,
        'gigs' : gigs,
        'id' : id,
        'acc' : acc
    }
    return render(request,'userprofile/mygigpage.html',context)



@login_required
def myOrders(request):
    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    orders = MyOrder.objects.filter(seller=request.user)

    total = orders.count()

    orders_inprogress = MyOrder.objects.filter(seller=request.user,status='In Progress')
    oip = orders_inprogress.count()

    orders_completed = MyOrder.objects.filter(seller=request.user,status='Complete')
    oc = orders_completed.count()

    orders_pending = MyOrder.objects.filter(seller=request.user,status='Pending')
    op = orders_pending.count()

    print('-----------------------------------')
    print(oip)
    print(oc)
    print(op)

    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    
    total_completed_order = completed_orders.count()
    
    if total == 0:
        total_completed = 1;
    else:
        total_completed = (total_completed_order/total)

    total_completed_percentage = (total_completed*100)



    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
        
        

    context = {
        'orders'  : orders,
        'acc' : acc,
        'userinfo' : userinfo,
        'total' : total,
        'oip' : oip,
        'oc':oc,
        'op' : op,
        'total_completed_percentage':total_completed_percentage,
        'available_for_withdrawal' : available_for_withdrawal,

    }
    #myorders = MyOrder.objects.filter(gig=gig.user.id)
    #print(myorder)
    #print('---------------------------------------------')
    return render(request,'userprofile/myorders.html',context)


@login_required
def myOrdersDetails(request,slug):


    orders = MyOrder.objects.get(slug=slug)

    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
        
        

    context = {
        'orders'  : orders,
        'available_for_withdrawal' : available_for_withdrawal,


    }

    return render(request,'userprofile/myordersdetails.html',context)


@login_required
def buyerOrders(request):
    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    orders = MyOrder.objects.filter(customer=request.user)

    total = orders.count

    orders_inprogress = MyOrder.objects.filter(customer=request.user,status='In Progress')
    oip = orders_inprogress.count()

    orders_completed = MyOrder.objects.filter(customer=request.user,status='Complete')
    oc = orders_completed.count()

    orders_pending = MyOrder.objects.filter(customer=request.user,status='Pending')
    op = orders_pending.count()

    print('-----------------------------------')
    print(oip)
    print(oc)
    print(op)

    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
        
        

    context = {
        'orders'  : orders,
        'acc' : acc,
        'userinfo' : userinfo,
        'total' : total,
        'oip' : oip,
        'oc':oc,
        'op' : op,
        'available_for_withdrawal' : available_for_withdrawal,

    }
    #myorders = MyOrder.objects.filter(gig=gig.user.id)
    #print(myorder)
    #print('---------------------------------------------')
    return render(request,'userprofile/buying_orders.html',context)



@login_required
def buyersOrdersDetails(request,slug):


    orders = MyOrder.objects.get(slug=slug)
    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    available_for_withdrawal = 0;
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
        
        
 

    context = {
        'orders'  : orders,
        'available_for_withdrawal' : available_for_withdrawal,


    }

    return render(request,'userprofile/buyers_orderdetailspage.html',context)



@login_required
def complete_order(request,slug):


    orders = MyOrder.objects.get(slug=slug)

    orders.status = 'Complete'
    
    orders.save()
    print('kdfjdkfjkdfjkdfjkdfjdkfjdkf')   
    messages.success(request,'Your Order Has Been Completed.')

    context = {
        'orders'  : orders,
        


    }

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cancel_order(request,slug):


    orders = MyOrder.objects.get(slug=slug)

    orders.status = 'Cancelled'
    
    orders.save()
    print('kdfjdkfjkdfjkdfjkdfjdkfjdkf')   
    messages.error(request,'Your Order Has Been Cancelled.')

    context = {
        'orders'  : orders,
        


    }

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required
# def myFollowFollowing(request):

#    following = Follow.objects.filter(followed_by=request.user.id)
#    followers = Follow.objects.filter(followed_to=request.user.id)

#    userinfo = MyProfile.objects.get(user_id=request.user.id)
#    context ={
#        'following' : following,
#        'followers' : followers,
#        'userinfo' : userinfo,
#    }

#    return render(request,'userprofile/follow_following.html',context)


@login_required
def userAnalytics(request):
    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)


    orders = MyOrder.objects.filter(seller=request.user)
    total = orders.count()



    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')
    total_completed_order = completed_orders.count()

    total_completed = (total_completed_order/total)
    total_completed_percentage = (total_completed*100)
    print(total_completed_percentage)
    print('oooooooooooooooooooooooo')

    available_for_withdrawal = 0;
    

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
    
    print (available_for_withdrawal)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    

    context = {
        'orders'  : orders,
        'acc' : acc,
        'userinfo' : userinfo,
        'total' : total,
        'total_completed_percentage' : total_completed_percentage,
        'available_for_withdrawal' : available_for_withdrawal,

    }

    return render(request,'userprofile/analytics.html',context)
    


@login_required
def userEarnings(request):
    acc = Account.objects.get(id=request.user.id)
    userinfo = MyProfile.objects.get(user_id=request.user.id)
    orders = MyOrder.objects.filter(seller=request.user)

    total_orders = MyOrder.objects.filter(seller=request.user)
    completed_orders = MyOrder.objects.filter(seller=request.user,status='Complete')

    total_earnings = 0;
    available_for_withdrawal = 0;

    for order in total_orders:
        
        total_earnings += order.gig.price

    print (total_earnings)
    print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

    for order in completed_orders:
        
        available_for_withdrawal += order.gig.price
    
    print (available_for_withdrawal)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    context = {
        'orders' : orders,
        'total_orders'  : total_orders,
        'completed_orders' : completed_orders,
        'acc' : acc,
        'userinfo' : userinfo,
        'total_earnings' : total_earnings,
        'available_for_withdrawal': available_for_withdrawal,

    }

    return render(request,'userprofile/earnings.html',context)