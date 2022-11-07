from django.shortcuts import redirect, render
from django.views import View
from admin_dashboard.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


class AffiliateHomePageViews(View):

    def get(self, request):

        if request.user.is_authenticated and request.user.is_affiliator == True:

            return render(request, 'affiliator/business-panel-dashboard.html')

        return redirect('affiliatelogin')


class DetailsMyAffiliater(View):
    def get(self, request):
        return render(request, 'affiliator/my_affiliater_details.html')


class SettingView(View):
    def get(self, request):
        return render(request, 'affiliator/setting.html')

    def post(self, request):
        id = request.user.id
        print(id)
        user = CustomUser.objects.get(id=id)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_id = request.POST.get('email_id')

        phone_number = request.POST.get('phone_number')

        choose_profilepic = request.POST['choose_profilepic']

        gender = request.POST.get('gender')
        address = request.POST.get('address')
        Country = request.POST.get('Country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        Postal_zipcode = request.POST.get('Postal_zipcode')
        user.first_name = first_name
        user.last_name = last_name
        user.email_id = email_id
        user.phone_number = phone_number
        user.choose_profilepic = choose_profilepic
        user.gender = gender
        user.address = address
        user.Country = Country
        user.state = state
        user.city = city
        user.Postal_zipcode = Postal_zipcode
        user.save()
        return redirect('affiliator-Setting')
class Change_password(View):

    def get(self, request):
        return render(request, 'affiliator/change-password.html')

    def post(self, request):

        old_password = request.POST.get('old_password')

        new_password = request.POST.get('new_password')

        confirm_password = request.POST.get('confirm_password')

        if old_password and new_password and confirm_password:
            if request.user.is_authenticated:
                user = CustomUser.objects.get(email_id=request.user.email_id)

                user.set_password(new_password)
                user.save()
                return redirect('affiliator-Setting')
            else:
                print("user is not authenticate")

        else:
            print("we required old_password and new_password and confirm_password fields")
            return redirect('affiliator-Setting')

class PrivacyPolicy(View):
    def get(self, request):
        return render(request, 'affiliator/privacy-policy.html')

class TermsCoditionsViews(View):
    def get(self, request):
        return render(request, 'affiliator/term-condition.html')    