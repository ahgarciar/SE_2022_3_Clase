int leds[] = {10, 11, 12, 13};

void setup() {
  // put your setup code here, to run once:    
  Serial.begin(9600);
  Serial.setTimeout(10); //ms  por defecto = 1000

  for(int i  = 0; i<4; i++){
    pinMode(leds[i], OUTPUT);
    }
    
}

String v; 
void loop() { //16Mhz
  // put your main code here, to run repeatedly:

  if(Serial.available()>0){
      v = Serial.readString(); //led que se va a prender
      for(int i = 0; i<4; i++){
          if(v == i){
              digitalWrite(leds[i], HIGH);
            }
            else{
              digitalWrite(leds[i], LOW);
              }
        }
    }
  
}
