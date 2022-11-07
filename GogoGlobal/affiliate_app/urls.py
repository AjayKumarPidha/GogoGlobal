from django.urls import path
from.import views



urlpatterns=[
    
    path('dashboard', views.AffiliateHomePageViews.as_view(), name='affiliterDashboard'),
    path('affiliator-product-details', views.DetailsMyAffiliater.as_view(), name='MyaffiliterProduct'),
    path('affiliator-setting',views.SettingView.as_view(), name='affiliator-Setting'),
    path('changepassword',views.Change_password.as_view(), name='ChangePassword'),
    path("privacy-policy", views.PrivacyPolicy.as_view(), name="AffiliatePrivacyPolicy"),
    path("terms-coditions", views.TermsCoditionsViews.as_view(), name="AffiliatetermCoditions")

    
    
    
]
