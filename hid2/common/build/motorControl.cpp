#include <Arduino.h>
#include "motorControl.h"
#include "waiting.h"

byte rightPower = 0;
byte leftPower = 0;
byte rightState = STOP;
byte leftState = STOP;

void initMotor(){
    pinMode(PIN_RIGHT_A, OUTPUT);
    pinMode(PIN_RIGHT_B, OUTPUT);
    pinMode(PIN_LEFT_A, OUTPUT);
    pinMode(PIN_LEFT_B, OUTPUT);
}

void handleRight()
{
    /* Need to stop before rotation because of MCU is being reset due to low voltage. */
    digitalWrite(PIN_RIGHT_A, LOW);
    digitalWrite(PIN_RIGHT_B, LOW);
    if(rightPower > 0)
    {
        delay(50);
        if (rightState == FORWARD)
        {
            analogWrite(PIN_RIGHT_A, rightPower);
        }
        else if(rightState == BACKWARD)
        {
            analogWrite(PIN_RIGHT_B, rightPower);
        }
        else
        {
            digitalWrite(PIN_RIGHT_A, HIGH);
            digitalWrite(PIN_RIGHT_B, HIGH);
        }
    }
}
void handleLeft()
{
    digitalWrite(PIN_LEFT_A, LOW);
    digitalWrite(PIN_LEFT_B, LOW);
    if(leftPower > 0)
    {
        delay(50);
        if(leftState == FORWARD)
        {
            analogWrite(PIN_LEFT_A, leftPower);
        }
        else if(leftState == BACKWARD)
        {
            analogWrite(PIN_LEFT_B, leftPower);
        }
        else
        {
            digitalWrite(PIN_LEFT_A, HIGH);
            digitalWrite(PIN_LEFT_B, HIGH);
        }
    }
}
void handleBoth()
{
    digitalWrite(PIN_LEFT_A, LOW);
    digitalWrite(PIN_LEFT_B, LOW);
    digitalWrite(PIN_RIGHT_A, LOW);
    digitalWrite(PIN_RIGHT_B, LOW);
    delay(100);
    if (leftState == FORWARD && rightState == FORWARD)
    {
        analogWrite(PIN_LEFT_A, leftPower);
        analogWrite(PIN_RIGHT_A, rightPower);
    }
    if (leftState == BACKWARD && rightState == BACKWARD)
    {
        analogWrite(PIN_LEFT_B, leftPower);
        analogWrite(PIN_RIGHT_B, rightPower);
    }
    if (leftState == FORWARD && rightState == BACKWARD)
    {
        analogWrite(PIN_LEFT_A, leftPower);
        analogWrite(PIN_RIGHT_B, rightPower);
    }
    if (leftState == BACKWARD && rightState == FORWARD)
    {
        analogWrite(PIN_LEFT_B, leftPower);
        analogWrite(PIN_RIGHT_A, rightPower);
    }
    if (leftState == FORWARD && rightState == STOP)
    {
        analogWrite(PIN_LEFT_A, leftPower);
    }
    if (leftState == STOP && rightState == FORWARD)
    {
        analogWrite(PIN_LEFT_A, leftPower);
    }
}

void rightMotorControl(byte control)
{
    rightState = control;
    handleRight();
}
void rightMotorPower(byte power)
{
    rightPower = power;
    handleRight();
}
void leftMotorControl(byte control)
{
    leftState = control;
    handleLeft();
}
void leftMotorPower(byte power)
{
    leftPower = power;
    handleLeft();
}
void motorControl(byte controlL, byte controlR)
{
    leftPower = 200;
    rightPower = 200;
    leftState = controlL;
    rightState = controlR;
    handleBoth();
}
