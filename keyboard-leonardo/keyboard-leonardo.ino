#include <Arduino.h>

#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <Bounce2.h>

//buttons settings
//pin definitios
int A = 9, B = 8;
int up = 10, down = 11, left = 12, right = 14;
//bounce objects
Bounce btnA = Bounce();
Bounce btnB = Bounce();
Bounce btnUp = Bounce();
Bounce btnDown = Bounce();
Bounce btnLeft = Bounce();
Bounce btnRight = Bounce();
//variables to store the value.
bool statusA = false, statusB = false, statusUp = false, statusDown = false, statusLeft = false, statusRight = false;

int debounceTime = 10;

//encoder settings
Encoder myEnc(5, 6);
int pinBtn = 7;
int pinLedLong = 13;

bool clicked = false;

long oldPosition  = -999;

int userDelay = 250;
unsigned long nextTime;
int intervale = 1000;

// Number of mechanichal clicks of the encoder to increase or decrease
//the volume of the computer.
int mechClicks = 2;
int pulsesPerClick = 4; // Electrical pulses per mechanichal pulse

int rotation = (pulsesPerClick*mechClicks) - 1;

void setup() {

  Serial.begin(19200);
  //encoder setup
  pinMode(pinBtn, INPUT);
  pinMode(pinLedLong, OUTPUT);

  //buttons setup
  pinMode(A, INPUT);
  btnA.attach(A);
  btnA.interval(debounceTime);
  pinMode(B, INPUT);
  btnB.attach(B);
  btnB.interval(debounceTime);
  pinMode(up, INPUT);
  btnUp.attach(up);
  btnUp.interval(debounceTime);
  pinMode(down, INPUT);
  btnDown.attach(down);
  btnDown.interval(debounceTime);
  pinMode(left, INPUT);
  btnLeft.attach(left);
  btnLeft.interval(debounceTime);
  pinMode(right, INPUT);
  btnRight.attach(right);
  btnRight.interval(debounceTime);

  // Sends a clean report to the host. This is important on any Arduino type.
  Consumer.begin();
  Keyboard.begin();
  delay(100);
}

void loop() {
  updateButtons();
  sendKeyStrokes();
  Serial.println(statusA);

  nextTime = millis() + intervale;
  while (digitalRead(pinBtn)) {
    clicked = true;
    if (millis() > nextTime) {
      digitalWrite(pinLedLong, HIGH);
    }
  }
  digitalWrite(pinLedLong, LOW);
  if (clicked) {
    if (millis() > nextTime) {
      //Long click
      nextSong();
    } else {
      //Short click
      playPause();
    }
    delay(userDelay);//Debouncing
    clicked = false;
  }

  //encoder rotation
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    if (newPosition > (oldPosition + rotation)) {
      increaseVol();
      oldPosition = newPosition;
    }
    if (newPosition < (oldPosition - rotation)) {
      decreaseVol();
      oldPosition = newPosition;
    }
  }
}
void nextSong() {
  Consumer.write(MEDIA_NEXT);
}
void playPause() {
  Consumer.write(MEDIA_PLAY_PAUSE);
}
void increaseVol() {
  Consumer.write(MEDIA_VOLUME_UP);
}

void decreaseVol() {
  Consumer.write(MEDIA_VOLUME_DOWN);
}
void updateButtons(){
  //Update the buttons to have the last values
  btnA.update();
  btnB.update();
  btnUp.update();
  btnDown.update();
  btnLeft.update();
  btnRight.update();
  //store the last values in the variables
  statusA = btnA.read();
  statusB = btnB.read();
  statusUp = btnUp.read();
  statusDown = btnDown.read();
  statusLeft = btnLeft.read();
  statusRight = btnRight.read();
}

void sendKeyStrokes(){
  if (statusA){
    Keyboard.press('a');
    Keyboard.release('a');
  }
  if(statusB){
    Keyboard.press('b');
    Keyboard.release('b');
  }
  if(statusUp){
    Keyboard.write(KEY_UP_ARROW);
    Keyboard.release(KEY_UP_ARROW);
  }
  if(statusDown){
    Keyboard.write(KEY_DOWN_ARROW);
    Keyboard.release(KEY_DOWN_ARROW);
  }
  if(statusLeft){
    Keyboard.write(KEY_LEFT_ARROW);
    Keyboard.release(KEY_LEFT_ARROW);
  }
  if(statusRight){
    Keyboard.write(KEY_RIGHT_ARROW);
    Keyboard.release(KEY_RIGHT_ARROW);
  }
}
