
from django.urls import path

from .views import (
    ListClientDetailView,
    ListClientView,

)

app_name = "campaign"

urlpatterns = [
    path('', ListClientView.as_view()),
    path('detail-list/<slug>', ListClientDetailView.as_view()),
    # path('empty-cart', EmptyCartView.as_view()),
    # path('synch', SynchCartView.as_view()),
]
