from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_view),
    path('reviews/<slug:review_slug>/', views.review_detail, name='review_detail'),
    path('add_review', views.review_add, name='review_add'),
    path('user_details', views.user_info, name='user_details'),
    path('delete/<int:pk>', views.delete_review, name='delete_review'),
]