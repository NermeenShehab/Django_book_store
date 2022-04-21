from django.urls import path
from .views import author_detail, authors, get_book, index,  upload,update_book,delete_book
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('author/', authors , name='authors'),
    path('author/<int:id>/', author_detail , name='author'),
     path('books/<int:id>' , get_book , name="book"),
    path('upload/',upload, name='upload-book'),
    path('update/<int:book_id>',update_book),
    path('delete/<int:book_id>',delete_book)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

