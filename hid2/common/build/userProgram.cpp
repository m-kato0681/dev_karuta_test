#include <avr/eeprom.h>
#include "Arduino.h"
#include "usbdrv.h"
#include "userProgram.h"
#include "motorControl.h"
#include "waiting.h"

#define PIN_IR 14
#define PIN_TOUCH_L 16
#define PIN_TOUCH_R 17

#define POWER_ON_MOTION 200

// ---------------------------------------
// prototype declaration
// ---------------------------------------

// ---------------------------------------
// Global variable
// ---------------------------------------
// ---------------------------------------
// When the alarm time arrives.
// ---------------------------------------
int getIRPhoto()
{
    return analogRead(PIN_IR);
}
int getTouch_L()
{
    return digitalRead(PIN_TOUCH_L);
}
int getTouch_R()
{
    return digitalRead(PIN_TOUCH_R);
}

void turnL()
{
    motorControl(FORWARD, STOP);
}
void turnR()
{
    motorControl(STOP, FORWARD);
}
void rotationL()
{
    motorControl(FORWARD, BACKWARD);
}
void rotationR()
{
    motorControl(BACKWARD, FORWARD);
}
void controlFORWARD()
{
    motorControl(FORWARD, FORWARD);
}
void controlBACKWARD()
{
    motorControl(BACKWARD, BACKWARD);
}
void controlSTOP()
{
    motorControl(STOP, STOP);
}

void initProgram()
{
    initMotor();
    pinMode(PIN_IR, INPUT);
    pinMode(PIN_TOUCH_L, INPUT_PULLUP);
    pinMode(PIN_TOUCH_R, INPUT_PULLUP);
}

// ---------------------------------------
// mainroutine
// ---------------------------------------
int calibDC[] = {0, 0};

void loopProgram() {
   while (true) { check();
      if ((getTouch_L() == 0)) {
         if ((getTouch_R() == 0)) {
            controlBACKWARD();
            delay(0.5 * 1000UL);
            rotationL();
            delay(1 * 1000UL);

         } else {
            rotationR();
            delay(0.2 * 1000UL);
         }

      } else {
         if ((getTouch_R() == 0)) {
            rotationL();
            delay(0.2 * 1000UL);

         } else {
            controlFORWARD();
         }
      }
      if ((getIRPhoto() < 10)) {
         controlBACKWARD();
         delay(0.5 * 1000UL);
         rotationR();
         delay(1 * 1000UL);
      }
   }
}
