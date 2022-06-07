# test program
speed 5
push 0b1100
push 0b1010

storem $jan1
storem $jan

loadm $jan1
loadm $jan

halt


	speed 3

	push 2
	push 1

	loadb
	#loada

	speed 5

	testg

	halt