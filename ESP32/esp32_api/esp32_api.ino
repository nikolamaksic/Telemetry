#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
 
const char* ssid = "Maksic";
const char* password =  "nemasifre";


void setup() {
 
  Serial.begin(115200);
  delay(4000);   //Delay needed before calling the WiFi.begin
 
  WiFi.begin(ssid, password); 
 
  while (WiFi.status() != WL_CONNECTED) { //Check for the connection
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
 
}
 
void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
    JsonObject& root = JSONbuffer.createObject(); 
 
    root["front_left_weel"] = 2.9;
    root["front_right_weel"] = 2.8;
    root["back_left_weel"] = 2.7;
    root["back_right_weel"] = 2.1;
    root["servo_angle"] = 2.8;

    String jsonStr;
    root.printTo(jsonStr);
    Serial.println(jsonStr);
 
    HTTPClient http;    //Declare object of class HTTPClient
 
    http.begin("http://192.168.1.106:5000/measurement/");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
    http.addHeader("Authorization", "Basic czpk");
    http.addHeader("cache-control", "no-cache");
 
    int httpCode = http.POST(jsonStr);   //Send the request
    String payload = http.getString();                                        //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection
 
  } else {
 
    Serial.println("Error in WiFi connection");
 
  }
 
  delay(5000);  //Send a request every 5 seconds
}
