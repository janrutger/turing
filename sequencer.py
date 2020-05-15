# de sequencer is verantwoordelijk dat de tapecommander gevoed wordt met de juiste tape commando´s
# als input gebruikt de sequencer het Commando en de huidige tape waardes
#
# de sequencer haalt de de state informatie van het Commando op (LDA)
# Zoekt binnen LDA naar de startstate S0 en haalt de microcode van de state (S0) op
#
# binnen de microcode wordt de huidige tapewaarde opgezocht, en  die wijst naar <nieuwe waardes><move> en volgende state (S1)
# na het uitvoeren van de microcode zijn de <nieuwe waardes> de <huidige waardes> geworden en wordt de actie herhaald
#
# Zoek binnen LDA naar state S1, haal de microcode op, zoek naar de <huidige waarde> voer de microcode uit, bepaal de volgende state.
# Herthaal dit tot de volgende stae de halt state is (H), (breng de heads terug naar default uitgangspositie) en de sequencer is klaar.
#
#
#import tapecommander as tc

class Sequencer():
    pass
