/* Wi-CHORD: Chord Protocol application on a P2P LoRaWAN Wireless Sensor Network - IoT
* Supported LoRa MCU: TTGO T-BEAM v1.1 ESP32
* Implemented by: Christos-Panagiotis Balatsouras
* ORCID: https://orcid.org/0000-0001-8914-7559
*/

#include <LoRa.h>
#include <WiFi.h>
#include <ArduinoJson.h>
#include "mbedtls/md.h"

#define LED_PIN 4

// Define the hash space for hashing operations
#define HASH_SPACE 1024

// Define LoRa chip pins (Configuration for TTGO T-Beam v1.1 LoRa Board)
#define SCK 5
#define MISO 19
#define MOSI 27
#define SS 18
#define RST 23
#define DIO0 26

// Define LoRa Band (868MHz for Europe)
#define BAND 868E6

/* Global Variables */
int node_id = 0; // the node ID, initialy is zero before hashing the MAC address to calculate the id
String mac_addr = ""; // variable to store the node's MAC address
StaticJsonDocument<256> doc; // JSON Document to send sensor values via LoRa

/* Function to calculate the hash value of a given String input */
int getHash(String val, int space)
{
  Serial.print("SHA-1 Hashing the input: ");
  Serial.println(val);
  char const *input = val.c_str(); // input to be hashed
  byte shaResult[20]; // allocate memory for the result

  // select sha1 algorithm
  mbedtls_md_context_t context;
  mbedtls_md_type_t md_type = MBEDTLS_MD_SHA1;

  const size_t inputLength = strlen(input); // input length

  mbedtls_md_init(&context);
  mbedtls_md_setup(&context, mbedtls_md_info_from_type(md_type), 0);
  mbedtls_md_starts(&context);
  mbedtls_md_update(&context, (const unsigned char *) input, inputLength);
  mbedtls_md_finish(&context, shaResult);
  mbedtls_md_free(&context);

  String hash = ""; // hash output in HEX

  for(int i = 0; i < sizeof(shaResult); i++)
  {
    char str[3];
    sprintf(str, "%02x", (int)shaResult[i]);
    hash = hash + str;
  }

  String selected_hash = ""; // a subset of the hash output in HEX, for memory allocation reasons
  int max_chars = 7;
  selected_hash = hash.substring(0, max_chars);

  long output_val = 0; // the output value such as: out = sha1(val) mod space
  char *endptr;
  output_val = strtol(selected_hash.c_str(), &endptr, 16); // convert HEX String to DEC integer
  output_val = output_val % space;

  return output_val;
}

/* Function to retrieve the Node's MAC Address */
String getWiFiMAC()
{
  String mac_address = "";
  mac_address = WiFi.macAddress();
  return mac_address;
}

/* Initialize LoRa */
void setupLoRa()
{
  // setup lora connection
  SPI.begin(SCK, MISO, MOSI, SS); //SPI Communication for LoRa Chip pins
  LoRa.setPins(SS, RST, DIO0); //setup LoRa module
  if(!LoRa.begin(BAND))
  {
    Serial.println("ERROR: Could not start LoRa");
    delay(500);
    while(!LoRa.begin(BAND));
    {
      Serial.println("ERROR: Could not start LoRa");
      delay(500);
    }
  }
  LoRa.setSyncWord(0xF8);
  Serial.println("LoRa Started Successfully!");
}

/* Send LoRa Packet Function */
void sendLoRaPacket(String message, int &messageID)
{
  // Send the LoRa Packet
  Serial.print("Sending LoRa Package: ");
  Serial.println(messageID);
  Serial.print("Data: ");
  Serial.println(message);

  digitalWrite(LED_PIN, HIGH); // Indicate package sending with LED on GPIO4 pin
  LoRa.beginPacket();
  LoRa.print(message);
  LoRa.endPacket();
  delay(1000);
  digitalWrite(LED_PIN, LOW); // Indicate package sent with LED on GPIO4 pin
  
  messageID++;
}

/* Receive LoRa Packet Function */
String receiveLoRaPacket()
{
  String received_message = "";
  int packageSize = LoRa.parsePacket();
  if(packageSize)
  {
    Serial.print("Received packet: ");
    digitalWrite(LED_PIN, HIGH); // Indicate received package with LED on GPIO4
    
    // read package content
    while(LoRa.available())
    {
      // get LoRa data
      received_message = LoRa.readString();
      Serial.println(received_message);
    }
    delay(1000);
    digitalWrite(LED_PIN, LOW);
  }

  return received_message;
}

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
