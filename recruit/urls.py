from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('recruit-1/', views.recruit_1, name='recruit-1'),
    path('recruit-2/', views.recruit_2, name='recruit-2'),
    path('recruit-quest/', views.recruit_quest, name='recruit_quest'),
    path('sith/', views.sith_choice, name='sith-choice'),
    path('sith/<slug>/', views.sith_page, name='sith-page'),
    path('shadow-hand/', views.shadow_hand, name='shadow-hand'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)