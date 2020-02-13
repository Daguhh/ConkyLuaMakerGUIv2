#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui
import time

from interfaceclasses import PreviewPanel, ChoiceButtonPanel, OptionPanel,\
                             SelectPanel, MenuButtons, INTERFACE_SIZE
from luadrawings import LuaDrawings


def main() :

    pygame.init()

    pygame.display.set_caption('ConkyLuaMakerGui')
    window_surface = pygame.display.set_mode(INTERFACE_SIZE)
    manager = pygame_gui.UIManager(INTERFACE_SIZE, 'themes/label_theme.json')

    background = pygame.Surface(INTERFACE_SIZE)
    background.fill(pygame.Color('#222222'))
    window_surface.blit(background, (0, 0))

    # Inferface init
    menupanel = MenuButtons(manager)
    previewpanel = PreviewPanel(window_surface, manager)
    choicepanel = ChoiceButtonPanel(window_surface, manager)
    optionpanel = OptionPanel(manager, window_surface)
    selectpanel = SelectPanel(manager, window_surface)

    # Store drawings that will create lua conf file
    drawings = LuaDrawings(previewpanel.background)

    clock = pygame.time.Clock()
    timer = Timer()

    update_graph = 2
    is_running = True
    while is_running:
        time_delta = clock.tick(15)/1000.0
        mouse_pos = pygame.mouse.get_pos() # absolute mouse pos
        pp_mouse_pos = ((mouse_pos[0]-previewpanel.pos[0]),
                        (mouse_pos[1]-previewpanel.pos[1]))
        previewpanel.mouse_pos = mouse_pos
        keys = pygame.key.get_pressed()

        timer.print_loop_time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.USEREVENT:

                update_graph = 2

                if event.user_type == 'ui_button_pressed':

                    if event.ui_element in choicepanel.buttons :
                        ID = choicepanel.get_name(event.ui_element)
                        drawings.create(ID)

                    elif event.ui_element.text == "Load config" :
                        dct_list = menupanel.load()
                        for ID, dct in dct_list.items() :
                            drawings.create_from_dct(dct, ID)
                            selectpanel.update_list(list(drawings.objects.keys()))

                    elif event.ui_element.text == "Generate luaconf" :
                        menupanel.gen_luaconf(drawings.objects)

                    elif event.ui_element.text == "?" :
                        menupanel.display_help()

                    elif event.ui_element.text == "Del" :
                        del(drawings.selected_draw)
                        selectpanel.drawing_name_list.remove(drawings.selected_item)
                        selectpanel.update_list(list(drawings.objects.keys()))

                    elif previewpanel.grid_size_as_changed() :
                        if drawings.objects :
                            drawings.selected_draw.grid_step = previewpanel.grid_size

                elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED :
                    drawings.selected_item_ID = event.text
                    optionpanel.update_lua_dct(drawings.selected_draw.get_lua_dct())

                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED :
                    if event.ui_element in optionpanel.entrys :
                        name, new_value = optionpanel.get_new_entry(event.ui_element)
                        drawings.selected_draw.set_dct_item_from_lua({name:new_value})
                        update_graph = 2

                    elif event.ui_element == selectpanel.new_name_entry_box :
                        new_name = selectpanel.new_name_entry_box.get_text()
                        drawings.objects[new_name] = drawings.objects.pop(drawings.selected_item_ID)
                        selectpanel.current_selection = new_name
                        selectpanel.update_list(list(drawings.objects.keys()))
                        selectpanel.new_name_entry_box.set_text("Rename")

                elif event.user_type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED :
                    menupanel.display_link(event.link_target)

            elif left_click(event)\
                and previewpanel.rect.collidepoint(mouse_pos) :

                update_graph = 2
                if drawings.buf.waiting_inputs :
                    drawings.buf.add_input(previewpanel.mouse_pos) # store mouse position in a buffer
                    if not drawings.buf.waiting_inputs : # and buffer is non empty :
                        drawings.draw_from_buffer() # draw object
                        drawings.selected_item_ID = list(drawings.objects.keys())[-1]
                        optionpanel.update_lua_dct(drawings.selected_draw.get_lua_dct())
                        selectpanel.current_selection = drawings.selected_item_ID
                        selectpanel.update_list(list(drawings.objects.keys()))
                        drawings.selected_draw.grid_step = previewpanel.grid_size

                elif drawings.objects : # if an object exist
                    if drawings.an_object_is_moving : # stop moving at click
                        drawings.an_object_is_moving = False

                    elif drawings.an_object_is_resizing :
                        drawings.an_object_is_resizing = False

                    else : # click on object => start moving
                        for ID, drawing in drawings.objects.items() :
                            test_pos = (int(pp_mouse_pos[0]-drawing.pos[0]),
                                        int(pp_mouse_pos[1]-drawing.pos[1]))
                            if drawing.surface.get_rect().collidepoint(test_pos) :
                                if drawing.mask.get_at(test_pos) == True :
                                    drawings.selected_item_ID = ID
                                    selectpanel.set_select_item(ID)
                                    optionpanel.update_lua_dct(drawing.get_lua_dct())
                                    previewpanel.grid_size = drawing.grid_step
                                    if keys[pygame.K_LCTRL] :
                                        mouse_pos_start = mouse_pos
                                        drawing_pos_start = drawing.pos
                                        drawings.an_object_is_moving = True
                                        break
                                    elif keys[pygame.K_LSHIFT] :
                                        mouse_pos_start = previewpanel.mouse_pos
                                        drawings.an_object_is_resizing = True
                                        break


            if drawings.buf.waiting_inputs\
                    and previewpanel.rect.collidepoint(mouse_pos) :

                drawings.preview_from_buffer(previewpanel.mouse_pos)
                update_graph = 2

            elif drawings.an_object_is_moving :
                drawings.selected_draw.pos = (
                    drawing_pos_start[0] + (mouse_pos[0]-mouse_pos_start[0]),
                    drawing_pos_start[1] + (mouse_pos[1]-mouse_pos_start[1])
                )
                optionpanel.update_position(drawings.selected_draw.get_lua_dct())
                update_graph = 2

            elif drawings.an_object_is_resizing :
                drawings.selected_draw.resize(previewpanel.mouse_pos)
                optionpanel.update_size(drawings.selected_draw.get_lua_dct())
                update_graph = 2

            manager.process_events(event)
        manager.update(time_delta)

        if update_graph > 0   :
            update_graph -= 1
            window_surface.blit(background, (0, 0))
            previewpanel.blit()
            previewpanel.clear()
            #optionpanel.blit()
            for name, drawing in drawings.objects.items() :
                drawing.blit()
            if drawings.buf.input_remaning == 1 :
                try :
                    drawings.buf.drawing.blit()
                except :
                    print('thickness is bigger than size :\n    =>  enlarge your draw')

        manager.draw_ui(window_surface)
        pygame.display.update()


def left_click(event) :
    return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
#    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
#        return True
#    else :
#        return False

class Timer():
    def __init__(self):
        self.tic = time.time()
        self.nb_loop = 0
        self.loop_threshold = 200

    def print_loop_time(self) :

        self.nb_loop += 1
        if self.nb_loop >= self.loop_threshold :
            toc = time.time() - self.tic
            loop_time_average = toc*1000/self.nb_loop
            self.nb_loop = 0
            self.tic = time.time()
            print("mean loop time = {:4.2f}ms".format(loop_time_average))

main()

