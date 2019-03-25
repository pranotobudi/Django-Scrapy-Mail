from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'scraper/home.html')

def scraping_process(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('scraper/scraping_process.html')


    
    return render(request, 'scraper/home.html')
