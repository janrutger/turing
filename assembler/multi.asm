speed 3

push 1
push 5

multi

#halt

:loop
    storea
    storeb
    push 0
    loadb


    multi
jump :loop

halt