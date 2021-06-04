#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>

const char* ssid = "hathway31"; 
const char* password = "idontknow"; 

const char* host = "script.google.com";
const int httpsPort = 443;

WiFiClientSecure client;

String GAS_ID = "AKfycbyQzklPOVxiNYa0V8i5NPe5F_SrU7JMzznyIPtCV7RczjwSuQ";

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
  delay(500);

  WiFi.begin(ssid, password);
  Serial.println("");
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(250);
  }
  Serial.println("");
  Serial.print("Successfully connected to : ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  client.setInsecure();
}

void loop() {
  int voltage = 5;
  float average=0;
  for (int i=0;i<1000;i++)
  { 
    int read=analogRead(A0);
    average=average+(((0.199264*read))-1.52)/1000;
    delay(1);
    }
    
  int current=average;
  Serial.println(current);
  
  sendData(current, voltage); 
  delay(6000);
}

void sendData(int i, int v) {
  Serial.println("==========");
  Serial.print("connecting to ");
  Serial.println(host);
  
  if (!client.connect(host, httpsPort)) {
    Serial.println("connection failed");
    return;
  }
  
  String string_current =  String(i);
  String string_voltage =  String(v); 
  String url = "/macros/s/" + GAS_ID + "/exec?Amp=" + string_current + "&Volt=" + string_voltage;
  Serial.print("requesting URL: ");
  Serial.println(url);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
         "Host: " + host + "\r\n" +
         "User-Agent: BuildFailureDetectorESP8266\r\n" +
         "Connection: close\r\n\r\n");
  Serial.println("request sent");
  while (client.connected()) {
    String line = client.readStringUntil('\n');
    if (line == "\r") {
      Serial.println("headers received");
      break;
    }
  }
  String line = client.readStringUntil('\n');
  if (line.startsWith("{\"state\":\"success\"")) {
    Serial.println("esp8266/Arduino CI successfull!");
  } else {
    Serial.println("esp8266/Arduino CI has failed");
  }
  Serial.print("reply was : ");
  Serial.println(line);
  Serial.println("closing connection");
  Serial.println("==========");
  Serial.println();
}
