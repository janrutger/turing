speed 1

push 1
push 16
speed 0
multi

:loop
    storeb
    #clrb
    push 0
    loadb

    ex
    decb
    jumpt :halt

    storeb
    clrb

    multi

jump :loop

:halt
    speed 1
    loadb
    storeb
    prt

    storeb
    bc
    storea
    prt


    halt