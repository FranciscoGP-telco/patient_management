from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Patient
from .forms import PatientForm, FetchForm

@csrf_exempt
def add(request):
    status = ''
    if request.method == 'POST':
        form = PatientForm(request.POST)
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')
        if password != confirm:
            status = 'Password doesn\'t match'
        else:
            if form.is_valid():
                form.save()
                status = 'Patiend added'
            else:
                status = 'Error adding users'
    else:
        form = PatientForm()
    context={
        'add_form': form,
        'status': status
    }
    template = loader.get_template('add.html')
    return HttpResponse(template.render(context))

@csrf_exempt
def fetch(request):
    form = FetchForm()
    patient = None
    error = ''
    if request.method == 'POST':
        try:
            patient = Patient.objects.get(id=request.POST.get('id'))
        except:
            error = 'Patient doesn\'t found'
    template = loader.get_template('fetch.html')
    context = {
      'fetch_form': form,
      'patient': patient,
      'error': error
    }
    return HttpResponse(template.render(context))