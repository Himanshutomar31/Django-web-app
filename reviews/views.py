from .models import Book, Review
from .utils import average_rating
from bookr.form import SearchForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([ review.rating for review in reviews])
            no_of_reviews = len(reviews)
        else:
            book_rating = None
            no_of_reviews = 0
        book_list.append({'book':book, 'book_rating':book_rating, 'no_of_reviews':no_of_reviews})

    context = {'book_list': book_list}
    return render(request, "reviews/book_list.html", context)


def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.review_set.all()
    context = {
        'book' : book,
        'reviews' : reviews,
    }
    return render(request, "reviews/book_details.html", context)


def index(request):
    return render(request, 'base.html')


def book_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            search_in = form.cleaned_data["search_in"]
            if search_in == "Title" or search_in =="":
                if search != "":
                    res = Book.objects.filter(title__icontains=search)
                else:
                    res = Book.objects.all()
            else:
                if search != "":
                    res = Book.objects.filter(Q(contributors__first_name=search)|Q(contributors__last_name=search))
                else:
                    res = Book.objects.all()
            context = {'book_list': res}
            return render(request, "search-results.html", context)

    form = SearchForm()
    context = {
        'form': form,
    }
    return render(request, "search-results.html", context)
