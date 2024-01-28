# from django.shortcuts import render

# # Create your views here.
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import status

# from rest_framework.response import Response
# from .seriallizers import *


# @api_view(['POST'])
# def regis(request):
#     if request.method == "POST":
#         data = {}
#         serializer = OutletSeriallizers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  # Save the new Karyawan record
#             data['msg'] = "Success"
#             data['outlet'] = serializer.data
#             return Response(data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#     else:
#         return Response("MethodNoTAlow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(['PUT'])
# def update_outlet(request, slug):
#     if request.method == "PUT":
#         try:
#             outlet_instance = Outlet.objects.get(slug=slug)
#         except:
#             return Response({"msg": "Outlet Not Found"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#         data = {}
#         serializer = OutletSeriallizers(
#             outlet_instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()  # Save the new Karyawan record
#             data['msg'] = "Success"
#             data['outlet'] = serializer.data
#             return Response(data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#     else:
#         return Response("MethodNoTAlow", status=status.HTTP_405_METHOD_NOT_ALLOWED)
