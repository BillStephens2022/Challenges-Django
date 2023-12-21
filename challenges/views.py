from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Get 30 minutes of exercise every day!",
    "may": "Run at least 50 miles this month!",
    "june": "Learn Java for at least 20 minutes every day!",
    "july": "Read at least 3 books this month!",
    "august": "Drink no alcohol for the entire month!",
    "september": "Learn C# for at least 20 minutes every day!",
    "october": "Learn a new fact every day!",
    "november": "Eat no sweets/candy for the entire month!",
    "december": "Learn React Native for at least 20 minutes every day!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize();
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"""
    <div>
        <h1>Challenges Page</h1>
        <ul>
          {list_items}
        </ul>
    </div>
    """
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    # converts the keys from the monthly_challenges dictionary into a list (of months)
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
       
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month.capitalize()})
    except:
        return HttpResponseNotFound("This month is not supported!")
