from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import Create_Account_Form,CreateForm
from .models import Create_Business
from django.http import HttpResponse                     


# Create your views here.

def home(request):
    return render(request, 'home.html')

 
class Create_Account_View(CreateView):
    form_class = Create_Account_Form
    success_url = reverse_lazy('login')
    template_name = 'registration/create_account.html'

def account_type(request):
    return render(request,"account_type.html")


def select_business_step(request):
    return render(request, 'select_business_step.html')

def create_business(request):
	shelf = Create_Business.objects.all()
	return render(request, 'book/create_business.html', {'shelf': shelf})

def upload_business(request):
	upload = CreateForm()
	if request.method == 'POST':
		upload = CreateForm(request.POST)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'book/create_business_form.html', {'upload_form':upload})

def update_business(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Create_Business.objects.get(id = book_id)
	except Create_Business.DoesNotExist:
		return redirect('index')
	book_form = CreateForm(request.POST or None, instance = book_sel)
	if book_form.is_valid():
		book_form.save()
		return redirect('index')
	return render(request, 'book/create_business_form.html', {'upload_form':book_form})

def delete_business(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Create_Business.objects.get(id = book_id)
	except Create_Business.DoesNotExist:
		return redirect('index')
	book_sel.delete()
	return redirect('index')

