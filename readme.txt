ConkyLuaMakerGUIv2

A python tkinter GUI to create a Lua conf file for fisadev/conky-draw

written in python3 using : 
    - matplotlib 
    - tkinter 
    - numpy

working on linux on 1980*1600 screen

Usage :

    Create new object :
        - just click on objects of left panel to create a new LUA objects
        - then click on the graph to create new object at the wanted position 
        (2 click for ring and bar, for respectively center/radius and start/end)
        
    Select object :
        in the "object" left panel, select an item in list you can then
            - delete it or 
            - rename buy filling entrybox and click on rename

    Edit property :
        - you can drag figure to a new position (shift + mouse)
        - you change change figure size (ctrl + mouse)
        - you can edit manually and click on "valide"

    Create Lua configuration file :
        - just hit save and generate
        - you can also save your canfiguration and load it later


    Notes :
        I'm still learing python, the main aim of this project is for me to familiarise with python and GUI, so, code looks quite ugly, 
        You have to not click everywhere because script don't handle exception and can be broken easily,
        so you have to keep all ' and { or 0x of the properties if you don't want to go back to the start
        hope you can create a conf file with not much problems, but it works : 
        just check "pythonGUI_conkypreview.png" that show the GUI and "Conky_created.png" that show conky running with config file


New version and bugs :
    - add other objects from conky-draw by fisadev
    - can now draw and resize object (buq : once you start editing manually you can't do it anymore)
    - ellipse not working
