library = {}

def loadlibrary():

    library["MULTI"] = (
        ("START", {"ST":"1", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RA":"0", "RB":"0"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RA":"0", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RA":"1", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RA":"1", "RB":"0"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),


        ("START", {"ST":"0", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RA":"0", "RB":"0"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RA":"0", "RB":"_"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RA":"1", "RB":"_"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "START")),

        ("START", {"ST":"#", "RA":"_", "RB":"_"}, ({"ST":"#", "RA":"_", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),

        ("retA", {"ST":"#", "RA":"1", "RB":"0"}, ({"ST":"#", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"#", "RA":"0", "RB":"0"}, ({"ST":"#", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"#", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"_", "RB":"_"}, {"ST":"R", "RA":"R", "RB":"R"}, "multi")),

        ("retA", {"ST":"_", "RA":"1", "RB":"1"}, ({"ST":"_", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"_", "RA":"1", "RB":"0"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"_", "RA":"0", "RB":"0"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"_", "RA":"1", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"_", "RA":"0", "RB":"_"}, ({"ST":"_", "RA":"0", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")),
        ("retA", {"ST":"_", "RA":"0", "RB":"1"}, ({"ST":"_", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"L"}, "retA")), 
        ("retA", {"ST":"_", "RA":"_", "RB":"1"}, ({"ST":"_", "RA":"_", "RB":"1"}, {"ST":"R", "RA":"R", "RB":"R"}, "multi")),
        ("retA", {"ST":"_", "RA":"_", "RB":"0"}, ({"ST":"_", "RA":"_", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "multi")),
        ("retA", {"ST":"_", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"_", "RB":"0"}, {"ST":"R", "RA":"R", "RB":"R"}, "multi")),

        ("multi", {"ST":"1", "RA":"0", "RB":"0"}, ({"ST":"1", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),
        ("multi", {"ST":"1", "RA":"0", "RB":"_"}, ({"ST":"1", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),
        ("multi", {"ST":"1", "RA":"1", "RB":"0"}, ({"ST":"1", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),
        ("multi", {"ST":"1", "RA":"1", "RB":"_"}, ({"ST":"1", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),
        ("multi", {"ST":"1", "RA":"0", "RB":"1"}, ({"ST":"1", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),
        ("multi", {"ST":"1", "RA":"1", "RB":"1"}, ({"ST":"1", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "addA")),

        ("multi", {"ST":"0", "RA":"0", "RB":"_"}, ({"ST":"0", "RA":"0", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),
        ("multi", {"ST":"0", "RA":"1", "RB":"_"}, ({"ST":"0", "RA":"1", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),
        ("multi", {"ST":"0", "RA":"0", "RB":"0"}, ({"ST":"0", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),
        ("multi", {"ST":"0", "RA":"1", "RB":"0"}, ({"ST":"0", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),
        ("multi", {"ST":"0", "RA":"0", "RB":"1"}, ({"ST":"0", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),
        ("multi", {"ST":"0", "RA":"1", "RB":"1"}, ({"ST":"0", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "addZero")),

        ("multi", {"ST":"#", "RA":"0", "RB":"_"}, ({"ST":"#", "RA":"0", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"_", "RB":"_"}, ({"ST":"#", "RA":"_", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"1", "RB":"_"}, ({"ST":"#", "RA":"1", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"0", "RB":"0"}, ({"ST":"#", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"1", "RB":"0"}, ({"ST":"#", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"0", "RB":"1"}, ({"ST":"#", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),
        ("multi", {"ST":"#", "RA":"1", "RB":"1"}, ({"ST":"#", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "end")),

        ("addA", {"ST":"1", "RA":"0", "RB":"0"}, ({"ST":"1", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("addA", {"ST":"1", "RA":"0", "RB":"_"}, ({"ST":"1", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("addA", {"ST":"1", "RA":"0", "RB":"1"}, ({"ST":"1", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),

        ("addA", {"ST":"1", "RA":"1", "RB":"0"}, ({"ST":"1", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("addA", {"ST":"1", "RA":"1", "RB":"_"}, ({"ST":"1", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("addA", {"ST":"1", "RA":"1", "RB":"1"}, ({"ST":"1", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "carry")),

        ("addA", {"ST":"1", "RA":"_", "RB":"1"}, ({"ST":"_", "RA":"_", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"S"}, "retA")),
        ("addA", {"ST":"1", "RA":"_", "RB":"0"}, ({"ST":"_", "RA":"_", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"S"}, "retA")),
        ("addA", {"ST":"1", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"_", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"S"}, "retA")),

        ("carry", {"ST":"1", "RA":"1", "RB":"1"}, ({"ST":"1", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "carry")),
        ("carry", {"ST":"1", "RA":"1", "RB":"0"}, ({"ST":"1", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "carry")),
        ("carry", {"ST":"1", "RA":"1", "RB":"_"}, ({"ST":"1", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "carry")),
        ("carry", {"ST":"1", "RA":"0", "RB":"1"}, ({"ST":"1", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"R", "RB":"R"}, "carry")),

        ("carry", {"ST":"1", "RA":"0", "RB":"0"}, ({"ST":"1", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("carry", {"ST":"1", "RA":"0", "RB":"_"}, ({"ST":"1", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"R", "RB":"R"}, "addA")),
        ("carry", {"ST":"1", "RA":"_", "RB":"0"}, ({"ST":"_", "RA":"_", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"S"}, "retA")),
        ("carry", {"ST":"1", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"_", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"S"}, "retA")), 

        ("addZero", {"ST":"0", "RA":"0", "RB":"_"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),
        ("addZero", {"ST":"0", "RA":"1", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),
        ("addZero", {"ST":"0", "RA":"0", "RB":"0"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),
        ("addZero", {"ST":"0", "RA":"1", "RB":"0"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),
        ("addZero", {"ST":"0", "RA":"1", "RB":"1"}, ({"ST":"_", "RA":"1", "RB":"1"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),
        ("addZero", {"ST":"0", "RA":"0", "RB":"1"}, ({"ST":"_", "RA":"0", "RB":"1"}, {"ST":"R", "RA":"S", "RB":"R"}, "multi")),



        ("end", {"ST":"#", "RA":"_", "RB":"_"}, ({"ST":"_", "RA":"_", "RB":"_"}, {"ST":"S", "RA":"R", "RB":"R"}, "HALT")),
        ("end", {"ST":"#", "RA":"_", "RB":"1"}, ({"ST":"#", "RA":"_", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"_", "RB":"0"}, ({"ST":"#", "RA":"_", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"1", "RB":"1"}, ({"ST":"#", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"1", "RB":"0"}, ({"ST":"#", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"1", "RB":"_"}, ({"ST":"#", "RA":"1", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")), #niuw
        ("end", {"ST":"#", "RA":"0", "RB":"1"}, ({"ST":"#", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"0", "RB":"0"}, ({"ST":"#", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")),
        ("end", {"ST":"#", "RA":"0", "RB":"_"}, ({"ST":"#", "RA":"0", "RB":"_"}, {"ST":"S", "RA":"L", "RB":"L"}, "end")), #Write RB _ ipv 0



        # ("end", {"ST":"#", "RA":"1", "RB":"_"}, ({"ST":"_", "RA":"1", "RB":"_"}, {"ST":"S", "RA":"S", "RB":"S"}, "HALT")),
        # ("end", {"ST":"#", "RA":"0", "RB":"0"}, ({"ST":"_", "RA":"0", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "HALT")),
        # ("end", {"ST":"#", "RA":"1", "RB":"0"}, ({"ST":"_", "RA":"1", "RB":"0"}, {"ST":"S", "RA":"S", "RB":"S"}, "HALT")),
        # ("end", {"ST":"#", "RA":"0", "RB":"1"}, ({"ST":"_", "RA":"0", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "HALT")),
        # ("end", {"ST":"#", "RA":"1", "RB":"1"}, ({"ST":"_", "RA":"1", "RB":"1"}, {"ST":"S", "RA":"S", "RB":"S"}, "HALT")),


    )

    library["RWD"] = (
        ("START",  {"ST":"_"}, ({"ST":"_"}, {"ST":"R"}, "HALT")),
        ("START",  {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("START",  {"ST":"0"}, ({"ST":"0"}, {"ST":"L"}, "START")),
    )

    library["ABS"] = (
        ("START", {"ST":"_", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"S", "RA":"S"}, "HALT")),
        ("START", {"ST":"_", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"S", "RA":"S"}, "HALT")),

        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"S"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"S"}, "START")),

        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"S"}, "START")),
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"S"}, "START")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"S", "RA":"R"}, "ADD")),

        ("ADD", {"ST":"_", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"S", "RA":"L"}, "REWIND")),
        ("ADD", {"ST":"_", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"S", "RA":"L"}, "REWIND")),
        ("ADD", {"ST":"_", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"S", "RA":"R"}, "ADD")),

        ("REWIND", {"ST":"_", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"S", "RA":"L"}, "REWIND")),
        ("REWIND", {"ST":"_", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"S", "RA":"L"}, "REWIND")),
        ("REWIND", {"ST":"_", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "START")),
    )


    library["2S-BB"] = (
        ("START", {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "B")),
        ("START", {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "B")),
        ("B"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("B"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"R"}, "HALT")),
    )

    library["4S-BB"] = (
        ("START", {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "B")),
        ("START", {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "B")),
        ("START", {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "B")),

        ("B"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("B"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("B"    , {"ST":"1"}, ({"ST":"0"}, {"ST":"L"}, "C")),

        ("C"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "HALT")),
        ("C"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "HALT")),
        ("C"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "D")),

        ("D"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "D")),
        ("D"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "D")),
        ("D"    , {"ST":"1"}, ({"ST":"0"}, {"ST":"R"}, "START")),
    )

    library["5S-BB"] = (
        ("START", {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "B")),
        ("START", {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "B")),
        ("START", {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "START")),

        ("B"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "C")),
        ("B"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "C")),
        ("B"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"R"}, "B")),

        ("C"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("C"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("C"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"R"}, "D")),

        ("D"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("D"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("D"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"R"}, "E")),

        ("E"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "HALT")),
        ("E"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "HALT")),
        ("E"    , {"ST":"1"}, ({"ST":"0"}, {"ST":"R"}, "C")),
        
    )

    library["5S-BBv2"] = (
        ("START", {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "B")),
        ("START", {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "B")),
        ("START", {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "C")),

        ("B"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "C")),
        ("B"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "C")),
        ("B"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"R"}, "B")),

        ("C"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "D")),
        ("C"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "D")),
        ("C"    , {"ST":"1"}, ({"ST":"0"}, {"ST":"L"}, "E")),

        ("D"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("D"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"L"}, "START")),
        ("D"    , {"ST":"1"}, ({"ST":"1"}, {"ST":"L"}, "D")),

        ("E"    , {"ST":"_"}, ({"ST":"1"}, {"ST":"R"}, "HALT")),
        ("E"    , {"ST":"0"}, ({"ST":"1"}, {"ST":"R"}, "HALT")),
        ("E"    , {"ST":"1"}, ({"ST":"0"}, {"ST":"L"}, "START")),
    )


    library["STA"] =    (
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"1", "RA":"1"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"0", "RA":"1"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"1", "RA":"0"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"0", "RA":"0"}, {"ST":"L", "RA":"S"}, "START")),
        ("START", {"ST":"_", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"S"}, "toend")),
        ("START", {"ST":"_", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"S"}, "toend")),

        ("toend", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "toend")),
        ("toend", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "toend")),        
        ("toend", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"L", "RA":"L"}, "write")),

        ("write", {"ST":"_", "RA":"1"}, ({"ST":"1", "RA":"1"}, {"ST":"L", "RA":"L"}, "write")),
        ("write", {"ST":"_", "RA":"0"}, ({"ST":"0", "RA":"0"}, {"ST":"L", "RA":"L"}, "write")),
        ("write", {"ST":"_", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT")),
    )

    library["STB"] =    (
        ("START", {"ST":"1", "RB":"1"}, ({"ST":"1", "RB":"1"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"0", "RB":"1"}, ({"ST":"0", "RB":"1"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"1", "RB":"0"}, ({"ST":"1", "RB":"0"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"0", "RB":"0"}, ({"ST":"0", "RB":"0"}, {"ST":"L", "RB":"S"}, "START")),
        ("START", {"ST":"_", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"S"}, "toend")),
        ("START", {"ST":"_", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"S"}, "toend")),

        ("toend", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"R"}, "toend")),
        ("toend", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"R"}, "toend")),        
        ("toend", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"L", "RB":"L"}, "write")),

        ("write", {"ST":"_", "RB":"1"}, ({"ST":"1", "RB":"1"}, {"ST":"L", "RB":"L"}, "write")),
        ("write", {"ST":"_", "RB":"0"}, ({"ST":"0", "RB":"0"}, {"ST":"L", "RB":"L"}, "write")),
        ("write", {"ST":"_", "RB":"_"}, ({"ST":"_", "RB":"_"}, {"ST":"R", "RB":"R"}, "HALT")),
    )

    library["DECB"] =  (
        ("START", {'RB': '1', "S": "0"}, ({"RB":"1", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '1', "S": "1"}, ({"RB":"1", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '0', "S": "0"}, ({"RB":"0", "S":"_"}, {"RB":"S", "S":"S"}, "START")),
        ("START", {'RB': '0', "S": "1"}, ({"RB":"0", "S":"_"}, {"RB":"S", "S":"S"}, "START")),

        ("START", {'RB': '1', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("START", {'RB': '0', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "leen")),

        ("leen",  {'RB': '1', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("leen",  {'RB': '0', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "leen")),
        ("leen",  {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "isnul")),

        ("eind",  {'RB': '0', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("eind",  {'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"R", "S":"S"}, "eind")),
        ("eind",  {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "terug")),

        ("terug", {'RB': '0', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "terug")),
        ("terug", {'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug", {'RB': '_', "S": "_"}, ({"RB":"_", "S":"_"}, {"RB":"L", "S":"S"}, "isnul")),

        ("terug1",{'RB': '1', "S": "_"}, ({"RB":"1", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug1",{'RB': '0', "S": "_"}, ({"RB":"0", "S":"_"}, {"RB":"L", "S":"S"}, "terug1")),
        ("terug1",{'RB': '_', "S": "_"}, ({"RB":"_", "S":"0"}, {"RB":"R", "S":"S"}, "HALT")),

        ("isnul", {'RB': '_', "S": "_"}, ({"RB":"0", "S":"1"}, {"RB":"S", "S":"S"}, "HALT")),
        ("isnul", {'RB': '1', "S": "_"}, ({"RB":"0", "S":"1"}, {"RB":"S", "S":"S"}, "HALT"))
    )

    library["ADD"] =    (
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("START", {"ST":"_", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"S", "RA":"S"}, "HALT")),
        ("START", {"ST":"_", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"S", "RA":"S"}, "HALT")),
          
        ("ADD",   {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "RWD-A")),
        ("ADD",   {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "RWD-A")), 
        ("ADD",   {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"0", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD",   {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD",   {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"S"}, "RWD-A")),
          
        ("ADD1",  {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
        ("ADD1",  {'ST':"0", 'RA':"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "ADD")),
          
        ("ADD1",  {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "ADD1")),
        ("ADD1",  {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "ADD")),
        ("ADD1",  {'ST':'#', 'RA':'0'}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"R"}, "ADD")),
          
        ("RWD-A", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT"))
    )

    library["LDA"] =    (
        ("START", {"ST":"1", "RA":"_"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"1", "RA":"1"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"1", "RA":"0"}, ({"ST":"_", "RA":"1"}, {"ST":"R", "RA":"R"}, "START")),

        ("START", {"ST":"0", "RA":"_"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"0", "RA":"1"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
        ("START", {"ST":"0", "RA":"0"}, ({"ST":"_", "RA":"0"}, {"ST":"R", "RA":"R"}, "START")),
          
        ("START", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "START")),
        ("START", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "START")),
        ("START", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"R"}, "RWD-A")),
          
        ("RWD-A", {"ST":"#", "RA":"_"}, ({"ST":"#", "RA":"_"}, {"ST":"S", "RA":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RA":"1"}, ({"ST":"#", "RA":"1"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"0"}, ({"ST":"#", "RA":"0"}, {"ST":"S", "RA":"L"}, "loop")),
        ("loop" , {"ST":"#", "RA":"_"}, ({"ST":"_", "RA":"_"}, {"ST":"R", "RA":"R"}, "HALT"))
    )

    library["LDB"] =    (
        ("START", {"ST":"1", "RB":"_"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RB":"1"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"1", "RB":"0"}, ({"ST":"_", "RB":"1"}, {"ST":"R", "RB":"R"}, "START")),

        ("START", {"ST":"0", "RB":"_"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RB":"1"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
        ("START", {"ST":"0", "RB":"0"}, ({"ST":"_", "RB":"0"}, {"ST":"R", "RB":"R"}, "START")),
          
        ("START", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "START")),
        ("START", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "START")),
        ("START", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"R"}, "RWD-A")),
          
        ("RWD-A", {"ST":"#", "RB":"_"}, ({"ST":"#", "RB":"_"}, {"ST":"S", "RB":"L"}, "RWD-A")),
        ("RWD-A", {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"L"}, "loop")),
        ("RWD-A", {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"L"}, "loop")),
          
        ("loop" , {"ST":"#", "RB":"1"}, ({"ST":"#", "RB":"1"}, {"ST":"S", "RB":"L"}, "loop")),
        ("loop" , {"ST":"#", "RB":"0"}, ({"ST":"#", "RB":"0"}, {"ST":"S", "RB":"L"}, "loop")),
        ("loop" , {"ST":"#", "RB":"_"}, ({"ST":"_", "RB":"_"}, {"ST":"R", "RB":"R"}, "HALT"))
    )

    library["EX"] =   (
        ("START", {"RB":"_", "RA":"_"}, ({"RB":"_", "RA":"_"}, {"RB":"S", "RA":"S"}, "HALT")),

        ("START", {"RB":"1", "RA":"1"}, ({"RB":"1", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"0", "RA":"0"}, ({"RB":"0", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"1", "RA":"0"}, ({"RB":"0", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"1", "RA":"_"}, ({"RB":"_", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"0", "RA":"_"}, ({"RB":"_", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),

        ("START", {"RB":"1", "RA":"1"}, ({"RB":"1", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"0", "RA":"1"}, ({"RB":"1", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"_", "RA":"1"}, ({"RB":"1", "RA":"_"}, {"RB":"R", "RA":"R"}, "ex")),
        ("START", {"RB":"_", "RA":"0"}, ({"RB":"0", "RA":"_"}, {"RB":"R", "RA":"R"}, "ex")),

        ("ex"   , {"RB":"1", "RA":"1"}, ({"RB":"1", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"1", "RA":"0"}, ({"RB":"0", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"1", "RA":"_"}, ({"RB":"_", "RA":"1"}, {"RB":"R", "RA":"R"}, "ex")),

        ("ex"   , {"RB":"0", "RA":"0"}, ({"RB":"0", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"0", "RA":"_"}, ({"RB":"_", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"0", "RA":"1"}, ({"RB":"1", "RA":"0"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"_", "RA":"1"}, ({"RB":"1", "RA":"_"}, {"RB":"R", "RA":"R"}, "ex")),
        ("ex"   , {"RB":"_", "RA":"0"}, ({"RB":"0", "RA":"_"}, {"RB":"R", "RA":"R"}, "ex")),

        ("ex"   , {"RB":"_", "RA":"_"}, ({"RB":"_", "RA":"_"}, {"RB":"L", "RA":"L"}, "terug")),

        ("terug", {"RB":"1", "RA":"1"}, ({"RB":"1", "RA":"1"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"1", "RA":"0"}, ({"RB":"1", "RA":"0"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"1", "RA":"_"}, ({"RB":"1", "RA":"_"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"0", "RA":"_"}, ({"RB":"0", "RA":"_"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"0", "RA":"0"}, ({"RB":"0", "RA":"0"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"0", "RA":"1"}, ({"RB":"0", "RA":"1"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"_", "RA":"1"}, ({"RB":"_", "RA":"1"}, {"RB":"L", "RA":"L"}, "terug")),
        ("terug", {"RB":"_", "RA":"0"}, ({"RB":"_", "RA":"0"}, {"RB":"L", "RA":"L"}, "terug")),

        ("terug", {"RB":"_", "RA":"_"}, ({"RB":"_", "RA":"_"}, {"RB":"R", "RA":"R"}, "HALT")),
    )

    library["TSTZ"] =   (
            ("START", {"RA":"_", "S":"_"}, ({"RA":"_", "S":"_"}, {"RA":"S", "S":"S"}, "HALT")),
            ("START", {"RA":"_", "S":"1"}, ({"RA":"_", "S":"_"}, {"RA":"S", "S":"S"}, "HALT")),
            ("START", {"RA":"_", "S":"0"}, ({"RA":"_", "S":"_"}, {"RA":"S", "S":"S"}, "HALT")),

            ("START", {"RA":"0", "S":"_"}, ({"RA":"0", "S":"_"}, {"RA":"R", "S":"S"}, "isnul")),
            ("START", {"RA":"0", "S":"1"}, ({"RA":"0", "S":"_"}, {"RA":"R", "S":"S"}, "isnul")),
            ("START", {"RA":"0", "S":"0"}, ({"RA":"0", "S":"_"}, {"RA":"R", "S":"S"}, "isnul")),

            ("START", {"RA":"1", "S":"_"}, ({"RA":"1", "S":"_"}, {"RA":"R", "S":"S"}, "notnul")),
            ("START", {"RA":"1", "S":"1"}, ({"RA":"1", "S":"_"}, {"RA":"R", "S":"S"}, "notnul")),
            ("START", {"RA":"1", "S":"0"}, ({"RA":"1", "S":"_"}, {"RA":"R", "S":"S"}, "notnul")),

            ("isnul", {"RA":"1", "S":"_"}, ({"RA":"1", "S":"_"}, {"RA":"R", "S":"S"}, "notnul")),
            ("isnul", {"RA":"0", "S":"_"}, ({"RA":"0", "S":"_"}, {"RA":"R", "S":"S"}, "isnul")),
            ("isnul", {"RA":"_", "S":"_"}, ({"RA":"_", "S":"1"}, {"RA":"L", "S":"S"}, "HALT")),

            ("notnul", {"RA":"1", "S":"_"}, ({"RA":"1", "S":"0"}, {"RA":"L", "S":"S"}, "rewind")),
            ("notnul", {"RA":"0", "S":"_"}, ({"RA":"0", "S":"0"}, {"RA":"L", "S":"S"}, "rewind")),
            ("notnul", {"RA":"_", "S":"_"}, ({"RA":"_", "S":"0"}, {"RA":"L", "S":"S"}, "rewind")),

            ("rewind", {"RA":"1", "S":"0"}, ({"RA":"1", "S":"0"}, {"RA":"L", "S":"S"}, "rewind")),
            ("rewind", {"RA":"0", "S":"0"}, ({"RA":"0", "S":"0"}, {"RA":"L", "S":"S"}, "rewind")),
            ("rewind", {"RA":"_", "S":"0"}, ({"RA":"_", "S":"0"}, {"RA":"R", "S":"S"}, "HALT"))

    )

    library["TSTE"] =   (
            ("START", {"RA":"_", "RB":"_", "S":"_"}, ({"RA":"_", "RB":"_", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "HALT")),

            ("START", {"RA":"1", "RB":"1", "S":"1"}, ({"RA":"1", "RB":"1", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"1", "RB":"0", "S":"1"}, ({"RA":"1", "RB":"0", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"0", "RB":"1", "S":"1"}, ({"RA":"0", "RB":"1", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"0", "RB":"0", "S":"1"}, ({"RA":"0", "RB":"0", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),

            ("START", {"RA":"1", "RB":"1", "S":"0"}, ({"RA":"1", "RB":"1", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"1", "RB":"0", "S":"0"}, ({"RA":"1", "RB":"0", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"0", "RB":"1", "S":"0"}, ({"RA":"0", "RB":"1", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),
            ("START", {"RA":"0", "RB":"0", "S":"0"}, ({"RA":"0", "RB":"0", "S":"_"}, {"RA":"S", "RB":"S", "S":"S"}, "START")),

            ("START", {"RA":"1", "RB":"1", "S":"_"}, ({"RA":"1", "RB":"1", "S":"_"}, {"RA":"R", "RB":"R", "S":"S"}, "ISe")),
            ("START", {"RA":"0", "RB":"0", "S":"_"}, ({"RA":"0", "RB":"0", "S":"_"}, {"RA":"R", "RB":"R", "S":"S"}, "ISe")),

            ("START", {"RA":"1", "RB":"0", "S":"_"}, ({"RA":"1", "RB":"0", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("START", {"RA":"0", "RB":"1", "S":"_"}, ({"RA":"0", "RB":"1", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),

            ("ISe"  , {"RA":"1", "RB":"1", "S":"_"}, ({"RA":"1", "RB":"1", "S":"_"}, {"RA":"R", "RB":"R", "S":"S"}, "ISe")),
            ("ISe"  , {"RA":"0", "RB":"0", "S":"_"}, ({"RA":"0", "RB":"0", "S":"_"}, {"RA":"R", "RB":"R", "S":"S"}, "ISe")),

            ("ISe"  , {"RA":"1", "RB":"0", "S":"_"}, ({"RA":"1", "RB":"0", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("ISe"  , {"RA":"0", "RB":"1", "S":"_"}, ({"RA":"0", "RB":"1", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("ISe"  , {"RA":"1", "RB":"_", "S":"_"}, ({"RA":"1", "RB":"_", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("ISe"  , {"RA":"0", "RB":"_", "S":"_"}, ({"RA":"0", "RB":"_", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("ISe"  , {"RA":"_", "RB":"1", "S":"_"}, ({"RA":"_", "RB":"1", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("ISe"  , {"RA":"_", "RB":"0", "S":"_"}, ({"RA":"_", "RB":"0", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),

            ("ISe"  , {"RA":"_", "RB":"_", "S":"_"}, ({"RA":"_", "RB":"_", "S":"1"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),

            ("back" , {"RA":"1", "RB":"1", "S":"1"}, ({"RA":"1", "RB":"1", "S":"1"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"1", "RB":"1", "S":"0"}, ({"RA":"1", "RB":"1", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"1", "RB":"0", "S":"1"}, ({"RA":"1", "RB":"0", "S":"1"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"1", "RB":"0", "S":"0"}, ({"RA":"1", "RB":"0", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),

            ("back" , {"RA":"0", "RB":"0", "S":"1"}, ({"RA":"0", "RB":"0", "S":"1"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"0", "RB":"0", "S":"0"}, ({"RA":"0", "RB":"0", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"0", "RB":"1", "S":"1"}, ({"RA":"0", "RB":"1", "S":"1"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),
            ("back" , {"RA":"0", "RB":"1", "S":"0"}, ({"RA":"0", "RB":"1", "S":"0"}, {"RA":"L", "RB":"L", "S":"S"}, "back")),

            ("back" , {"RA":"_", "RB":"_", "S":"1"}, ({"RA":"_", "RB":"_", "S":"1"}, {"RA":"R", "RB":"R", "S":"S"}, "HALT")),
            ("back" , {"RA":"_", "RB":"_", "S":"0"}, ({"RA":"_", "RB":"_", "S":"0"}, {"RA":"R", "RB":"R", "S":"S"}, "HALT")),        
    )

    return(library)

