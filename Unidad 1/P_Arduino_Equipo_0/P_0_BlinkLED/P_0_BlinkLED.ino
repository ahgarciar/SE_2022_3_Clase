int led = 13; //variable asignada al pin 13

void setup() {
  // put your setup code here, to run once:

  pinMode(led, OUTPUT);
  
}

void loop() { //16Mhz
  // put your main code here, to run repeatedly:
  
  digitalWrite(led, 1); //1, HIGH, true
  delay(1000);//ms
  digitalWrite(led, 0); //1, HIGH, true
  delay(1000);//ms
  
}
