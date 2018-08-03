from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import GetBalance
from .forms import ActivateForm
from .models import SimCard
from .models import Offer

# Create your views here.
def index(request):
    return get_balance(request)
def is_admin(user):
    return user.groups.filter(name='webadmin').exists()
def is_guid(user):
    return user.groups.filter(name='guides').exists()

def get_balance(request):
    if request.method == "GET" and 'phone' in request.GET:
        form = GetBalance(request.GET)
        
        if form.is_valid():
            #post = form.save(commit=False)
            post = request.GET
            phone = post['phone']
            try:
                SCard = SimCard.objects.get(phone=phone)
            except:
                error=True
                return render(request, 'cell/get_balance.html', {'form': form,'error':error})
            form = GetBalance(request.GET, instance=SCard)
            aform = ActivateForm(request.POST, instance=SCard)
            alloffers = Offer.objects.all()
            
            stcoffers=[]
            mobilyoffers=[]
            zainoffers=[]
            for offer in alloffers:
                if offer.price <= SCard.current_balance:
                    offer.disabled=False
                else:
                    offer.disabled=True
                if offer.network=='STC':
                    stcoffers.append(offer)
                elif offer.network=='Mobily':
                    mobilyoffers.append(offer)
                elif offer.network=='Zain':
                    zainoffers.append(offer)
              
            length = max(len(stcoffers),len(mobilyoffers),len(zainoffers))  
            #post.published_date = timezone.now()
            #post.save()
            err=False
            if SCard.activated:
                err=True
            return render(request, 'cell/activate.html', {'err':err,'balance':SCard.current_balance,'stc':stcoffers,'mobily':mobilyoffers,'zain':zainoffers , 'phone':phone, 'length':length, 'form':form,'aform': aform})
            #return render(request, 'cell/activate.html', {'balance':SCard.current_balance,'myoffers':alloffers, 'phone':phone,'form':form,'aform': aform})
    elif request.method == "POST":

        form = ActivateForm(request.POST)
        if form.is_valid():
            sim = form.save(commit=False)
            #sim.phone = request.phone
            try:
                SCard = SimCard.objects.get(phone=sim.phone)
            except:
                pass

            SCard.offerid=sim.offerid
            SCard.activated=True
            SCard.time_activate=timezone.now()
            #offerprice = Offer.objects.get(offerid=sim.offerid)
            price=sim.offerid.price
            #SCard = SimCard.objects.get(phone=sim.phone)
            SCard.current_balance=SCard.current_balance-price

            SCard.save()
            return render(request,'cell/thanks.html')
    else:
        form = GetBalance()
        return render(request, 'cell/get_balance.html', {'form': form})

def activate(request):
    if request.method == "POST":
        form = ActivateForm(request.POST)
        if form.is_valid():
            sim = form.save(commit=False)
            #sim.phone = request.phone
            try:
                SCard = SimCard.objects.get(phone=sim.phone)
            except:
                pass

            SCard.offerid=request.soffer
            SCard.activated=True
            SCard.time_activate=timezone.now()
            price = Offer.objects.get(offerid=sim.offerid).price
            #SCard = SimCard.objects.get(phone=sim.phone)
            SCard.current_balance=SCard.current_balance-price

            SCard.save()
            return render(request,'cell/thanks.html')

    else:
        form = ActivateForm()
        return render(request, 'cell/activate.html', {'form': form})

def activate_done(request):
    return render(request, 'cell/thanks.html')

def showCells(request):
	return render(request, 'cell/fake.html',{'img':'cell/fakes/1.png'})
def enterGuid(request):
	return render(request, 'cell/fake.html',{'img':'cell/fakes/2.png'})

def recharge(request):
	return render(request, 'cell/fake.html',{'img':'cell/fakes/3.png'})
def guidsInfo(request):
	return render(request, 'cell/fake.html',{'img':'cell/fakes/4.png'})
def enterCell(request):
	return render(request, 'cell/fake.html',{'img':'cell/fakes/7.png'})