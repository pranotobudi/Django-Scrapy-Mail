from django.shortcuts import render, HttpResponseRedirect
from .forms import ScrapingProcessForm

# Create your views here.
def home_view(request):
    print("BISMILLAH")
    form = ScrapingProcessForm()
    return render(request, 'scraper/home.html',{'form':form})

def scraping_process(request):
    print("MASUKKK")
    if request.method == 'POST':
        print("MASUKKK POST")
        form = ScrapingProcessForm(request.POST, request.FILES)
        if form.is_valid():
            # Insert into DB
            # e.g. form.cleaned_data['custom_user']
            # e.g. form.cleaned_data['website_lists']
            if request.FILES.get('file_source', False):
                file_source = request.FILES['file_source']
                print(file_source)
                file_content = handle_uploaded_file(request.FILES['file_source'])
                init_mutable_value = request.POST._mutable
                request.POST._mutable = True
                request.POST['website_lists'] = file_content
                request.POST._mutable = init_mutable_value
            
            if request.POST.get('website_lists', False):
                #website list available, SCRAPE NOW
                website_lists = form.cleaned_data['website_lists']
                print(website_lists)
            
            # redirect to a new URL:
            form.save()
            return render(request, 'scraper/home.html',{'form':form})

    else:
        print('======================FORM NOT VALID======================')
            # GET, generate unbound (blank) form
        form = ScrapingProcessForm()
    return render(request,'scraper/home.html',{'form':form})

def handle_uploaded_file(f):
    result = ""
    with open('target_file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            result += chunk.decode("utf-8") 
            destination.write(chunk)
    return result