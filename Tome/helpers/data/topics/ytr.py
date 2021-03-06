from topics.models import Topic, YearTopicRank
from news.models import Corpus, Issue
from Tome.helpers.debug import Printer

progress = Printer(True)


def wipeYTRs():
    YearTopicRank.objects.all().delete()


def generateYTRs():
    dates = Issue.objects.dates("date_published", "year")
    corpus = Corpus.objects.all()[0]
    topics = Topic.objects.all().order_by('-score')

    progress.reset()

    ct = 0
    for t in topics:
        progress.log("{} / 100".format(ct))
        for date in dates:
            addYTR(date.year, t, corpus)
        ct += 1


def addYTR(y, t, c):
    ytr = YearTopicRank(year=y, topic=t, corpus=c)
    ytr.calculateScore()
    ytr.save()


def main():
    qRun()


def qRun():
    wipeYTRs()
    generateYTRs()


if __name__ == '__main__':
    main()
