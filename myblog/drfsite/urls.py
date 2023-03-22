from django.urls import path, include
from article.views import articleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'article', articleViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('api/v1/article/', articleViewSet.as_view({'get': 'list'}), name='artAPI'),
    # path('api/v1/article/<int:pk>', articleViewSet.as_view({'put': 'update'}), name='artPKAPI')
]