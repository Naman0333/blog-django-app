from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import UpdatePostView


urlpatterns =[
    #urls for blogs
    path('',views.blogs,name='blogs'),
    path('blog/<str:slug>/',views.blogs_comments,name='blogs_comments'), 
    path('add_blogs',views.add_blogs,name='add_blogs'),
    path('edit_blog_post/<str:slug>/',UpdatePostView.as_view(),name='edit_blog_post'),
    path('delete_blog_post/<str:slug>/',views.delete_blog_post,name='delete_blog_post'),
    path('search',views.search,name='search'),
    
    # urls for profiles.
    path('user_profile',views.user_profile,name='user_profile'),
    path('search_profile',views.search_profile,name='search_profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),

    #urls for User authentication
    path('signUp',views.signUp,name='sigUp'),
    path('signIn',views.signIN,name='signIn'),
    path('signOut',views.signOut,name='signOut'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)