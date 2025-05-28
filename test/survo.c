#include <stdio.h>
#include <wiringPi.h>

#define SERVO 29

int main(int n, char **s){ // servo [회전각도 0~180]
	
	if(n < 2){
		
			printf("Usave : servo [Rotate degree (0 ~ 180)]\n");
			return 0;
	
	}
	
	int r; // CLI 회전각도
	r = atoi(s[1]);
	r = r*500 / 90;	// microdelay value
	
	printf("Pulse width(ms) : %d\n\n", r);
	
	wiringPiSetup();
	pinMode(SERVO, OUTPUT);
	
	for(int i=0;i<10;i++){
		
		int r1 = 1500 +r *((i%2)?(-1):1);
		for(int j=0; j<10; j++){
			digitalWrite(SERVO, HIGH);
			delayMicroseconds(r1);  // 1ms = 90 degree
			digitalWrite(SERVO, LOW);
			delayMicroseconds(20000-r1); // 19ms + 1ms = 20ms = 50Hz
			
		}
		delayMicroseconds(60000);

	}
}
