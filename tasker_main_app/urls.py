from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import ChecklistCreate

urlpatterns = [
  path('', views.home, name='welcome'),
  path('signup/', views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
  path('checklists/create/', views.ChecklistCreate.as_view(), name='checklist-create'),
  path('checklists/', views.checklist_index, name='checklist-index'),
  path('checklists/<int:checklist_id>/', views.checklist_detail, name='checklist-detail'),
  path('checklists/<int:pk>/update/', views.ChecklistUpdate.as_view(), name='checklist-update'),
  path('checklists/<int:pk>/delete/', views.ChecklistDelete.as_view(), name='checklist-delete'),
  path('checklists/<int:checklist_id>/add-task', views.add_task_to_checklist, name='add-task'),
  path('checklists/<int:checklist_id>/edit-task/<int:pk>/', views.ListitemUpdate.as_view(), name='edit-task'),
  path('checklists/<int:checklist_id>/delete-task/<int:pk>/', views.ListitemDelete.as_view(), name='delete-task'),
 ]