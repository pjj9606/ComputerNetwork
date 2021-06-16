from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.index_tmp, name='index_tmp'),
    path('YutNoLee/make', views.make_YutNoLee, name='make_YutNoLee'),
    path('<str:room_name>/', views.room, name='room'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
