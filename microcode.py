library = {}

def loadlibrary():

    library["_LDA"] =   (
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "HALT")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "START"))
    )

    library["_ADD"] =   ( 
        ("STadd", {"ST":"1", "Rb":"_"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "START")),
        ("STadd", {"ST":"1", "Rb":"1"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "START")),
        ("STadd", {"ST":"1", "Rb":"0"}, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "DONE"))
    )

    return(library)


