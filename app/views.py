from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")


def counter(request):
    words = request.POST["words"]
    # print(words)
    temp = words
    word_count = len(temp.split())

    return render(
        request,
        "counter.html",
        {
            "words": words,
            "word_count": word_count,
        },
    )
