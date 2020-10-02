from django.shortcuts import render
from .forms import ProfileForm
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
                print('a')
                data.save()
                messages.success(request,'Your Profile is Set')
                return redirect('dashboard')
            except:
                print('b')
                return render(request,'userprofile.html',context={'form':form})
        else:
        	return render(request,'userprofile.html',context = {'form':form})

    return render(request,'userprofile.html',context={'form':form})

