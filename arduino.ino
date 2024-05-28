const int CLASS_ROOM = 3;
const int LAB = 10;

void setup() {
  Serial.begin(9600);
  pinMode(CLASS_ROOM, OUTPUT);
  pinMode(LAB, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    switch(command) {
      case '0':
        digitalWrite(CLASS_ROOM, HIGH);
        break;
      case '1':
        digitalWrite(LAB, HIGH);
        break;
      case '2':
        digitalWrite(CLASS_ROOM, LOW);
        break;
      case '3':
        digitalWrite(LAB, LOW);
        break;
    }
  }
}