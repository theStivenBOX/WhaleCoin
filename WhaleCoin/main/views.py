from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.
def index(request):
    user = request.user
    return render(request, 'main/index.html', {'user': user})

def friends(request):
    user = request.user
    referral_counts = {
        'level_1': user.count_referrals_at_level(1),
        'level_2': user.count_referrals_at_level(2),
        'level_3': user.count_referrals_at_level(3),
        'level_4': user.count_referrals_at_level(4),
        'level_5': user.count_referrals_at_level(5),
    }
    context = {'referral_counts': referral_counts}  

    return render(request, 'main/friends.html', context)

def earn(request):
    return render(request, 'main/earn.html')