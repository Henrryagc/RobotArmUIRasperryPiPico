
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver();

String data;
bool isConnected = false;

byte ROBOT_GRIPPER = 6;
byte ROBOT_WRIST = 5;
byte ROBOT_ARM_TOP = 4;
byte ROBOT_ARM_BOTTOM = 3;
byte ROBOT_SHOULDER_RIGHT = 2;
byte ROBOT_SHOULDER_LEFT = 1;
byte ROBOT_BASE = 0;

void setup() {
    Serial.begin(9600);
    while (!Serial);  
    Serial.println("Begin");
    pwm1.begin();
    pwm1.setPWMFreq(60); // This is the maximum PWM frequency   
    pinMode (13, OUTPUT);
}

void loop() {    

    if(Serial.available()) {        
        data = Serial.readString();

        int position = data.substring(0, 1).toInt();
        int signal = data.substring(2).toInt();
        Serial.println(signal);
        robotMovement(position, signal);
    } 
    /*
        digitalWrite(13, HIGH);
        delay(1000);
        digitalWrite(13, LOW);
        delay(2000);
    */
}

void robotMovement(int position, int signal) {
    switch (position) {
    case 5:
        // move gripper        
        pwm1.setPWM(ROBOT_GRIPPER, 0, signal);
        break;
    
    case 4:        
        // move wrist
        pwm1.setPWM(ROBOT_WRIST, 0, signal);
        break;

    case 3:
        // move arm top
        pwm1.setPWM(ROBOT_ARM_TOP, 0, signal);
        break;

    case 2:
        // move arm bottom
        pwm1.setPWM(ROBOT_ARM_BOTTOM, 0, signal);
        break;

    case 1:
        // move shoulders
        pwm1.setPWM(ROBOT_SHOULDER_RIGHT, 0, signal);
        pwm1.setPWM(ROBOT_SHOULDER_LEFT, 0, signal);
        break;
    
    case 0:
    // move base        
        pwm1.setPWM(ROBOT_BASE, 0, signal);
        break;

    default:
        break;
    }
}
