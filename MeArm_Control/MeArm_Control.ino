#include <Servo.h>
unsigned int table[8] = {0};
Servo myservo1; // 建立Servo物件，控制伺服馬達
Servo myservo2;
Servo myservo3;
Servo myservo4;

void setup() 
{ 
  myservo1.attach(9);
  myservo2.attach(10);// 連接數位腳位9，伺服馬達的訊號線
  myservo3.attach(11);
  myservo4.attach(12);
  myservo1.write(90);
  myservo2.write(90);
  myservo3.write(90);
  myservo4.write(0);
  delay(1000);
  Serial.begin(115200);
} 

void loop() 
{
  int readdata = 0, count = 0;
  if (Serial.available()>0)
  {
    while((readdata = Serial.read()) != (int)-1)
    {
      table[count] = readdata;
      count++;
      delay(10);
    }
    
    if((table[0] == 255) && (table[1] == 85))
    {
      myservo1.write(table[2]);
      delay(10);
      myservo2.write(table[3]);
      delay(10);
      myservo3.write(table[4]);
      delay(10);
      myservo4.write(table[5]);
      delay(10);
    }
  }
}