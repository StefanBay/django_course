from django.urls import path
from . import views

urlpatterns = [
    path('notes',views.NotesListView.as_view(),name = "notes.list"),
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name = "notes.detail"), #/<int:pk> displays the specific object id
    path('notes/new',views.NotesCreateView.as_view(),name = "notes.new"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(),name = "notes.update"), # to  edit a specific note
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(),name = "notes.delete") 
]