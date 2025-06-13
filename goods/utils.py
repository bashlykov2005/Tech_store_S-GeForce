from django.db.models import Q
#from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from goods.models import Products

# Поиск по Postgres
#def q_search(query):
    #if query.isdigit() and len(query) <= 5:
        #return Products.objects.filter(id=int(query))

    #vector = SearchVector("name", "description")
    #query = SearchQuery(query)

    #return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # Поиск по SQLite
    return Products.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
