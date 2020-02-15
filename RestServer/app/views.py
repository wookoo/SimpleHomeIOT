from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import socket
import struct
import requests

WOL_PC_IP_ADDRESS = "INPUT_IP" #WOL 컴퓨터 내부 ip 주소
MAC_ADDRESS = "INPUT_MAC" #EX : 00-00-00-00-00-00
USER_NAME = "INPUT_USER" #유저 이름 적기

@csrf_exempt
def computer(request): #WOL 방식으로 컴퓨터 켜기
    if(request.method == "POST"):
        json_str = (request.body).decode('utf-8')
        received_json = json.loads(json_str)
        try:
            user = received_json["user"]
            if user == USER_NAME:
                mac = MAC_ADDRESS
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
                s.sendto(magic,(WOL_PC_IP_ADDRESS,7))
                s.close()
                return JsonResponse({"response":"success"},json_dumps_params = {'ensure_ascii':False})
        except:
            pass

    return JsonResponse({"response":"fail"},json_dumps_params = {'ensure_ascii':False})




PHYSIC_SWITCH_IP = "http://172.30.1.99/" #물리적 방식 연결 nodemcu ip주소

@csrf_exempt
def computer_physic(request): #물리적 방식으로 컴퓨터 켜기
    if(request.method == "POST"):
        json_str = (request.body).decode('utf-8')
        received_json = json.loads(json_str)
        try:
            user = received_json["user"]
            if user == USER_NAME:
                requests.get(PHYSIC_SWITCH_IP+"on")
                return JsonResponse({"response":"success"},json_dumps_params = {'ensure_ascii':False})
        except:
            pass

    return JsonResponse({"response":"fail"},json_dumps_params = {'ensure_ascii':False})




ROOM_LIGHT_SWITCH_IP = "http://172.30.1.98/" ## DeviceSource/LightSwitch.ino 파일 19번째 주소와 일치 시킬것
@csrf_exempt
def room(request,switch):

    if (switch == "on"):
        requests.get(ROOM_LIGHT_SWITCH_IP+"on")
    else:
        requests.get(ROOM_LIGHT_SWITCH_IP+"off")

    return JsonResponse({"response":"success"},json_dumps_params = {'ensure_ascii':False})




#@csrf_exempt
#def message(request):
#    print(request.method)
#    json_str = (request.body).decode('utf-8')
#    print(json_str)
#    return JsonResponse({"response":"temp"},json_dumps_params = {'ensure_ascii':False})
