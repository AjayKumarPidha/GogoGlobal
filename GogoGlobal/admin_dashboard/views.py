from django.shortcuts import render
from django.views import View
from .models import CustomUser, PrivacyPolicyModel, TermsConditionsModel
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from web_app.models import *
# Create your views here.
from vendor_app.models import ProductModel


class Businesspanel(View):
    def get(self, request):
        return render(request, 'admin/dashboard.html')

# =============LOGIN=============


def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        passwords = request.POST.get('password')
        print(email_id, passwords)
        user = authenticate(
            request=request, email_id=email_id, password=passwords)

        if user is not None:
            if CustomUser.objects.filter(email_id=email_id, is_superuser=True):
                dj_login(request, user)
                return redirect('admin-dashboard')
            else:
                messages.error(request, 'You Are Not Admin User')
        else:
            messages.error(request, 'Invalid Email or Password')

    return render(request, 'admin/login.html')

# =============LOGOUT=============


def userlogout(request):
    logout(request)
    messages.success(request, 'Admin Logged Out Successfully..!!')
    return redirect('admim-login')


@login_required(login_url='admim-login')
def adminPanel(request):

    if request.user.is_superuser == True:
        return render(request, 'admin/dashboard.html')
    else:
        return HttpResponseRedirect('/')


class PrivacyPolicyPageViews(View):
    def get(self, request):

        return render(request, 'admin/add-privacy-policy.html')

    def post(self, request):
        data = PrivacyPolicyModel()
        heading = request.POST.get('heading')
        description = request.POST.get('descriptions')

        data.heading = heading
        data.descriptions = description
        messages.success(request, 'New Recoard Add  Successfully..!!')

        data.save()
        return redirect('Detailprivacy_policy')


class DetailsPrivacyPolicyPageViews(View):
    def get(self, request):
        data = PrivacyPolicyModel.objects.all()
        return render(request, 'admin/privacy_details.html', {'data': data})


class DeletePrivacyPolicyViews(View):
    def get(self, request, id):
        data = PrivacyPolicyModel.objects.get(id=id)
        messages.success(request, ' Recoard Delete Successfully..!!')

        data.delete()
        return redirect('Detailprivacy_policy')


class EditPrivacyPolicyViews(View):
    def get(self, request, id):
        data = PrivacyPolicyModel.objects.get(id=id)
        return render(request, 'admin/edit-privacy-policy.html', {'data': data})

    def post(self, request, id):
        data = PrivacyPolicyModel()
        heading = request.POST.get('heading')
        description = request.POST.get('descriptions')
        data = PrivacyPolicyModel(
            id=id, heading=heading,  descriptions=description)

        messages.success(request, ' Recoard Updated Successfully..!!')

        data.save()
        return redirect('Detailprivacy_policy')


###################################################
class TermsConditionsPageViews(View):
    def get(self, request):
        return render(request, 'admin/add-terms_conditions.html')

    def post(self, request):
        data = TermsConditionsModel()
        heading = request.POST.get('heading')
        description = request.POST.get('descriptions')

        data.heading = heading
        data.descriptions = description
        messages.success(request, 'New Recoard Add  Successfully..!!')

        data.save()
        return redirect('DetailstermsConditions')


class DetailsTermsConditions(View):
    def get(self, request):
        data = TermsConditionsModel.objects.all()
        return render(request, 'admin/terms-details.html', {'data': data})


class DeleteTermsConditionsViews(View):
    def get(self, request, id):
        data = TermsConditionsModel.objects.get(id=id)
        messages.success(request, ' Recoard Delete Successfully..!!')

        data.delete()
        return redirect('Detailprivacy_policy')


class EditTermsConditions(View):
    def get(self, request, id):
        data = TermsConditionsModel.objects.get(id=id)
        return render(request, 'admin/edit-termsConditions.html', {'data': data})

    def post(self, request, id):
        data = TermsConditionsModel()
        heading = request.POST.get('heading')
        description = request.POST.get('descriptions')
        data = TermsConditionsModel(
            id=id, heading=heading, descriptions=description)

        messages.success(request, 'Recoard Updated  Successfully..!!')

        data.save()
        return redirect('DetailstermsConditions')


class ContactEnquiryViews(View):
    def get(self, request):
        data = ContactEnquiryModels.objects.all()
        return render(request, 'admin/contact-us.-details.html', {'data': data})


class ContactInquiryMoreDetailsViews(View):
    def get(self, request, id):
        data = ContactEnquiryModels.objects.get(id=id)
        return render(request, 'admin/contact-more-details.html', {'data': data})


class ContactInquiryDeleteViews(View):
    def get(self, request, id):
        data = ContactEnquiryModels.objects.get(id=id)
        data.delete()
        messages.success(
            request, 'User Contact Enquiry Delete  Successfully..!!')

        return redirect('contactInquary')


class Vendor_business(View):
    def get(self, request):
        data = CustomUser.objects.filter(is_vendor=True).exclude(
            is_affiliator=True).exclude(is_admin=True)
        return render(request, 'admin/manage-vendor.html', {'info': data})


class Affiliator_business(View):
    def get(self, request):
        data = CustomUser.objects.filter(is_affiliator=True)
        return render(request, 'admin/manage-affiliator.html', {'user': data})


class Vendor_deletebusiness(View):
    def get(self, request, id):
        data = CustomUser.objects.get(id=id)

        data.delete()
        return redirect('Vendorbusiness')


class Affiliator_deletebusiness(View):
    def get(self, request, id):
        data = CustomUser.objects.get(id=id)
        data.delete()
        return redirect('Affiliatorbusiness')


# class Vendor_productdetails(View):
#     def get(self, request, id):
#         id = request.user.id
#         print(id)

#         data = ProductModel.objects.exclude(id=id)
#         return render(request, 'admin/Vendor-product-details.html', {'info': data})


class VendorProductDetails(View):
    def get(self, request, verdor_id):
        data = ProductModel.objects.filter(vendor_id=verdor_id)
        print(data)
        return render(request, 'admin/vendor-products-details.html', {'data':data})

class Settings_View(View):
    def get(self,request):
        
        return render(request,'admin/setting.html')
        
     
    def post(self,request):
        id=request.user.id
        print(id)
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        
        email_id=request.POST.get('email_id')
        
        phone_number=request.POST.get('phone_number')
        
        
        choose_profilepic=request.FILES.get('choose_profilepic')

        if choose_profilepic is not None:

            user=CustomUser.objects.get(pk=id)
            print(user)
            user.first_name=first_name
            user.last_name=last_name
            user.email_id=email_id
            user.phone_number=phone_number

            user.choose_profilepic=choose_profilepic
            user.save()
            print(choose_profilepic)
            return redirect('adminsetting')

        else:

            user=CustomUser.objects.get(pk=id)
            print(user)
            user.first_name=first_name
            user.last_name=last_name
            user.email_id=email_id
            user.phone_number=phone_number

            user.choose_profilepic=user.choose_profilepic
            user.save()
            print(choose_profilepic)
            return redirect('adminsetting')



class Change_password(View):
    def get(self,request): 

        return render(request,'admin/change_password.html')

    def post(self,request):

        old_password  = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if old_password and new_password and confirm_password:
            if request.user.is_authenticated:
                new_password=confirm_password
                user=CustomUser.objects.get(email_id=request.user.email_id)
                user.set_password(new_password)
                user.save()
                return redirect('admim-login')
            else:
                messages.success(request,'New Password is not valid')

        else:
            messages.success(request,'old password and new password and confirm password is required')



class Forget_password(View):
    def get(self,request):
        return render(request,'admin/forget-password.html')
    
    def post(self,request):
        email_id=request.POST.get('email_id')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        if email_id and new_password and confirm_password:

            if CustomUser.objects.filter(email_id=email_id).exists():
                new_password=confirm_password
                user=CustomUser.objects.get(email_id=email_id)
                user.set_password(new_password)
                user.save()
                return redirect('admim-login')

            else:
                messages.success(request,'email id is not exist')


        else:

            messages.success(request,'Email_id and New_password and Confirm_password is required')

                

                
        



    










        
        

     