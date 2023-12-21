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
    "december": None,
}


def index(request):
    
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months" : months})


def monthly_challenge_by_number(request, month):
    # converts the keys from the monthly_challenges dictionary into a list (of months)
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    # /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        return HttpResponseNotFound("This month is not supported!")
