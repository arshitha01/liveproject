from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
from django.http import JsonResponse

# Create your views here.
def index(request):
	data=gallery_tb.objects.all()
	return render(request,'index.html',{'details':data})

def about(request):
	return render(request,'about.html')

def services(request):
	data=service.objects.all()
	return render(request,'services.html',{'sdata':data})

def usercontact(request):
	if request.method=="POST":
		cname=request.POST['text1']
		cphone=request.POST['text2']
		cemail=request.POST['text3']
		cmessage=request.POST['text4']

		# check=contact.objects.filter(useremail=cemail)
		# if check:
		# 	return render(request,'contact.html',{'error':'already registered'})
		# else:
		add=contact(username=cname,userphone=cphone,useremail=cemail,usermessage=cmessage)
		add.save()

		x = ''.join(random.choices(cname + string.digits, k=8))
		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
		subject = 'Welcome to Samridhi Ayurvedic Clinic'
		message = f'Hi {cname}, Thank you for valuable feeback.'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [cemail, ]
		send_mail( subject, message, email_from, recipient_list )
		asubject = 'Contact form '
		amessage = f' A message from  {cname}, message is {cmessage}, contact number is {cphone} '
		aemail_from = settings.EMAIL_HOST_USER
		arecipient_list = [settings.EMAIL_HOST_USER , ]
		send_mail( asubject, amessage, aemail_from, arecipient_list )
		return render(request,'index.html',{'success':'Data Saved'})
	else:
		return render(request,'contact.html',{"error":"message is not send"})

def getprice(request):
	if request.method=='POST':
		sid=request.GET['sid']
		cname=request.POST['text1']
		cemail=request.POST['text2']
		cphone=request.POST['text3']
		cmessage=request.POST['text4']
		servid=service.objects.get(id=sid)
		check=getprice_tb.objects.filter(useremail=cemail)
		if check:
			return render(request,'services.html',{'error':'already registered','data':sid})

		else:
			add=getprice_tb(sid=servid,username=cname,useremail=cemail,userphone=cphone,details=cmessage)
			add.save()

			x = ''.join(random.choices(cname + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'Welcome to Samridhi Ayurvedic Clinic'
			message = f'Hi {cname}, Thank you for valuable feeback.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [cemail, ]
			send_mail( subject, message, email_from, recipient_list )
			asubject = 'Get Price form '
			amessage = f' A message from  {cname}, message is {cmessage}, contact number is {cphone} '
			aemail_from = settings.EMAIL_HOST_USER
			arecipient_list = [settings.EMAIL_HOST_USER , ]
			send_mail( asubject, amessage, aemail_from, arecipient_list )
			return render(request,'index.html',{'success':'Data Saved'})
	else:
		return render(request,'services.html',{'data':sid})


########################....ADMIN....#######################################################

def admin_index(request):
	if request.session.has_key('myid'):
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/login.html')

def contactdisplay(request):
	if request.session.has_key('myid'):
		data=contact.objects.all()
		return render(request,'admin/contacttable.html',{'details':data})
	else:
		return render(request,'admin/login.html')

def admin_register(request):
	if request.method=='POST':
		name=request.POST['text1']
		email=request.POST['text2']
		phone=request.POST['text3']
		password=request.POST['text4']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=register.objects.filter(email=email)
		if check:
			return render(request,'admin/registration.html')
		else:
			admin=register(name=name,email=email,phone=phone,password=password)
			admin.save()
			subject = 'welcome to '
			message = f'Hi {name}, thank you for registering in . your user username: {email} and  password: {password}.'
			email_from = settings.EMAIL_HOST_USER 
			recipient_list = [email, ] 
			send_mail( subject, message, email_from, recipient_list ) 
			return render(request,'admin/login.html')
	else:
		return render(request,'admin/registration.html')

def admin_login(request):
	if request.method=='POST':
		email=request.POST['text1']
		password=request.POST['text2']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		
		check=register.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.name
				return render(request,'admin/index.html',{'success':'logged in'})
		else:
			return render(request,'admin/login.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'admin/login.html')

def admin_logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/admin_index/')
	else:
		return redirect('/admin_login/')

def sform(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			sname=request.POST['text1']
			descript=request.POST['text2']
			image=request.FILES['text3']
			add=service(servicename=sname,description=descript,image=image)
			add.save()
			return render(request,'admin/index.html')
		else:
			return render(request,'admin/serviceform.html')
	else:
		return render(request,'admin/login.html')

def stable(request):
	if request.session.has_key('myid'):
		data=service.objects.all()
		return render(request,'admin/servicetable.html',{'details':data})
	else:
		return render(request,'admin/login.html')


def stableupdate(request):
	if request.method=="POST":
		servicename=request.POST['text1']
		descript=request.POST['text2']
		cid=request.GET['sid']
		imgval=request.POST['imgup']
		if imgval == "Yes":

			cimage=request.FILES['images']
			oldrec=service.objects.filter(id=cid)
			updrec=service.objects.get(id=cid)
			for x in oldrec:
				if x.image: 
					imgurl=x.image.url
					pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
					if os.path.exists(pathtoimage):
						os.remove(pathtoimage)
						print('successfully deleted')
			updrec.image=cimage
			updrec.save()        
		add=service.objects.filter(id=cid).update(servicename=servicename,description=descript)
		return HttpResponseRedirect('/stable/')
	else:
		cid=request.GET['sid']
		data=service.objects.filter(id=cid)
		return render(request,"admin/supdate.html",{'details':data})

def stabledelete(request):
	sid=request.GET['sid']
	tdata=service.objects.filter(id=sid).delete()
	return redirect('/stable/')

def gform(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			image=request.FILES['text1']
			caption=request.POST['text2']
			add=gallery_tb(image=image,caption=caption)
			add.save()
			return render(request,'admin/index.html')
		else:
			return render(request,'admin/gform.html')
	else:
		return render(request,'admin/login.html')


def gtable(request):
	if request.session.has_key('myid'):
		data=gallery_tb.objects.all()
		return render(request,'admin/gtable.html',{'details':data})
	else:
		return render(request,'admin/login.html')

def gtableupdate(request):
	if request.method=='POST':
		caption=request.POST['text2']
		cid=request.GET['gid']
		imgval=request.POST['imgup']
		if imgval == "Yes":

			cimage=request.FILES['images']
			oldrec=gallery_tb.objects.filter(id=cid)
			updrec=gallery_tb.objects.get(id=cid)
			for x in oldrec:
				if x.image: 
					imgurl=x.image.url
					pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
					if os.path.exists(pathtoimage):
						os.remove(pathtoimage)
						print('successfully deleted')
		updrec.image=cimage
		updrec.save()        
		add=gallery_tb.objects.filter(id=cid).update(caption=caption)
		return HttpResponseRedirect('/gtable/')
	else:
		cid=request.GET['gid']
		data=gallery_tb.objects.filter(id=cid)
		return render(request,'admin/gupdate.html',{'newdata':data})

def gtabledelete(request):
	gid=request.GET['gid']
	data=gallery_tb.objects.filter(id=gid).delete()
	return redirect('/gtable/')

def gettable(request):
	if request.session.has_key('myid'):
		data=getprice_tb.objects.all()
		return render(request,'admin/gettable.html',{'details':data})
	else:
		return render(request,'admin/login.html')


