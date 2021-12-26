from .models import Book, Review
from .utils import average_rating
from django.shortcuts import render

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
    return render(request, "book_list.html", context)


