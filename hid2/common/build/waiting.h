#ifndef __WAITING_H_
#define __WAITING_H_

#define delay(t) waiting(t);

bool waiting(unsigned long duration);
bool check();

#endif
