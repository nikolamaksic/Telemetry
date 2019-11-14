#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
 
const char* ssid = "Maksic";
const char* password =  "nemasifre";
HTTPClient http1,http2;
int get_pin_value(){

  return 2;}


String read_from_sensor(){
    StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
    JsonObject& root = JSONbuffer.createObject(); 
 
    root["front_left_weel"] = get_pin_value();
    root["front_right_weel"] = 2.8;
    root["back_left_weel"] = 2.7;
    root["back_right_weel"] = 2.1;
    root["servo_angle"] = 2.8;
    String jsonStr;
    root.printTo(jsonStr);
    
    return jsonStr;
 }

void start_http(){
   // HTTPClient http1,http2;    //Declare object of class HTTPClient
    http1.begin("http://192.168.1.106:5000/measurement/");      //Specify request destination
    http1.addHeader("Content-Type", "application/json");  //Specify content-type header
    http1.addHeader("Authorization", "Basic czpk");
    http1.addHeader("cache-control", "no-cache");

    http2.begin("http://192.168.1.106:5000/parameters/");      //Specify request destination
    http2.addHeader("Content-Type", "application/json");  //Specify content-type header
    http2.addHeader("Authorization", "Basic czpk");
    http2.addHeader("cache-control", "no-cache");
  }

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
    String jsonStr;
    jsonStr = read_from_sensor();
    Serial.println(jsonStr);
    start_http();
 
    int httpCode1 = http1.POST(jsonStr);   //Send the request
    String payload1 = http1.getString();    //Get the response payload
    Serial.println(httpCode1);   //Print HTTP return code
    Serial.println(payload1);
    delay(2000);

    
    String s;
    int httpCode2 = http2.GET();
    String payload2 = http2.getString(); 
    Serial.println(httpCode2);   //Print HTTP return code
    Serial.println("Primljeni parametri\n\n\n");
    Serial.println(payload2);



 
    http1.end();  //Close connection
    http2.end();
 
  } else {
 
    Serial.println("Error in WiFi connection");
 
  }
 
  delay(5000);  //Send a request every 5 seconds
}
