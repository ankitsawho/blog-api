from django.urls import path
from .views import post_list, post_detail, post_search, category_list

urlpatterns = [
    path('all-posts/', post_list),
    path('post/<str:pk>', post_detail),
    path('search/<str:query>', post_search),
    path('categories/', category_list),
]