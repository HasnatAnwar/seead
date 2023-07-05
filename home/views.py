from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication , BaseAuthentication ,SessionAuthentication
from rest_framework.permissions import IsAdminUser , IsAuthenticated ,  BasePermission
from rest_framework.decorators import authentication_classes , permission_classes
from django.http import HttpResponse
from rest_framework import serializers, status
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate
from django.utils.timezone import now
from django.http import  QueryDict  
from home.serial import *
from home.models import *
from rest_framework.authtoken.models import Token
# pagination
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# from django.core.paginator import Paginator ,EmptyPage , PageNotAnInteger






def mutable(request):
    request.data._mutable =True

def DicttoQDict(dataa,request):
    if type(dataa)==dict:
        o_dataa = dataa
        dataa = QueryDict('',mutable=True)
        dataa.update(o_dataa)
    else:
        request.data._mutable =True




@api_view(['GET'])
def check(request):
    return Response(
        status=status.HTTP_200_OK,
        data={
            "message":"Check Succesfuly",
            
        }
    )



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def locations_get(request):
    
    # for the user checking
    # print(request.user)

    snippet = location.objects.all()
    serialize = locationSerial(snippet,many=True)


    return Response(
        status=status.HTTP_200_OK,
        data={
            "message":"Check Succesfuly",
            "data":serialize.data
        }
    )

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def location_post(request):
    
    # for the user checking
    # print(request.user)

    dataa = request.data 

        # mutable(request)
    DicttoQDict(dataa, request)

    serialize = locationSerial(data=dataa)
    if serialize.is_valid():
        serialize.save()
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"You added the location successfully",
                "data":serialize.data
            }
        )
    return Response(
        status=status.HTTP_200_OK,
        data={
            "message":"There is somekind of mistak in you data",
            
        }
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def location_get(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = location.objects.get(loc_id=pk)
    except location.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location not found",
                
            }
        )
    if request.method == "GET":
        snippet = location.objects.filter(loc_id=pk)
        serialize = locationSerial(snippet,many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location is here",
                "data":serialize.data
            }
        )

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def location_delete(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = location.objects.get(loc_id=pk)
    except location.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location not found",
                
            }
        )
    if request.method == "DELETE":
        snippet.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Deleted the item",
            }
        )
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def location_put(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = location.objects.get(loc_id=pk)
    except location.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location not found",
                
            }
        )
    if request.method == "PUT":
        dataa = request.data
        DicttoQDict(dataa,request)
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
            snippet.save()
        serialize = locationSerial(snippet)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location item updated",
                "data":serialize.data
            }
        )




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def ads_get(request):
    
    # for the user checking
    # print(request.user)

    snippet = ad.objects.all()
    serialize = adSerial(snippet,many=True)


    return Response(
        status=status.HTTP_200_OK,
        data={
            "message":"Check Succesfuly",
            "data":serialize.data
        }
    )

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def ad_post(request):
    
    # for the user checking
    # print(request.user)

    dataa = request.data 

        # mutable(request)
    DicttoQDict(dataa, request)

    serialize = adSerial(data=dataa)
    if serialize.is_valid():
        serialize.save()
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"You added the Ad successfully",
                "data":serialize.data
            }
        )
    return Response(
        status=status.HTTP_200_OK,
        data={
            "message":"There is somekind of mistak in you data",
            
        }
    )


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ad_get(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = ad.objects.get(ad_id=pk)
    except ad.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad not found",
                
            }
        )
    if request.method == "GET":
        snippet = ad.objects.filter(ad_id=pk)
        serialize = adSerial(snippet,many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad is here",
                "data":serialize.data
            }
        )

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ad_delete(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = ad.objects.get(ad_id=pk)
    except ad.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad not found",
                
            }
        )
    if request.method == "DELETE":
        snippet.delete()
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Deleted the item",
            }
        )


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ad_put(request,pk):
    dataa= request.data 
    # mutable(request)
    DicttoQDict(dataa, request)
    try :
        snippet = ad.objects.get(ad_id=pk)
    except ad.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad not found",
                
            }
        )
    if request.method == "PUT":
        dataa = request.data
        DicttoQDict(dataa,request)
        key = dataa.keys()
        for k in key:
            setattr(snippet,k,dataa[k])
            snippet.save()
        serialize = adSerial(snippet)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Location item updated",
                "data":serialize.data
            }
        )




# add visits 
# block after cross limit

@api_view(['GET'])

def ad_visits(request,pk):
    try :
        snippet = ad.objects.get(ad_id=pk)
    except ad.DoesNotExist:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad not found",
                
            }
        )
    dataa= request.data 
    DicttoQDict(dataa, request)
    snippet = ad.objects.get(ad_id=pk)

    serialize = adSerial(snippet)
    
    print(serialize.data)
    locate = serialize.data['ad_loc']
    print('here location')
    print(locate)
    locate = location.objects.get(loc_id = locate)
    locateserialize = locationSerial(locate)
    locatelimit = locateserialize.data['loc_limit']
    print(locatelimit)
    if int(locateserialize.data['loc_limit'])-1 >= int(serialize.data['ad_visits']):


        # to block when  exceeds the limit
        setattr(snippet,'ad_visits',int(serialize.data['ad_visits'])+1)
        snippet.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Limit  Not Filled",
                "data":serialize.data
            }
        )
    else:
        return Response(
            status=status.HTTP_200_OK,
            data={
                "message":"Ad Limit is full",
                
            }
        )



