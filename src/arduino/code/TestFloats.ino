#include <Wire.h>
#include <string.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver();

String data;

byte ROBOT_GRIPPER = 6;
byte ROBOT_WRIST = 5;
byte ROBOT_ARM_TOP = 4;
byte ROBOT_ARM_BOTTOM = 3;
byte ROBOT_SHOULDER_RIGHT = 2;
byte ROBOT_SHOULDER_LEFT = 1;
byte ROBOT_BASE = 0;

int minGripper = 0;
int minWrist = 0;
int minArmTop = 0;
int minArmBottom = 0;
int minShoulders = 0;
int minBase = 0;

int firstMovementList[10];
int secondMovementlist[10];

void setup()
{
  Serial.begin(9600);
  pwm1.begin();
  pwm1.setPWMFreq(60);
}
// TODO: Crear un movimiento inicial o estado inicial del brazo...
// Utilizar el minimo y maximo con los dos movimientos.... predecidos del brazo....

void loop()
{
  if (Serial.available())
  {
    /*float f = Serial.read() << 24;
    f = ((unsigned long) f) | (Serial.read() << 16);
    f = ((unsigned long) f) | (Serial.read() << 8);
    f = ((unsigned long) f) | Serial.read();
    Serial.print(f);*/
    data = Serial.readString();
    // Serial.println(data);
    myFunc(data, '-');
  }
  /*
    delay(500);
    Serial.println(23);
    delay(500);
    Serial.println("data");
    delay(500);
    Serial.println(23.5);
    delay(500);*/
}

void myFunc(String str, char delimiter)
{
  String temp = "";  
  int firstMovementCounter = 0;
  int secondMovementCounter = 0;

  for (int i = 0; i <= str.length(); i++)
  {
    if (str[i] != delimiter)
    {
      temp += str[i];
    }
    else
    {
      if (firstMovementCounter < 5) {
        firstMovementList[firstMovementCounter] = temp.toInt();
        temp = "";
        firstMovementCounter++;        
      } else {
        secondMovementlist[secondMovementCounter] = temp.toInt();
        temp = "";
        secondMovementCounter++;
      }
    }
  }

  robotMovement(1, 1);
}

void robotMovement(int position, int signal)
{
  switch (position)
  {
  case 5:
    // move gripper
    for (int i = minGripper; i < signal; i += 5)
    {
      pwm1.setPWM(ROBOT_GRIPPER, 0, i);
      delay(500);
    }
    break;

  case 4:
    // move wrist
    for (int i = minWrist; i < signal; i++)
    {
      pwm1.setPWM(ROBOT_WRIST, 0, signal);
      delay(500);
    }
    break;

  case 3:
    // move arm top
    for (int i = minArmTop; i < signal; i++)
    {
      pwm1.setPWM(ROBOT_ARM_TOP, 0, signal);
      delay(500);
    }
    break;

  case 2:
    // move arm bottom
    for (int i = minArmBottom; i < signal; i++)
    {
      pwm1.setPWM(ROBOT_ARM_BOTTOM, 0, signal);
      delay(500);
    }
    break;

  case 1:
    // move shoulders

    for (int i = minShoulders; i < signal; i++)
    {
      pwm1.setPWM(ROBOT_SHOULDER_RIGHT, 0, signal);
      pwm1.setPWM(ROBOT_SHOULDER_LEFT, 0, signal);
      delay(500);
    }
    break;

  case 0:
    // move base

    for (int i = minBase; i < signal; i++)
    {
      pwm1.setPWM(ROBOT_BASE, 0, signal);
      delay(500);
    }
    break;

  default:
    break;
  }
}