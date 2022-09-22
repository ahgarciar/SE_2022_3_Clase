int leds[] = {10, 11, 12};
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cad_aux= "";
char c;
void loop() {
  // put your main code here, to run repeatedly 

  if(Serial.available()>0){
      c = Serial.read(); //lee un caracter
      if(c=='E'){
          cad_aux = "";
        }
      else if(c=='A' || c=='F'){
          Serial.println(cad_aux);
          cad_aux = "";
        }
      else{
          cad_aux += c;
        }
    }
    
  delay(1000);
}//fin del loop
