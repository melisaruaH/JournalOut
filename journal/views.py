from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import JournalForm
# Create your views here.
from .models import Journal
import journalout.ai as ai
from django.http import StreamingHttpResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def index(request):
    journals = Journal.objects.filter(user_id=request.user.id) # get all the journals from the database
    context = {'journals': journals} # create a context dictionary to pass the journals to the template
    return render(request, 'journals.html', context)

@login_required
def post_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('journal_details', journal.id)
    else:
        form = JournalForm()
    return render(request, 'post_journal.html', {'form': form})

@login_required
def journalDetails(request,id):

    journal = Journal.objects.get(id=id,user=request.user) 
    journalForm = JournalForm(instance=journal)
    return render(request,"journalDetails.html",{"journal":journalForm,"id":id})



@login_required
def accessJournalDetails(request):
    if request.method == "POST":
        print(request.POST)
        id = request.POST["journal_id"]
        journal = Journal.objects.get(id=id,user=request.user) 
        if request.POST["journal_password"] == journal.password:
            return redirect("journal_details",journal.id)
    return redirect("journals")

@login_required
def editJournal(request,id):

    journal = Journal.objects.get(id=id,user=request.user)

    if request.method == "POST":
        newForm = JournalForm(request.POST)

        journal.title = newForm.data["title"]
        journal.body = newForm.data["body"]
        journal.password = newForm.data["password"]

        journal.save()


    return redirect("journal_details",id)


@login_required
@csrf_exempt
def streamAIResponse(request):


    if request.method == "POST":

        data = json.loads(request.body.decode("utf-8"))["content"]
        
        response = StreamingHttpResponse(ai.assistUser(data)() ,content_type="text/event-stream")
        response['X-Accel-Buffering'] = 'no'  # Disable buffering in nginx
        response['Cache-Control'] = 'no-cache'  # Ensure clients don't cache the data
        return response  

        return HttpResponse("OK")
    

