from urllib import request
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from vendor_app.models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from affiliate_app.models import *
from admin_dashboard.models import *
from web_app.models import ContactEnquiryModels
# Create your views here.


class RegisterViwes(View):
    def get(self, request):
        # id=request.user.id

        return render(request, 'website/vendor-registration.html')

    def post(self, request):

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        con_password = request.POST['con_password']
        choose_profilepic = ""
        gender = ""
        address = ""
        state = ""
        city = ""
        Postal_zipcode = 000

        Country = ""

        if password == con_password:
            # filter the user email
            if CustomUser.objects.filter(email_id=email_id).exists():
                messages.error(
                    request, 'Email id  Already Exist...? Use Diffrent Email id to Create Account.')
            else:

                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email_id=email_id, phone_number=phone_number, password=password,
                                                      choose_profilepic=choose_profilepic, gender=gender, Country=Country, address=address,  state=state,  city=city, Postal_zipcode=Postal_zipcode)
                user.is_vendor = True
                user.save()

                messages.success(request, 'User Registration Successfully..!!')
                return redirect('vendorlogin')
        return render(request, 'website/vendor-registration.html')


class Login(View):
    def get(self, request):
        # data=request.user.get(id=id)

        return render(request, 'website/vendor-login.html')

    def post(self, request):
        email_id = request.POST['email_id']

        password = request.POST['password']

        # id=request.user.id
        # print(id)

        user = authenticate(email_id=email_id, password=password)
        if user is not None:

            if CustomUser.objects.filter(email_id=email_id, is_vendor=True):

                login(request, user)

                return redirect('vendordashboard')

            else:
                
                messages.success(request, ' Sorry Yor Are Not Vendor user!!')
                return render(request, 'website/vendor-login.html')
        else:
            messages.success(request, 'Invalid Email or password !!')

            return redirect('vendorlogin')


class AffiliateRegister(View):
    def get(self, request):
        return render(request, 'website/affiliate-register.html')

    def post(self, request):

        first_name = request.POST['first_name']

        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        con_password = request.POST['con_password']
        choose_profilepic = ""
        gender = ""
        address = ""
        Country = ""
        state = ""
        city = ""
        Postal_zipcode = 000

        if password == con_password:
            # filter the user email
            if CustomUser.objects.filter(email_id=email_id).exists():
                messages.error(
                    request, 'Email id  Already Exist...? Use Diffrent Email id to Create Account.')
            else:

                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email_id=email_id, phone_number=phone_number, password=password,
                                                      choose_profilepic=choose_profilepic, gender=gender, Country=Country, address=address,  state=state,  city=city, Postal_zipcode=Postal_zipcode)
                user.is_affiliator = True
                user.save()

                messages.success(request, 'User Registraions Successfully..!!')
                return redirect('affiliatelogin')
        return render(request, 'website/affiliate-register.html')


class AffiliateLogin(View):
    def get(self, request):

        return render(request, 'website/affiliate-login.html')

    def post(self, request):
        email_id = request.POST['email_id']

        password = request.POST['password']

        user = authenticate(email_id=email_id, password=password)

        if user is not None:
            if CustomUser.objects.filter(email_id=email_id, is_affiliator=True):

                login(request, user)

                return redirect('/')

            else:
                messages.success(
                    request, ' Sorry Yor Are Not Affiliater user!!')
                return render(request, 'website/affiliate-login.html')
        messages.success(
                    request, 'Invalid Email or Password ')
        return render(request, 'website/affiliate-login.html')


class WebHomePageViews(View):
    def get(self, request):
        data = ProductModel.objects.all()
        return render(request, 'website/index.html', {'data': data})


class ConatctPageViews(View):
    def get(self, request):
        return render(request, 'website/contact.html')

    def post(self, request):
        data = ContactEnquiryModels()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data.first_name = first_name
        data.last_name = last_name
        data.email_id = email
        data.phone_number = phone_number
        data.subject = subject
        data.message = message
        messages.success(request, 'User Contact Forms Submit Successfully..!!')

        data.save()

        return redirect('contact')


class Uselogout(View):
    def get(request, user):
        logout(user)
    
        return redirect('affiliatelogin')


class ProductDetailsViews(View):

    def get(self, request, id):

        product = ProductModel.objects.get(pk=id)
        return render(request, 'website/view-product-details.html', {'product': product})


class ProductListsPage(View):
    def get(self, request):
        data = ProductModel.objects.all()
        return render(request, 'website/product-lists.html', {'data': data})


class AboutsPageViews(View):
    def get(self, request):
        return render(request, 'website/abouts-page.html')


class PrivacyPolicyPageViews(View):
    def get(self, request):
        data = PrivacyPolicyModel.objects.all()
        return render(request, 'website/privacy_policy.html', {'data': data})


class TermsConditionsPageViews(View):
    def get(self, request):
        data = TermsConditionsModel.objects.all()
        return render(request, 'website/terms_conditions.html', {'data': data})


class ShareProductViews(View):
    def post(self, request, data):

        print(data)
        return HttpResponse("Product Add Successfully!")




class Affiliate_Forget_password(View):
    def get(self,request):
        return render(request,'website/affiliate-forget-password.html')

    def post(self,request):
        email_id=request.POST.get('email_id')
        print(email_id)
        new_password=request.POST.get('new_password')
        print(new_password)
        confirm_password=request.POST.get('confirm_password')
        print(confirm_password)
       

            
                
        if CustomUser.objects.filter(email_id=email_id).exists():
            
            if new_password == confirm_password:
                user = CustomUser.objects.get(email_id=email_id)
                print(user)
                user.set_password(new_password)
                user.save()
                print(user.set_password(new_password))
                return redirect('affiliatelogin')

            else:
                messages.success(request,"Password is not valid")
                
        else:
            messages.success(request,"Email Id is not valid")       
       


class Vendor_Forget_Password(View):
    def get(self,request):    
        return render(request,'website/vendor-forget-password.html')

    def post(self,request):
        email_id=request.POST.get('email_id')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        if CustomUser.objects.filter(email_id=email_id).exists():
            if new_password==confirm_password:
                user= CustomUser.objects.get(email_id=email_id)
                user.set_password(new_password)
                user.save()
                return redirect('vendorlogin')

            else:
                messages.success(request,'Password is not valid')

        else:

            messages.success(request,'email id and old password and new password is required')


