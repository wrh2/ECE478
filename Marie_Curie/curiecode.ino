
#include <PololuMaestro.h>


#ifdef SERIAL_PORT_HARDWARE_OPEN
  #define maestroSerial SERIAL_PORT_HARDWARE_OPEN
#else
  #include <SoftwareSerial.h>
  SoftwareSerial maestroSerial(10, 11);
#endif

/* Next, create a Maestro object using the serial port.

Uncomment one of MicroMaestro or MiniMaestro below depending
on which one you have. */
MicroMaestro maestro(maestroSerial);
//MiniMaestro maestro(maestroSerial);

void setup()
{
  // Set the serial baud rate.
  maestroSerial.begin(9600);
}

void loop()
{

maestro.setTarget(0, 4000);//up 
  delay(100);
  maestro.setTarget(1, 4000);//up 
  delay(100);
  maestro.setTarget(0, 8000);//down 
  delay(100);
  maestro.setTarget(1, 8000);//up 
  delay(100);
  

//  code for eye movement 
  maestro.setTarget(0, 4000);//up 
  delay(500);
  maestro.setTarget(0, 8000);//down 
  delay(500);
 maestro.setTarget(0, 5000);
  delay(500);
  // eye motion left and right 
 maestro.setTarget(1, 4000);
  delay(500);
 maestro.setTarget(1, 8000);
  delay(500);
  maestro.setTarget(1, 6000);
  delay(500);


//opening and closing of mouth 
 maestro.setTarget(13,4000); //open
 delay(1500);
 maestro.setTarget(13,8000);//close
 delay(1500);


//eyebrow 
//right
maestro.setTarget(8, 6000);
  delay(500);
 maestro.setTarget(8, 8000);//up 
 delay(500);
//left
 maestro.setTarget(9, 4000);//up
 delay(500);
  maestro.setTarget(9, 6000);
  delay(500);
 //place between the eyebrow
 maestro.setTarget(10, 4000);//expand
  delay(500);
 maestro.setTarget(10, 8000);//contract
 delay(500);



// upper lip
  maestro.setTarget(11, 4000); //back
  delay(1000);
  maestro.setTarget(11, 8000); //front 
  delay(1000);
 //maestro.setTarget(11, 6000);
  delay(1000);
 //lower lip
 maestro.setTarget(12, 4000);// front 
  delay(1000);
 maestro.setTarget(12, 8000);//relaxed or back
  delay(1000);
  //maestro.setTarget(12, 6000);
  delay(1000);


  
}
