from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet,  AuthorViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')
router.register(r'authors', AuthorViewSet, basename='user')
urlpatterns = router.urls
