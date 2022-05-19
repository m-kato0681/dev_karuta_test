#include <Arduino.h>
#include "waiting.h"

// Waiting for a specified period with monitoring check().
bool waiting(unsigned long duration) {
  unsigned long start = millis();
  while(millis() - start < duration) {
    if(check()) return false;
  }
  return true;
}
