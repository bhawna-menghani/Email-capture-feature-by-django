import csv
from django.http import JsonResponse

def capture_email(email):
    with open('emails.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([email])

def landing_page(request):
    return render(request, 'index.html')

def capture_email_route(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            capture_email(email)
            return JsonResponse({'message': 'Email captured successfully!'})
        else:
            return JsonResponse({'message': 'Invalid request, email not provided.'}, status=400)
