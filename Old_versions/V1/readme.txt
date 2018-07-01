ConkyLuaMakerGUIv2

A python tkinter GUI to create a Lua conf file for fisadev/conky-draw

written in python3 using : 
    - matplotlib 
    - tkinter 
    - numpy

working on linux
preview : "pythonGUI_conkypreview.png" that show the GUI
          "Conky_created.png" that show conky running with config file

Usage :
    Run script :
        just put "create_lua_conf_v5.py" and "LuaObjectClass" in the same folder and run "create_lua_conf_v6.py"
        
    Create new object :
        - just click on objects of left panel to create a new LUA objects
        - then click on the graph to create new object at the wanted position 
        (2 click for ring and bar, for respectively center/radius and start/end)
        
    Select object :
        in the "object" right panel, select an item in list you can then
            - delete it 
            - duplicate it
            - rename buy filling entrybox and click on rename

    Edit property :
        - you can drag figure to a new position
        - you can edit manually and click on "valide" (please keep all ' , # and } and others...

    Create Lua configuration file :
        - Menu : save : save your work in "Lua_conf_save.pkl"
                 load : load "Lua_conf_save.pkl"
                 save and generate : save your work and generate the LUA configuration file in "conky_draw_config.lua"


Last update :
    - add load/save
    - add duplicate button
    - some code cleaning 
    - add an example : put in "lua_conf_save.pkl" the same folder as "create_lua_conf_v6.py" and click on "fichier", then "load" 
    
Notes :
        I'm still learning python, the main aim of this project is for me to familiarise with python and GUI, 
        so, code looks quite ugly, 
        You have to not click everywhere because script don't handle exception and can be broken easily,
        so you have to keep all ' and { or 0x of the properties if you don't want to go back to the start
        hope you can create a conf file with not much problems, but it works : 
        just check : 
            - "pythonGUI_conkypreview.png" that show the GUI and 
            - "Conky_created.png" that show conky running with config file
        
        
        
hope you enjoy =)
        
        
        
        
