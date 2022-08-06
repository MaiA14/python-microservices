from django.urls import path
from .views import MovieViewSet, UserAPIView

urlpatterns = [
    path('movies/', MovieViewSet.as_view({
        'get': 'get',
        'post': 'add'
    })),
      path('movies/<str:pk>', MovieViewSet.as_view({
        'get': 'getById',
        'put': 'update',
        'delete': 'delete'
    })),
    path('user', UserAPIView.as_view())
]