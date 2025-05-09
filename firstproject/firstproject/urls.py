from django.contrib import admin
from django.urls import path
from secondapp import views
from secondapp.views import edit_data
from secondapp.views import edit
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertauthor/',views.insertauthor,name='insertauthor'),
    path('insertbook/',views.insertbook,name='insertbook'),
    path('author/',views.author,name='author'),
    path('edit_data/<int:id>/',edit_data, name='edit_data'),
    path('delete_data/<int:id>/',views.delete_data,name='delete_data'),
    path('book_aut/',views.book,name='book_aut'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('register_view/',views.register_view,name='register_view'),
    path('',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),


]
