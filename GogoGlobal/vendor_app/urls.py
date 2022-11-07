from django.urls import path
from .import views

urlpatterns=[


    path('',views.VendorHomePageViews.as_view(), name='vendordashboard'),
    path('user-profiles',views.VendorUserProfile.as_view(), name='vendorProfiles'),
    
    path('add-product', views.AddProductViews.as_view(), name="addProduct"),
    path('product-lists', views.ProductListsViews.as_view(), name='productLists'),
    path('product-delete/<int:id>', views.ProductDeleteViews.as_view(), name='productdelete'),
    path('edit-product/<int:id>', views.EditProductViews.as_view(), name='productEdit'),
    path('setting', views.SettingViews.as_view(), name='Settings'),
    path('manage-business',views.Managebusiness.as_view(), name='manage-business'),
    path('manage-business-details',views.Managebusiness_details.as_view(), name='Managebusiness_details'),
    path('change_password',views.Changepassword.as_view(), name='Changepassword'),
    path("privacy-policy", views.PrivacyPolicy.as_view(), name="privacyPolicy"),
    path("terms-coditions", views.TermsCoditionsViews.as_view(), name="termCoditions"),
    path('vendor-logout',views.userlogout, name='VendorUserlogout'),
    path('myaffiliate',views.Myaffiliate.as_view(), name='myaffiliate'),
    path('salesby-affiliate',views.Salesbyaffiliate.as_view(), name='salesbyaffiliate'),
    

    
    

]
