#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

//필요장비 : NODEMCU, 릴레이 스위치
//기능설명 : 릴레이 스위치를 사용한 전등 스위치 온 오프, 물리 장치

#ifndef STASSID
#define STASSID "USERSSID" //ssid 입력
#define STAPSK  "USERPASSWOORD" //비밀번호 입력
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

ESP8266WebServer server(80); //서버 포트주소

IPAddress ip(172, 30, 1, 98); //내부 아이피 주소 고정
IPAddress gateway(172, 30, 1, 254); //공유기 ip 주소 지정
IPAddress subnet(255, 255, 255, 0);

const int led = 13;
const int D1 = 5; //릴레이 스위치를 연결할 핀, D1
int Switch_Status = HIGH;

void handleRoot() {
  server.send(200, "text/plain", "hello from esp8266!");
}

void handleSwitchOn(){
  Switch_Status = LOW;
  server.send(200, "text/plain", "success");
}

void handleSwitchOff(){
  Switch_Status = HIGH;
  server.send(200, "text/plain", "success");
}


void handleNotFound() {
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void) {
  pinMode(D1,OUTPUT);
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  digitalWrite(D1, HIGH);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.config(ip,gateway,subnet); //와이파이 설정 변경
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }
  server.onNotFound(handleNotFound);
  server.on("/", handleRoot);
  server.on("/on",handleSwitchOn);
  server.on("/off",handleSwitchOff);
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  digitalWrite(D1,Switch_Status);
  server.handleClient();
  MDNS.update();
}
