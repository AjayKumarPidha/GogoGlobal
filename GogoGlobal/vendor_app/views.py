from email import message
import email
from this import d
from unicodedata import category
from django.shortcuts import render
from django.views import View
from django.contrib.auth import update_session_auth_hash

# Create your views here.
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from django.views import View
from admin_dashboard.models import CustomUser
from admin_dashboard.views import userlogout
from .models import ProductModel, Manage_business
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.


class VendorHomePageViews(View):
    def get(self, request):

        if request.user.is_authenticated and request.user.is_vendor == True:

            return render(request, 'vendor/business-panel-dashboard.html')

        return redirect("vendorlogin")


class VendorUserProfile(View):
    def get(self, request):
        user = request.user.id
        print(user)
        return render(request, 'vendor/profile-details.html')


class AddProductViews(View):
    def get(self, request):
        return render(request, 'vendor/add_product.html')

    def post(self, request):
        data = ProductModel()

        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        quantity = request.POST.get('product_quantity')
        link = request.POST.get('product_link')
        category = request.POST.get('product_category')
        image = request.FILES['image']
        serial_number = request.POST.get('serial_number')
        descriptions = request.POST.get('product_descriptions')

        data.product_name = name
        data.product_price = price
        data.product_quantity = quantity
        data.product_link = link
        data.product_category = category
        data.product_image = image
        data.product_description = descriptions
        data.serial_number = serial_number
        data.vendor_id = request.user.id
        data.save()
        return redirect("productLists")


class ProductListsViews(View):
    def get(self, request, ):
        print(request.user.first_name)
        data = ProductModel.objects.filter(vendor_id=request.user.id)
        print(data)
        return render(request, 'vendor/product_lists.html', {'data': data})


class ProductDeleteViews(View):
    def get(self, request, id):
        data = ProductModel.objects.get(pk=id)
        data.delete()
        messages.success(request, '  Product Delete Successfully..!!')
        return redirect("productLists")


class EditProductViews(View):
    def get(self, request, id):
        data = ProductModel.objects.get(pk=id)
        return render(request, 'vendor/edit_product.html', {'data': data})

    def post(self, request, id):
        print(request.user.id)
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        quantity = request.POST.get('product_quantity')
        link = request.POST.get('product_link')
        category = request.POST.get('product_category')
        image = request.FILES.get('image')
        serial_number = request.POST.get('serial_number')

        descriptions = request.POST.get('product_descriptions')
        if image is not None:
            data = ProductModel(id=id, product_name=name, product_price=price, product_quantity=quantity,
                                product_link=link, product_category=category, product_image=image, serial_number=serial_number, product_description=descriptions)
            data.save()
            return redirect("productLists")
        else:
            data = ProductModel.objects.get(pk=id)
            data = ProductModel(id=id, product_name=name, product_price=price, product_quantity=quantity, product_link=link,
                                product_category=category, product_image=data.product_image, serial_number=serial_number, product_description=descriptions)
            data.save()
            return redirect("productLists")


####### Affiliate Register############
class Register(View):
    def get(self, request):
        return render(request, 'vendor/registration-form.html')

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

                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email_id=email_id, phone_number=phone_number, choose_profilepic=choose_profilepic,
                                                      password=password, gender=gender, address=address, Country=Country, state=state, city=city, Postal_zipcode=Postal_zipcode)

                user.save()
                print(user)
                messages.success(request, 'User Created Successfully..!!')
                return redirect('loginA')
        return render(request, 'vendor/registration-form.html')


# class SettingViews(View):
#     def get(self,request):
#         id=request.user.id
#         print(id)
#         data=CustomUser.objects.get(id=id)
#         user=CustomUser.objects.filter(data=data)
#         return render(request,'vendor/setting.html',{'user':user})

#     def post(self,request):


#         email_id = request.POST.get('email_id')

#         first_name=request.POST.get('first_name')
#         last_name= request.POST.get('last_name')
#         phone_number= request.POST.get('phone_number')
#         password= request.POST.get('password')
#         choose_profilepic= request.POST.get('choose_profilepic')


#         # choose_profilepic=request.POST.get('choose_profilepic')
#         gender=request.POST.get('gender')
#         address=request.POST.get('address')
#         Country=request.POST.get('Country')
#         state=request.POST.get('state')
#         city=request.POST.get('city')
#         Postal_zipcode=request.POST.get('Postal_zipcode')

#         data=CustomUser.objects.create_user(email_id=email_id, first_name=first_name, last_name=last_name, phone_number=phone_number, password=password ,choose_profilepic=choose_profilepic,gender=gender,Country=Country,address=address,state=state,city=city,Postal_zipcode=Postal_zipcode)
#         data.save()

#         messages.success(request,'new recorded add successfully')
#         data=CustomUser.objects.all()
#         return render(request,'vendor/setting.html',{'data':data})


class SettingViews(View):

    def get(self, request):
        return render(request, 'vendor/setting.html')

    def post(self, request):

        id = request.user.id

        email_id = request.POST.get('email_id')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')

        choose_profilepic = request.FILES.get('choose_profilepic')

        gender = request.POST.get('gender')
        address = request.POST.get('address')
        Country = request.POST.get('Country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        Postal_zipcode = request.POST.get('Postal_zipcode')

        if choose_profilepic is not None:
            user = CustomUser.objects.get(id=id)

            user.first_name = first_name
            user.last_name = last_name
            user.email_id = email_id
            user.phone_number = phone_number
            user.gender = gender
            user.address = address
            user.Country = Country
            user.city = city
            user.state = state
            user.choose_profilepic = choose_profilepic

            user.Postal_zipcode = Postal_zipcode
            user.save()
            print(choose_profilepic)
            return redirect('Settings')

        else:

            user = CustomUser.objects.get(id=id)

            user.first_name = first_name
            user.last_name = last_name
            user.email_id = email_id
            user.phone_number = phone_number
            user.gender = gender
            user.address = address
            user.Country = Country
            user.city = city
            user.state = state
            user.choose_profilepic = user.choose_profilepic
            user.Postal_zipcode = Postal_zipcode
            user.save()
            print(choose_profilepic)
            return redirect('Settings')


class Managebusiness(View):
    def get(self, request):
        return render(request, 'vendor/manage_business.html')

    def post(self, request):
        business_name = request.POST.get('business_name')
        business_email_id = request.POST.get('business_email_id')
        business_phoneno = request.POST.get('business_phoneno')
        business_paidtotal_earning = request.POST.get(
            'business_paidtotal_earning')
        business_unpaidtotal_earning = request.POST.get(
            'business_unpaidtotal_earning')
        unpaid_paid_referals = request.POST.get('unpaid_paid_referals')
        paid_total_referals = request.POST.get('paid_total_referals')
        data = Manage_business.objects.create(business_name=business_name, business_email_id=business_email_id, business_phoneno=business_phoneno, business_paidtotal_earning=business_paidtotal_earning,
                                              business_unpaidtotal_earning=business_unpaidtotal_earning, unpaid_paid_referals=unpaid_paid_referals, paid_total_referals=paid_total_referals)
        data.save()
        return render(request, 'vendor/manage_business_details.html', {'data': data})


class Managebusiness_details(View):
    def get(self, request):
        data = Manage_business.objects.all()

        return render(request, 'vendor/manage_business_details.html', {'data': data})


class Changepassword(View):
    def get(self, request):
        print("ram")

        return render(request, 'vendor/change_password.html')

    def post(self, request):

        old_password = request.POST.get("old_password")
        print(old_password)
        new_password = request.POST.get("new_password")
        print(new_password)
        confirmed_new_password = request.POST.get("confirm_password")
        print(confirmed_new_password)

        if old_password and new_password and confirmed_new_password:

            if request.user.is_authenticated:
                user = CustomUser.objects.get(email_id=request.user.email_id)
                print(user)
                print(request.user.email_id)

                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request, "your password has been changed successfuly.!")
                return redirect('Settings')

            else:
                print(" user is not authenticate ")

        else:

            messages.warning(request, " sorry , all fields are required !")
            return redirect('Settings')


class PrivacyPolicy(View):
    def get(self, request):
        return render(request, 'vendor/privacy-policy.html')

class TermsCoditionsViews(View):
    def get(self, request):
        return render(request, 'vendor/term-condition.html')    
    

def userlogout(request):

    logout(request)
    messages.success(request, 'Vendor Logged Out Successfully..!!')
    return redirect('vendorlogin')    



class Myaffiliate(View):
    def get(self,request):
        return render(request,'vendor/my-affiliate.html')



class Salesbyaffiliate(View):
    def get(self,request):
        return render(request,'vendor/sales_by_affiliate.html')
