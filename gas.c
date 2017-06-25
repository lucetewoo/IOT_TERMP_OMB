#include<stdio.h>
#include<wiringPi.h>
#define GAS_PIN 19



int main(void){

char gas[1];

FILE *fp;
wiringPiSetupGpio();
pinMode(GAS_PIN,INPUT);

while(1){
if(digitalRead(GAS_PIN)==LOW){
printf("GAS DETECTED");
gas[0] = '1';
printf("\n");
}
else{
printf("Cool Environment");
gas[0] = '0';
printf("\n");
}
delay(1000);

fp = fopen("gasValue.txt","w");

fputs(gas, fp);

fclose(fp);
}





return 0;
}
