from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import socket
import struct
import requests

@csrf_exempt
def room(request,switch):
   
  #  if (switch == "on"):
  #      requests.get("http://172.30.1.99/on")
  #  else:
  #      requests.get("http://172.30.1.99/off")
    return JsonResponse({"response":"success"},json_dumps_params = {'ensure_ascii':False})


@csrf_exempt
def computer(request):
    if(request.method == "POST"):
        json_str = (request.body).decode('utf-8')
        received_json = json.loads(json_str)
        try:
            user = received_json["user"]
            
            '''    mac = "70-85-C2-03-B4-6C"
                addrs = mac.split("-")
                hw_addr = struct.pack("BBBBBB",int(addrs[0],16),
                                      int(addrs[1],16),
                                      int(addrs[2],16),
                                      int(addrs[3],16),
                                      int(addrs[4],16),
                                      int(addrs[5],16))
                magic = b"\xFF" * 6 + hw_addr *16

                s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
                s.sendto(magic,("118.37.231.3",7))
                s.close()'''
            if (user == "wookoo"):
                requests.get("http://172.30.1.99/on")
                return JsonResponse({"response":"success"},json_dumps_params = {'ensure_ascii':False})
        except:
            pass
        
    return JsonResponse({"response":"fail"},json_dumps_params = {'ensure_ascii':False})


@csrf_exempt
def message(request):
    print(request.method)
    json_str = (request.body).decode('utf-8')
    print(json_str)
    return JsonResponse({"response":"temp"},json_dumps_params = {'ensure_ascii':False})


    
   # content_name = received_json['content']
   # GetDB.GetDB(content_name)
   # type_name = received_json['type']


