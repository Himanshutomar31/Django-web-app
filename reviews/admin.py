from django.contrib import admin
from reviews.models import Book, Publisher, Contributor, BookContributor, Review

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'publication_date', 'publisher')
    list_filter = ('publication_date', 'publisher', )
    date_hierarchy = ('publication_date')
    search_fields = ('title', 'isbn')


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)

