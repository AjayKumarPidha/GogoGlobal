from django.urls import path
from.import views

urlpatterns=[
    
    path('admin-login/',views.login,name='admim-login'),
    path('admin-logout/', views.userlogout, name ='logouts'),
    path('', views.adminPanel, name='admin-dashboard'),
    path('add-privacy-policy', views.PrivacyPolicyPageViews.as_view(), name="privacy"),
    path('edit-privacy-policy/<int:id>', views.EditPrivacyPolicyViews.as_view(), name="EditPrivacy"),
    path('details-privacy-policy', views.DetailsPrivacyPolicyPageViews.as_view(), name="Detailprivacy_policy"),
    path('delete-privacy-policy/<int:id>', views.DeletePrivacyPolicyViews.as_view(), name="deletePrivacy"),
    
    path('add-terms-conditions', views.TermsConditionsPageViews.as_view(), name="termsConditions"),
    path('details-terms-conditions', views.DetailsTermsConditions.as_view(), name="DetailstermsConditions"),
    path('edit-terms-conditions/<int:id>', views.EditTermsConditions.as_view(), name="EdittermsConditions"),
    path('delete-terms-conditions/<int:id>', views.DeleteTermsConditionsViews.as_view(), name="DeletetermsConditions"),
    path('contact-details', views.ContactEnquiryViews.as_view(), name='contactInquary'),
    path('contact-user-details/<int:id>', views.ContactInquiryMoreDetailsViews.as_view(), name='moreDetails'),
    path('contact-Enquiry-delete/<int:id>', views.ContactInquiryDeleteViews.as_view(), name='conatctinquiryDelete'),
    
    path('vendor-business', views.Vendor_business.as_view(), name='Vendorbusiness'),
    path('affiliator-business', views.Affiliator_business.as_view(), name='Affiliatorbusiness'),
    path('Vendor_deletebusiness/<int:id>', views.Vendor_deletebusiness.as_view(), name='Vendordeletebusiness'),
    path('Affiliator_deletebusiness/<int:id>', views.Affiliator_deletebusiness.as_view(), name='Affiliatordeletebusiness'),
    path('Vendor-products-lists/<int:verdor_id>', views.VendorProductDetails.as_view(), name='vendorProducts'),
    path('admin-setting', views.Settings_View.as_view(), name='adminsetting'),
    path('admin-change-password', views.Change_password.as_view(), name='Adminchangepassword'),
    path('admin-forget-password', views.Forget_password.as_view(), name='adminforgetpassword'),
    
]
