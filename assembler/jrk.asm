# test program

	push 5
	push 3

	storem $getal
	push 0
	loada
	loadb

:loop
	loadm $getal
	add

	decrementb
	jumpf :loop

	storea
	storem $result
	loadm $result

	halt