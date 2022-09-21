int leds[] = {10, 11, 12};
//String cadena = "95A240A0";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

String cadena = "95A240A0";
//cadena = "XAYAZ"; //X,Y,Z 
//pueden ser cualquier valor en 0 y 255

String cad_aux= "";
void loop() {
  // put your main code here, to run repeatedly
  analogWrite(leds[0], 95);

  //"E0095A0240A0000F"
  if(cadena.charAt(0) == 'E' && cadena.charAt(15)=='F'){
    Serial.println("Cadena Completa");
    
    for(int i= 1; i<cadena.length()-1;i++){
        if(cadena[i]!='A'){
          cad_aux += cadena[i]; 
        }
        else{ //caracter leido  = 'A'
          Serial.println(cad_aux);
          cad_aux = "";
        }  
    }//fin for
    Serial.println(cad_aux);
  }//fin if que comprueba que la cadena sea completa
  while(true){}
  delay(1000);
}//fin del loop
