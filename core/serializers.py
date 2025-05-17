from rest_framework import serializers
from .models import *

class BoutiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boutique
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'boutique')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class PrixProduitSerializer(serializers.ModelSerializer):
    prix_vente_fcfa = serializers.FloatField(read_only=True)

    class Meta:
        model = PrixProduit
        fields = '__all__'

class PartenaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partenaire
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'

class CommandeClientSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    produit = ProduitSerializer(read_only=True)
    produit_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = CommandeClient
        fields = ['id', 'facture', 'nom', 'quantite', 'prenom','telephone', 'produit', 'produit_id','prix_unitaire_fcfa','total']
        extra_kwargs = {
            'produit': {'read_only': True}
        }
    
    def create(self, validated_data):
        produit_id = validated_data.pop('produit_id')
        produit = Produit.objects.get(id=produit_id)
        commande = CommandeClient.objects.create(produit=produit, **validated_data)
        return commande

class CommandePartenaireSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    produit = ProduitSerializer(read_only=True)
    produit_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CommandePartenaire
        fields = ['id', 'facture', 'partenaire', 'quantite', 'produit', 'produit_id','prix_unitaire_fcfa','total']
        extra_kwargs = {
            'produit': {'read_only': True}
        }
    def create(self, validated_data):
        produit_id = validated_data.pop('produit_id')
        produit = Produit.objects.get(id=produit_id)
        commande = CommandePartenaire.objects.create(produit=produit, **validated_data)
        return commande

class VersementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versement
        fields = '__all__'

class HistoriqueStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueStock
        fields = '__all__'