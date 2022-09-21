int leds[] = {10, 11, 12, 13};

void setup() {
  // put your setup code here, to run once:    
  Serial.begin(9600);
  Serial.setTimeout(10); //ms  por defecto = 1000

  for(int i  = 0; i<4; i++){
    pinMode(leds[i], OUTPUT);
    }
    
}


int led_a_prender;
void loop() { //16Mhz
  // put your main code here, to run repeatedly:
  led_a_prender = random(0, 4); 
  //num aleatorio entre 0 y 3

  Serial.println(led_a_prender);

  for(int i  = 0; i< 4; i++){
    digitalWrite(leds[i], LOW);  
  }

  digitalWrite(leds[led_a_prender], HIGH);

  delay(3000);
}
