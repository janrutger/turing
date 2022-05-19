speed 1

push 1
push 1023

multi

:loop
    storeb
    clrb

    ex
    decb
    jumpt :halt

    storeb
    clrb

    multi

jump :loop

:halt
    halt