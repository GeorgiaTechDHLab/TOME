import simplejson as json
from django.shortcuts import render
from news.models import Corpus, Article


# Create your views here.
def index(request):
    data = {}
    # get the corpus for later use
    corpus = Corpus.objects.all()[0]
    data["corpus"] = corpus

    # get the article counts by each year
    # arts = Article.objects.filter(issue__newspaper__corpus=data['corpus'])
    arts = Article.objects.all()
    counts = {}
    for i in range(corpus.date_started.year, corpus.date_ended.year + 1):
        c = arts.filter(issue__date_published__year=i).count()
        counts[i] = c
    data["article_count"] = json.dumps(counts)

    data["topics"] = data["corpus"].getTopicsByRank()
    data["topics_js"] = json.dumps(data["corpus"].getYearsTopics())
    return render(request, 'Tome/index.html', data)
