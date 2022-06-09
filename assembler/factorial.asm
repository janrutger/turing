speed 1

push 1
push 8
speed 1
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
    #clrb
    push 0
    loadb

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

    clra
    storeb
    abs
    storea
    prt


    halt