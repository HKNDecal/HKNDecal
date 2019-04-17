/*
 * In this demo, we'll be using a photoresistor to change the rate
 * at which a capacitor charges, displaying its voltage with LEDs
 */

#define CAP_PIN               P6_2   //Capacitor input voltage
#define LED33                 P2_5
#define LED66                 P2_4
#define LED100                P1_4
#define POWER_PIN             P6_3  //What the photoresistor is connected to

int input;

// TODO: Change here in part 2
const int period =  1; // in milliseconds

void setup()
{
  Serial.begin(9600);
  delay(500); // Otherwise the code doesn't always run successfully
  pinMode(CAP_PIN, INPUT);    //Setting up input pin
  pinMode(LED33, OUTPUT); //Setting up output for LED
  pinMode(LED66, OUTPUT); //Setting up output for LED
  pinMode(LED100, OUTPUT); //Setting up output for LED
  pinMode(POWER_PIN, OUTPUT);
  delay(500); // Otherwise the code doesn't always run successfully
}

//Sets the voltages of all LEDs
void setVoltages(int input) {
  int one_third = 1365;
  float ledRatio;
  if (input >= 2*one_third) {
    ledRatio = ((float)(input - 2*one_third)) / (float) one_third;
    digitalWrite(LED33, HIGH);
    digitalWrite(LED66, HIGH);
    analogWrite(LED100, (int) (255*ledRatio));    //Maps to value between 0-255
    Serial.println("Controls LED33: 255");
    Serial.println("Controls LED66: 255");
    Serial.print("Controls LED100: ");
    Serial.println((int) (255 * ledRatio));
  } else if (input >= one_third) {
    ledRatio = ((float) (input - one_third)) / (float) one_third;
    analogWrite(LED33, 255);
    analogWrite(LED66, (int) (255 * ledRatio));   //Maps to value between 0-255
    analogWrite(LED100, 0);
    Serial.println("Controls LED33: 255");
    Serial.print("Controls LED66: ");
    Serial.println((int) (255 * ledRatio));
    Serial.println("Controls LED100: 0");
  } else if (input < one_third) {
    ledRatio = ((float) input) / (float) one_third;
    analogWrite(LED33, (int) (255 * ledRatio));   //Maps to value between 0-255
    analogWrite(LED66, 0);
    analogWrite(LED100, 0);
    Serial.print("Controls LED33: ");
    Serial.println((int) (255 * ledRatio));
    Serial.println("Controls LED66: 0");
    Serial.println("Controls LED100: 0");
  }
}

void loop()
{
   /*
   * You can read the capacitor and LED values by opening the Serial Monitor in Tools > Serial Monitor
   */

  // Reading Observation
  input = analogRead(CAP_PIN); //Reading voltage across capacitor
  Serial.print("Observation: ");
  Serial.println(input);

  // Applying Controls
  setVoltages(input);

  if (input <= 50) {
    digitalWrite(POWER_PIN, HIGH);    //Want to start charging capacitor
  } else if (input >= 4020) {
    digitalWrite(POWER_PIN, LOW);     //Want to start discharging capacitor
  }
  
  // Pausing for a brief moment
  delay(period);
}
