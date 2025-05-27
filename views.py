# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel, PropertyRegisterModel, BlockChainTransactionModel
from datetime import datetime
from .blkchain import Blockchain
import random

blockchain = Blockchain()


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def UserSaleLand(request):
    if request.method == 'POST':
        sellerName = request.POST.get('sellerName')
        sellerEmail = request.POST.get('sellerEmail')
        sellerMobile = request.POST.get('sellerMobile')
        sellerAadhar = request.POST.get('sellerAadhar')
        sellerPan = request.POST.get('sellerPan')
        sellerAddress = request.POST.get('sellerAddress')
        buyerName = request.POST.get('buyerName')
        buyerEmail = request.POST.get('buyerEmail')
        buyerMobile = request.POST.get('buyerMobile')
        buyerAadhar = request.POST.get('buyerAadhar')
        buyerPan = request.POST.get('buyerPan')
        buyerAddress = request.POST.get('buyerAddress')
        length = request.POST.get('length')
        width = request.POST.get('width')
        eastSide = request.POST.get('eastSide')
        westSide = request.POST.get('westSide')
        northSide = request.POST.get('northSide')
        southSide = request.POST.get('southSide')
        propertyAddress = request.POST.get('propertyAddress')
        status = "waiting"
        t1 = blockchain.new_transaction(sellerName, sellerAadhar, 1)
        proofId = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        blockchain.new_block(int(proofId))
        print("Genesis block: ", blockchain.chain)
        print("T1 is ", t1)
        currentTrnx = blockchain.chain[-1]
        previousTranx = blockchain.chain[-2]
        ### Current Tranasction Details
        c_transactions = currentTrnx.get('transactions')
        c_tnx_Dict = c_transactions[0]
        c_index = currentTrnx.get('index')
        c_timestamp = currentTrnx.get('timestamp')
        c_timestamp = datetime.fromtimestamp(c_timestamp)
        c_sender = c_tnx_Dict.get('sender')
        c_recipient = c_tnx_Dict.get('recipient')
        c_count = c_tnx_Dict.get('count')
        c_proof = currentTrnx.get('proof')
        c_previous_hash = currentTrnx.get('previous_hash')
        try:
            c_dict_rslt = {'c_index': c_index, 'c_timestamp': c_timestamp, 'c_sender': c_sender,
                           'c_recipient': c_recipient, 'c_count': c_count, 'c_proof': c_proof,
                           'c_previous_hash': c_previous_hash}

            # previous Transaction
            p_dict_rslt = {}
            p_transactions = previousTranx.get('transactions')

            if (len(p_transactions) != 0):
                p_tnx_Dict = p_transactions[0]

                p_index = previousTranx.get('index')
                p_timestamp = previousTranx.get('timestamp')
                p_timestamp = datetime.fromtimestamp(p_timestamp)
                p_sender = p_tnx_Dict.get('sender')
                p_recipient = p_tnx_Dict.get('recipient')
                p_count = p_tnx_Dict.get('count')
                p_proof = previousTranx.get('proof')
                p_previous_hash = previousTranx.get('previous_hash')
                PropertyRegisterModel.objects.create(
                    sellerName=sellerName, sellerEmail=sellerEmail, sellerMobile=sellerMobile,
                    sellerAadhar=sellerAadhar, sellerPan=sellerPan, sellerAddress=sellerAddress, buyerName=buyerName,
                    buyerEmail=buyerEmail, buyerMobile=buyerMobile, buyerAadhar=buyerAadhar, buyerPan=buyerPan,
                    buyerAddress=buyerAddress, length=length, width=width, eastSide=eastSide, westSide=westSide,
                    northSide=northSide, southSide=southSide, propertyAddress=propertyAddress, status=status
                )
                p_dict_rslt = {'p_index': p_index, 'p_timestamp': p_timestamp, 'p_sender': p_sender,
                               'p_recipient': p_recipient, 'p_count': p_count, 'p_proof': p_proof,
                               'p_previous_hash': p_previous_hash}
                BlockChainTransactionModel.objects.create(c_index=c_index, c_timestamp=c_timestamp, c_sender=c_sender,
                                                          c_recipient=c_recipient, c_count=c_count, c_proof=c_proof,
                                                          c_previous_hash=c_previous_hash, p_index=p_index,
                                                          p_timestamp=p_timestamp, p_sender=p_sender,
                                                          p_recipient=p_recipient, p_count=p_count, p_proof=p_proof,
                                                          p_previous_hash=p_previous_hash)
            else:
                PropertyRegisterModel.objects.create(
                    sellerName=sellerName, sellerEmail=sellerEmail, sellerMobile=sellerMobile,
                    sellerAadhar=sellerAadhar, sellerPan=sellerPan, sellerAddress=sellerAddress, buyerName=buyerName,
                    buyerEmail=buyerEmail, buyerMobile=buyerMobile, buyerAadhar=buyerAadhar, buyerPan=buyerPan,
                    buyerAddress=buyerAddress, length=length, width=width, eastSide=eastSide, westSide=westSide,
                    northSide=northSide, southSide=southSide, propertyAddress=propertyAddress, status=status
                )
                BlockChainTransactionModel.objects.create(c_index=c_index, c_timestamp=c_timestamp, c_sender=c_sender,
                                                          c_recipient=c_recipient, c_count=c_count, c_proof=c_proof,
                                                          c_previous_hash=c_previous_hash, p_index=None,
                                                          p_timestamp=None, p_sender=None,
                                                          p_recipient=None, p_count=None,
                                                          p_proof=None,
                                                          p_previous_hash=None)


        except Exception as ex:
            print(ex)
        return render(request, 'users/landSale.html', {'hash': c_previous_hash})

    else:
        return render(request, 'users/landSale.html', {})
