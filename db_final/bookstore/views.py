from django.shortcuts import render
from django.contrib.auth.models import Group

from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer
from bookstore.serializers import (
    UmsUserSerializer, OmsCartItemSerializer,
    OmsOrderSerializer,UserSerializer, GroupSerializer,
    BmsBookSerializer,BmsCategorySerializer
)
from bookstore.filters import BmsBookFilter
from bookstore.utils.render_response import CustomRenderer
import bookstore.models as models
import django_filters




# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    查看，编辑用户数据的API接口
    """
    queryset = models.AuthUser.objects.all().order_by('-date_joined')
    #UserSerializer是我们刚刚在serializers.py里面写好的class UserSerializer
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    
    """
    查看，编辑用户群组的API接口
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BmsBookViewSet(viewsets.ModelViewSet):
    """
    查看，编辑图书数据的API接口
    """
    queryset = models.BmsBook.objects.all()
    serializer_class = BmsBookSerializer
    filter_class = BmsBookFilter

class BmsCategoryViewSet(viewsets.ModelViewSet):
    """
    查看，编辑图书分类的API接口
    """
    queryset = models.BmsCategory.objects.all()
    serializer_class = BmsCategorySerializer

class OmsOrderViewSet(viewsets.ModelViewSet):
    """
    查看，编辑订单数据的API接口
    """
    queryset = models.OmsOrder.objects.all()
    serializer_class = OmsOrderSerializer

class OmsCartItemViewSet(viewsets.ModelViewSet):
    """
    查看，编辑购物车数据的API接口
    """
    queryset = models.OmsCartItem.objects.all()
    serializer_class = OmsCartItemSerializer

class UmsUserViewSet(viewsets.ModelViewSet):
    """
    查看，编辑用户数据的API接口
    """
    queryset = models.User.objects.all()
    serializer_class = UmsUserSerializer

    