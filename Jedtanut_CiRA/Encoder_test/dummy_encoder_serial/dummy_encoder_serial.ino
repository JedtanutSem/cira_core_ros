
int i = 0;
int x = 0;
unsigned long current = 0;
unsigned long last = 0;
unsigned long diff = 0;
void setup() {
  Serial.begin(500000);
  pinMode(LED_BUILTIN, OUTPUT);
  
}

void loop()
{
  if(x == 0  )
  {
  for(i = 0 ; i<=10000;i++)
  {
    x++;
    current = millis();
    Serial.print(x);
    Serial.print(",");
    Serial.print(x);
    delayMicroseconds(10);  
    Serial.println("");
    
  }
  if(i > 10000)
  {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(5000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);
  for(i = 0 ; i<=10000;i++)
  {
    x--;
    current = millis();
    Serial.print(x);
    Serial.print(",");
    Serial.print(x);
    delayMicroseconds(10);  
    Serial.println("");
    
  }
  }
  
  }

  }
