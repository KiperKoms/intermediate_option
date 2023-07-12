from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete, PostCategoryView  # импортируем наше представление
from .views import upgrade_me
from .views import subscribe_to_category, unsubscribe_from_category

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', PostEdit.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('category/<int:pk>', PostCategoryView.as_view(), name= 'category'),
    path('subscribe/<int:pk>', subscribe_to_category, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe_from_category, name='unsubscribe'),

]