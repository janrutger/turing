speed 4

push 0
storem $count

push 185
push 11

loada
loadb

testz 
jumpt :DivZeroError

#ex

:while
    testg
    jumpt :done
   
:do  
    #ex
    storea
    storeb
    storea
    clra
    clrb
    sub
    loadm $count
    push 1
    loada
    add
    storea
    storem $count

    #ex
    #loadb
    loada

    jump :while

:done
    
    teste
    jumpt :do
    loadm $count
    loada
    #ex

    storeb
    storea
    prt
    prt

    halt

:DivZeroError
    clra
    clrb
    halt


