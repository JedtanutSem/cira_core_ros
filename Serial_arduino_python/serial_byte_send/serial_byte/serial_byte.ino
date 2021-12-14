#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX

void setup() {
 mySerial.begin(9600);
}
void loop() {
 int analogVal = analogRead(A0);
 byte checksum = 0;
 checksum += (byte) analogVal;
 checksum += (byte) (analogVal >> 8);
 mySerial.write(253); // start 
 mySerial.write(255); // start 
 mySerial.write(analogVal); // lower byte
 mySerial.write(analogVal >> 8); // upper byte
 mySerial.write(checksum); //checksum
 delay(250);
}
