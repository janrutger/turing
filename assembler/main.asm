@main
push 13

call @factorial

loadb
storeb
prt

storeb
push 5
call @modulo

halt