from django.shortcuts import render
from .models import News

# Create your views here.
def news_list(request):

    query = request.GET.get("q")

    news = News.objects.all().order_by("-points")

    if query:
        news = news.filter(title__icontains=query)

    context = {
        "news": news
    }

    return render(
        request,
        "news_list.html",
        context
    )