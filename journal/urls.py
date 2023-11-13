from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name="journals"),
    path('journal/new/', views.post_journal, name='post_journal'),
    path("<int:id>",views.journalDetails,name="journal_details"),
    path("accessJournalItems",views.accessJournalDetails,name="accessJournalDetails"),
    path("editJournal/<int:id>",views.editJournal,name="editJournal"),
    path("streamAIResponse",views.streamAIResponse,name="streamAIResponse")
]
