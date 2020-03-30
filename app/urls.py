from django.urls import path
from app.views import *


app_name="app"
urlpatterns=[
    path("",index,name="index"),
    path("login_page/",login_page,name="login_page"),
    path("login_view/",login_view,name="login_view"),
    path("signup_page/",signup_page,name="signup_page"),
    path('signup_view/',signup_view,name="signup_view"),
    path("logout_view/",logout_view,name="logout_view"),
    path("reset_page/",reset_page,name="reset_page"),
    path("save_contact/",save_contact,name="save_contact"),
    path("reset_password_view/",reset_password_view,name="reset_password_view"),
    path("update_profile_page/",update_profile_page,name="update_profile_page"),
    path("update_profile/<slug:slug>/",update_profile,name="update_profile"),
    path("detail/<int:id>/", detail, name="detail"),
    path("add_cart<int:id>/", add_cart, name="add_cart"),
    path("view_cart/", view_cart, name="view_cart"),
    path("add_order/<int:id>/",add_order,name="add_order"),
    path("view_order/",view_order,name="view_order"),
    path("remove_order/<int:id>/",remove_order,name="remove_order"),
    path("remove_cart/<int:id>/",remove_cart,name="remove_cart"),

]


