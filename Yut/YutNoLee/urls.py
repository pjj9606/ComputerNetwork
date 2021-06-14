from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking', views.ranking, name='ranking'),
    path('YutNoLee/ranking/register', views.register_ranking, name='register_ranking'),
    path('YutNoLee/ranking', views.get_ranking_list, name='get_ranking_list'),
    path('YutNoLee/check', views.check_YutNoLee, name='check_YutNoLee'),
    path('YutNoLee/make', views.make_YutNoLee, name='make_YutNoLee')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)