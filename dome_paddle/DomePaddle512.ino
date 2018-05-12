#include <XBOXRECV.h>
#include <SoftwareSerial.h>

// Satisfy the IDE, which needs to see the include statment in the ino too.
#ifdef dobogusinclude
#include <spi4teensy3.h>
#endif
#include <SPI.h>

USB Usb;
XBOXRECV Xbox(&Usb);

class Axis {
  public:

  Axis(int PositivePin, int NegativePin) {
    _posPin = PositivePin;
    _negPin = NegativePin;
    _lastCommandTime = 0;
    _state = 0;

    pinMode(_posPin, OUTPUT);
    pinMode(_negPin, OUTPUT);
  }

  boolean MovePositive() {
    if (_state != 'N') {
      digitalWrite(_posPin, LOW);
      _state = 'P';
      _lastCommandTime = millis();
      return true;//returns true if it moved positively
    }
    return false;//return false if it did not move positively
  }

  boolean MoveNegative() {
    if (_state != 'P') {
      digitalWrite(_negPin, LOW);
      _state = 'N';
      _lastCommandTime = millis();
      return true;//return true if it moved negatively
    }
    return false;//return false if it did not move negatively
  }

  void Stop() {
    if (millis() - _lastCommandTime > 200) {
      digitalWrite(_posPin, HIGH);
      digitalWrite(_negPin, HIGH);
      _state = 0;
    }
  }

  private:
    char _state;
    double _posPin;
    double _negPin;
    unsigned long _lastCommandTime;
};


Axis N_S_Axis(2,3);
Axis E_W_Axis(4,5);

void setup() {
  Serial.begin(115200);
#if !defined(__MIPSEL__)
  while (!Serial); // Wait for serial port to connect - used on Leonardo, Teensy and other boards with built-in USB CDC serial connection
#endif
  if (Usb.Init() == -1) {
    Serial.print(F("\r\nOSC did not start"));
    while (1); //halt
  }
  Serial.print(F("\r\nXBOX USB Library Started"));
}
void loop() {
  Usb.Task();
  if (Xbox.XboxReceiverConnected) {
    for (uint8_t i = 0; i < 4; i++){
      if (Xbox.Xbox360Connected[i]) {
        if (Xbox.getButtonPress(L2, i)) {
          
          // NORTHWEST and SOUTHWEST
          if (Xbox.getButtonPress(UP, i) && Xbox.getButtonPress(RIGHT, i)) {
            N_S_Axis.MovePositive();
            E_W_Axis.MovePositive();
            Serial.print("NORTHWEST");
          } else if (Xbox.getButtonPress(DOWN, i) && Xbox.getButtonPress(RIGHT, i)) {
            N_S_Axis.MoveNegative();
            E_W_Axis.MovePositive();
            Serial.print("SOUTHWEST");
          } 

          // NORTHEAST and SOUTHEAST
          if (Xbox.getButtonPress(UP, i) && Xbox.getButtonPress(LEFT, i)) {
            N_S_Axis.MovePositive();
            E_W_Axis.MoveNegative();
            Serial.print("NORTHEAST");
          } else if (Xbox.getButtonPress(DOWN, i) && Xbox.getButtonPress(LEFT, i)) {
            N_S_Axis.MoveNegative();
            E_W_Axis.MoveNegative();
            Serial.print("SOUTHEAST");
          }
          
          
          if (Xbox.getButtonPress(UP, i)) {  // North
            Xbox.setLedOn(LED1);
            N_S_Axis.MovePositive();
            Serial.print("N");
            break;
          } else if (Xbox.getButtonPress(DOWN, i)) {  // South
            Xbox.setLedOn(LED4);
            N_S_Axis.MoveNegative();
            Serial.print("S");
            break;
          } else if (Xbox.getButtonPress(RIGHT, i)) {  // West
            Xbox.setLedOn(LED3);
            E_W_Axis.MovePositive();
            Serial.print("W");
            break;
          } else if (Xbox.getButtonPress(LEFT, i)) {  // East
            Xbox.setLedOn(LED2);
            E_W_Axis.MoveNegative();
            Serial.print("E");
            break;
          } else {
            N_S_Axis.Stop();
            E_W_Axis.Stop();
          }
        }
      }
    }
  delay(1);
  }
}
