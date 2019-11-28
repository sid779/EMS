from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from .forms import VisitorForm,HostForm,HostloginForm,TimeForm
from ems.models import Host,Visitor
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
	return render(request, 'ems/home.html', {})

def checkin(request):
	if request.method == 'POST':
		form = VisitorForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			#query Host
			host = Host.objects.all().first()
			if not host:
				return redirect('host')
			obj.host = host.host_name
			obj.save()
			print("SAVE")	

			html_message = render_to_string('ems/mail_host.html', {'data':obj})
			plain_message = strip_tags(html_message)
			from_email = settings.EMAIL_HOST_USER
			to_email = obj.email
			send_mail(
			'Visitor details',
			plain_message,
			from_email,
			[to_email],
			fail_silently=False,
			html_message = html_message,
			)


					
			
			return redirect('lobby',pk=obj.pk)
		else:
			render(request, 'ems/checkin.html', {'form':form})
	else:
		form = VisitorForm()
		return render(request, 'ems/checkin.html', {'form':form})

def lobby(request,pk):
	if request.method == 'POST':
		form = TimeForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			cur_data = get_object_or_404(Visitor, pk=pk)
			cur_data.exit(obj.checkout)
			
			html_message = render_to_string('ems/mail_visitor.html', {'data':cur_data})
			plain_message = strip_tags(html_message)
			from_email = settings.EMAIL_HOST_USER
			to_email = cur_data.email
			send_mail(
			'Your visiting details',
			plain_message,
			from_email,
			[to_email],
			fail_silently=False,
			html_message = html_message,
			)		
			
			return redirect('home')
	else:
		data = get_object_or_404(Visitor, pk=pk)
		form = TimeForm()
		return render(request, 'ems/lobby.html', {'data':data, 'form':form})

def host(request):
	if request.method == 'POST':
		form = HostForm(request.POST)
		#query Host
		me  = Host.objects.all()
		print(not me)
		
		if not me and form.is_valid():
			obj = Host()
			obj.host_name = form.cleaned_data['host_name']
			obj.email = form.cleaned_data['email']
			obj.phone = form.cleaned_data['phone']
			obj.save()
			print("SAVE")
			return redirect('hostlogin')
		elif not me:
			return render(request, 'ems/host.html' , {'form':form})
		else:
			print ("AGAIN")
			return render(request, 'ems/host.html' , {'form':form})
		
	else:
		form = HostForm()
		return render(request, 'ems/host.html', {'form':form})

def hostlogin(request):
	if request.method == 'POST':
		form = HostloginForm(request.POST)
		
		
		if form.is_valid():
			name = form.cleaned_data['host_name']
			me = Host.objects.filter(host_name=name)
			if me:
				return redirect('host_manage')
			else:
				form = HostloginForm()
				return render(request, 'ems/host_login.html' , {'form':form})

		else:
			form = HostloginForm()
			return render(request, 'ems/host_login.html' , {'form':form})
	else:
		form = HostloginForm()
		return render(request, 'ems/host_login.html' , {'form':form})


def host_manage(request):
	#query visitor
	data = Visitor.objects.all()
	return render(request, 'ems/host_manage.html' , {'data':data})











