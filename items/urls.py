from django.urls import path
from .views import (
    ItemDetailView,
    SuccessView,
    CancelView,
    RetriveCheckoutSessionId
   )

urlpatterns = [
    path('item/<pk>/', ItemDetailView.as_view(), name='detail_view'),
    path('buy/<pk>/', RetriveCheckoutSessionId.as_view(), name='buy_page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='succes'),
]
