#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver();

String data;

#define servoMIN 150 // Esto puede funcionar para los servos pequeños
#define servoMAX 600
byte servo = 0;

byte servos = 0;

void setup() {
    Serial.begin(9600);
    pwm1.begin();
    pwm1.setPWMFreq(60); // This is the maximum PWM frequency
    pinMode(13, OUTPUT);
}

void loop() {    

    if(Serial.available()) {
        Serial.println(Serial.available());
        data = Serial.readString();
        gripper(data.toInt());
        Serial.println(data);

        int position = data.substring(0, 1).toInt();
        int signal = data.substring(2).toInt();

        robotMovement(position, signal)
    }
       // gripper(data.toInt());
    /*for (int pulse = servoMIN; pulse < servoMAX; pulse++) {
    pwm1.setPWM(servo, 0, pulse);
    Serial.println(servo);
  }
  delay(100);*/
    /*if(Serial.available()) {
        data = Serial.readString();
       // gripper(data.toInt());
          
        pwm1.setPWM(0, 0, data.toInt());

        Serial.println(data); 
    }*/

    moverServos();
}


void gripper(int number) {
    switch (number){
    case 1:
        digitalWrite(13, HIGH);
        pwm1.setPWM(0, 0, 250);  
        break;
    case 2:
        digitalWrite(13, LOW);
        pwm1.setPWM(1, 0, 250);
        pwm1.setPWM(2, 0, 250);
        break;
    default:
        break;
    }
}

void moverServos(){
        for (int angulo = 150; angulo < 350; angulo+=10)
    {        
        if (servos!=1)  
        {
            pwm1.setPWM(servos, 0, angulo);    
        } else {
            pwm1.setPWM(servos, 0, angulo);            
            pwm1.setPWM(servos + 1, 0, angulo);
        }
        
        //angulo += 10;
        delay(300);
    }
    
    if (servos==1)
    {
        servos++;
    }
    
    servos++;

    if (servos>6)
    {
        servos = 0;
    }
}

void robotMovement(int position, int signal) {
    switch (position)
    {
    case 5:
        // move gripper
        pwm1.setPWM(5, 0, signal);
        break;
    
    case 4:
        pwm1.setPWM(4, 0, signal);
        // move wrist
        break;

    case 3:
        // move arm top
        pwm1.setPWM(3, 0, signal);
        break;

    case 2:
        // move arm bottom
        pwm1.setPWM(2, 0, signal);
        break;

    case 1:
        // move shoulders
        pwm1.setPWM(1, 0, signal);
        break;
    
    case 0:
    // move base
        pwm1.setPWM(0, 0, signal);
        break;

    default:
        break;
    }
}