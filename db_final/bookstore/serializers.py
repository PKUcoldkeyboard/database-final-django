#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-07-16 18:07:34
# @Author  : Pang S.Z (158505862@qq.com)
# @Link    : 
# @Version : $Id$

from django.contrib.auth.models import Group

import bookstore.models as models

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('id', 'url', 'username', 'email')
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=('id','url','name','user_set',)

class BmsBookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BmsBook
        fields = '__all__'

class BmsCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BmsCategory
        fields = '__all__'

class OmsOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OmsOrder
        fields = '__all__'
class OmsCartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OmsCartItem
        fields = '__all__'

class UmsUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
