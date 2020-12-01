# Dit is mijn eerste test programma
	jump :init

:start
	storea
	add
	jump :loop


:init
	push 0b1010101
	push 10
	loadb
	loada
	jump :start
:loop
	decrementb
	jumpf :start

	push 0b00000