from rest_framework.routers import SimpleRouter

from .views import BooksViewSet

router = SimpleRouter()

router.register("", BooksViewSet, basename="books")
# router.register("{bookid}", BooksViewSet, basename="booksbyid")

urlpatterns = router.urls
