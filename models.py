from django.db import models


# Create your models here.
class UserRegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.loginid

    class Meta:
        db_table = 'UserRegistrations'


class PropertyRegisterModel(models.Model):
    sellerName = models.CharField(max_length=100)
    sellerEmail = models.CharField(max_length=100)
    sellerMobile = models.CharField(max_length=100)
    sellerAadhar = models.CharField(max_length=100)
    sellerPan = models.CharField(max_length=100)
    sellerAddress = models.CharField(max_length=1000)
    buyerName = models.CharField(max_length=100)
    buyerEmail = models.CharField(max_length=100)
    buyerMobile = models.CharField(max_length=100)
    buyerAadhar = models.CharField(max_length=100)
    buyerPan = models.CharField(max_length=100)
    buyerAddress = models.CharField(max_length=1000)
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    eastSide = models.CharField(max_length=100)
    westSide = models.CharField(max_length=100)
    northSide = models.CharField(max_length=100)
    southSide = models.CharField(max_length=100)
    propertyAddress = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.sellerName

    class Meta:
        db_table = 'PropertyRegisterTable'


class BlockChainTransactionModel(models.Model):
    c_index = models.CharField(max_length=100)
    c_timestamp = models.CharField(max_length=100)
    c_sender = models.CharField(max_length=100)
    c_recipient = models.CharField(max_length=100)
    c_count = models.CharField(max_length=100)
    c_proof = models.CharField(max_length=100)
    c_previous_hash = models.CharField(max_length=100)
    p_index = models.CharField(max_length=100)
    p_timestamp = models.CharField(max_length=100)
    p_sender = models.CharField(max_length=100)
    p_recipient = models.CharField(max_length=100)
    p_count = models.CharField(max_length=100)
    p_proof = models.CharField(max_length=100)
    p_previous_hash = models.CharField(max_length=100)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "BlockChainTransactiontable"