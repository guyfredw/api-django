from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.post_views import Posts, PostDetail
from .views.comment_views import Comments, CommentDetail
from .views.post_unauthenticated_views import APosts

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('posts/', Posts.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('comments/', Comments.as_view(), name='comments'),
    path('comments/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
    path('all-posts/', APosts.as_view(), name='all_posts' )
]
