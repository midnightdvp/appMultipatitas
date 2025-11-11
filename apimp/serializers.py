from rest_framework import serializers
from core.models import Adress, Sale

class AdressSerializar(serializers.ModelSerializer):
    class Meta:
        model=Adress
        fields = ['idAdress','streetAdress','descAdress','postalCodeAdress','id']

class SaleSerializar(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields = ['idSale','saleDate','saleTotal','dispatchValue','id']

