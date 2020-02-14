# ConkyLuaMakerGUIv2

### Purpose 
This is a python interactive interface to create a Lua configuration file for (the amazing) https://github.com/fisadev/conky-draw. 

### Functionnalities :
1. all conky-draw "shapes" are supported, 
      * draw them with a few mouse button hit
      * move them, resize them with mouse, change their properties with entries boxes 
      * delete them
2. generate and reload your configuration file in one button hit
3. place objects on a resizable magnetic grid (kind of)
4. easily (re)find your drawings : give them a name, use the dropdown menu or grab them with mouse

### Example
![alt text](Example/Screenshot_2.png)


### How to run it ?
It use python3 and you need to install few requirements :

  ```bash
  pip3 install -r requirements.txt
  ```
will install  : 
  - pygame (pygame.draw)
  - pygame-gui

then just run
  ```bash
  python3 conky_lua_maker_main.py
  ```
> developped and tested on debian only



### Usage :

    1. Create a new object (ring graph, bar graph, text) :
        - hit a button on the left panel
        - programm now wait for an input on the preview area to start drawing
      
          => then, you should see the dropdown list and the properties list update (on the right panel)
             you can repeat the step many times as you want
    
    2.1) Select an object :
      Selecting an object means that : 
               * its name will appear on the dropdown list button
               * its properties will be displayed on the property list panel
               * the delete button will delete it.
               
      There is 3 ways to select an object :
            * a newly created object is automaticaly selected 
            * an preview panel with left mouse button hit
            * with the dropdown menu (top right of the interface)
    
    2.2) Edit object properties (right panel) :
      to modify a drawing property, you can :
          * change a value in the property list and hit enter
          * grab an object on the preview panel :
               left_ctrl + left mouse button = move
               left_shift + left mouse button = resize
               
    2.3 Other properties and interactions :
          * **del** button will delete selecteed graph (can't be undone)
          * all drawing have an intrinsic "grid size" value, this value (in pixel) is the size of the "magnetic grid", it can be changed with the slider, any new created graph will take as grid size the slider value a the moment of creation. As it is an intrinsic value, next time you select the object, no matter what you've done in between, grid will come back to it's resolution value. 

    3) Saving and Loading configuration files :
      On the top bar of the interface you get some menu buttons (no a lot yet, I know) :
        - "Generate Lua Conf" button will create the configuration file : "conky_draw_config.lua" needed in fisadev/conky-draw project 
        - "Load" will read this same file and create a preview from it, that you can continue tu edit it later.
        - "?" will display a little reminder on how the gui works
      

    Notes :
        I'm still learing python, the main aim of this project is for me to familiarise with python and GUI, so, code looks quite ugly, 
        Script don't handle exception and can be broken easily (take care of value, don't try to much exotic things),
        so you have to keep all ' and { or 0x of the properties if you don't want to go back to the start
        hope you can create a conf file with not much problems, but it works : 
        
        I've recently change code and dependancy from matplotlib to pygame,
        code now running better, exception are still not handled but, you can save your work and load it more easily now, 
        so you don't have to restart from the start each time you find a bug. 
        graph are also more accurate, and the preview looks more like it will be displayed by the conky

