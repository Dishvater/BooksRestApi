from rest_framework.routers import SimpleRouter

from .views import BooksViewSet, AuthorsViewSet, DbUpdateView

router = SimpleRouter()

router.register("books", BooksViewSet, basename="books")

urlpatterns = router.urls
