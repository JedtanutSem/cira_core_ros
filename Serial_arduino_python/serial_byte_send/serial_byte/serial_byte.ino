#include <SoftwareSerial.h>

//SoftwareSerial mySerial(2, 3); // RX, TX
int analogVal = 0;
byte val2 = 0;
byte val3 = 0;
void setup() {
 //mySerial.begin(9600);
 Serial.begin(9600);
}
void loop() {
  analogVal = 256;
  val2++;
  val3++;
 //int analogVal = analogRead(A0);
 //analogVal = 520;
 //val2 = 255;
 //val3 = 254;
 //Serial.print(analogVal);
 int checksum = 0;
 //checksum = 255+254;
 checksum += (byte) analogVal;
 checksum += (byte) (analogVal>>8);
 checksum += (byte) val2;
 checksum += (byte) val3;
 //Serial.print((byte) analogVal);
 //Serial.print(checksum);
 Serial.write(253); // start 
 Serial.write(255); // start 
 Serial.write(analogVal);
 Serial.write(analogVal>>8);
 //Serial.print(analogVal);
 Serial.write(val2);
 Serial.write(val3);
 //mySerial.write(analogVal); // lower byte
 //mySerial.write(analogVal >> 8); // upper byte
 Serial.write(checksum);
 Serial.write(checksum>>8);//checksum'
 //Serial.print(checksum);
 //Serial.write(checksum>>16);//checksum
 //Serial.write(checksum>>24);//checksum
 //Serial.print(checksum);
 delay(100);
}
