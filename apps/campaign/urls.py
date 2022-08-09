
from django.urls import path

from .views import (
    ListClientView,
)

app_name = "campaign"

urlpatterns = [
    path('', ListClientView.as_view()),
    # path('empty-cart', EmptyCartView.as_view()),
    # path('synch', SynchCartView.as_view()),
]
