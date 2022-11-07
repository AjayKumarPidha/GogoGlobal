from itertools import product
from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[
    path('',views.WebHomePageViews.as_view(), name='home'),
    path('contact-us', views.ConatctPageViews.as_view(), name="contact"),
    path('product-lists', views.ProductListsPage.as_view(), name="product"),
    path('about-us', views.AboutsPageViews.as_view(), name="aboutus"),
    path('terms-conditions', views.TermsConditionsPageViews.as_view(), name="termsCondition"),
    path('privacy-policy', views.PrivacyPolicyPageViews.as_view(), name="privacypage"),
    path('vendor-login/', views.Login.as_view(), name='vendorlogin'),
    
    path('vendor-register/', views.RegisterViwes.as_view(), name='register'),
    path('affiliate-register/', views.AffiliateRegister.as_view(), name='affiliateRegister'),
    path('affiliate-login/', views.AffiliateLogin.as_view(), name='affiliatelogin'),
    path('user-logout', views.Uselogout.as_view(), name="logout"),
    path('view-product/<int:id>', views.ProductDetailsViews.as_view(), name="prodictView"),
    path('add-share-product', views.ShareProductViews.as_view(), name="addShaereProduct"),
    path('affiliate-forgotpassword',views.Affiliate_Forget_password.as_view(), name='affiliateForgotpassword'),
    path('vendor-forgotpassword',views.Vendor_Forget_Password.as_view(), name='vendorForgotpassword')
   

]
