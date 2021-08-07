"""myobject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#前台大堂点餐端子路由文件
from django.contrib import admin
from django.urls import path,include
from web.views import index,cart,orders

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',index.index,name='index'),

    #前端登陆退出的路由
    path('login', index.login, name="web_login"), #加载登录表单
    path('dologin', index.dologin, name="web_dologin"), #执行登录
    path('logout', index.logout, name="web_logout"), #退出
    path('verify', index.verify, name="web_verify"), #输出验证码

    #为urls路由添加请求前缀,凡此带web前缀的地址，都要登录之后才能访问
    path('web/',include([
        path('', index. webindex, name='web_index'),#前台大堂点餐首页

        # 购物车信息管理路由
        path('cart/add/<int:pid>', cart.add, name='web_cart_add'),#购物车添加
        path('cart/delete/<int:pid>', cart.delete, name='web_cart_delete'),#购物车删除
        path('cart/clear', cart.clear, name='web_cart_clear'),#购物车清空
        path('cart/change', cart.change, name='web_cart_change'),#购物车更改

        # 订单信息管理路由
        path('orders/insert', orders.insert, name='web_orders_insert'),  # 执行订单添加
        path('orders/<int:pindex>',orders.index, name='web_orders_index'),  # 购物车删除
        path('orders/detail', orders.detail, name='web_orders_detail'),  # 购物车清空
        path('orders/status', orders.status, name='web_orders_status'),  # 购物车更改
    ]))
]
