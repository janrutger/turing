speed 2



push 3
push 9

loada
testz
jumpt :done
ex
loada
testz
jumpt :done

:while
    teste
    jumpt :done

    testg
    jumpf :Asmaller
    storeb
    storea
    storeb
    jump :subtract
:Asmaller
    storea
    storeb
    storea

:subtract
    clra
    clrb
    sub
    ex
    loadb
    jump :while



:endWhile
    halt

:done
    storea
    prt
    halt