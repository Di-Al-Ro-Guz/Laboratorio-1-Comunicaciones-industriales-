#include <Wire.h>

int pot = A0;
byte valor = 0;

void requestEvent() {
  int lectura = analogRead(pot);
  valor = lectura >> 2; // 10 bits → 8 bits
  Wire.write(valor);
}

void setup() {
  Wire.begin(8); // Dirección esclavo
  Wire.onRequest(requestEvent);
}

void loop() {
  delay(100);
}
