from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib import admin
from django.urls import path,include

router = DefaultRouter()
router.register(r'boutiques', BoutiqueViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'prix-produits', PrixProduitViewSet)
router.register(r'partenaires', PartenaireViewSet)
router.register(r'factures', FactureViewSet)
router.register(r'commandes-client', CommandeClientViewSet)
router.register(r'commandes-partenaire', CommandePartenaireViewSet)
router.register(r'versements', VersementViewSet)
router.register(r'historiques-stock', HistoriqueStockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]