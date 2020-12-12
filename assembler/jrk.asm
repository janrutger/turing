# test program

	push 2
	push 2

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