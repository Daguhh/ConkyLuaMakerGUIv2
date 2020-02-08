#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui

import time

from ObjectPanelClass import PreviewPanel, ChoiceButtonPanel, OptionPanel, SelectPanel, MenuButtons
from luadrawings import LuaDrawings

from interface_object_position import INTERFACE_SIZE


def main() :

    tic = time.time()
    nb_loop = 0
    show = 0

    interface_size = INTERFACE_SIZE

    pygame.init()

    pygame.display.set_caption('Quick Start')
    window_surface = pygame.display.set_mode(interface_size)
    manager = pygame_gui.UIManager(interface_size, 'themes/label_theme.json')

    background = pygame.Surface(interface_size)
    background.fill(pygame.Color('#222222'))

    # Inferface init
    menupanel = MenuButtons(manager)
    previewpanel = PreviewPanel(window_surface)
    choicepanel = ChoiceButtonPanel(window_surface, manager)
    optionpanel = OptionPanel(manager, window_surface)
    selectpanel = SelectPanel(manager, window_surface)
    mouse_display = MousePosPanel(manager)

    # Store drawings that will create lua conf file
    drawings = LuaDrawings(previewpanel.background)

    clock = pygame.time.Clock()
    is_running = True

    load_time_1 = clock.tick()

    grid_size = 5

    while is_running:
        time_delta = clock.tick(15)/1000.0
        mouse_pos = pygame.mouse.get_pos() # absolute mouse pos
        pp_mouse_pos = ((mouse_pos[0]-previewpanel.pos[0])//grid_size*grid_size,
                        (mouse_pos[1]-previewpanel.pos[1])//grid_size*grid_size,)# previewpanel relative mouse pos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == 'ui_button_pressed':

                    # create a new element
                    if event.ui_element in choicepanel.buttons :
                        # start creating an element and make it wait for input
                        drawings.create(choicepanel.get_name(event.ui_element))

                    # load or save a config
                    elif event.ui_element in menupanel.buttons :
                        if event.ui_element.text == "Load config" :
                            dct_list, name_list = menupanel.load()
                            for dct, name in zip(dct_list, name_list) :
                                drawings.create_from_dct(dct, name)
                                selectpanel.update_list([drawing.name for drawing in drawings.liste])

                        elif event.ui_element.text == "Generate luaconf" :
                            menupanel.gen_luaconf(drawings.liste)
                        #menupanel.execute(event.ui_element, drawings.liste)

                    elif event.ui_element.text == "Del" :
                        del(drawings.liste[drawings.selected_item])
                        del(selectpanel.drawing_name_list[drawings.selected_item])
                        selectpanel.update_list([drawing.name for drawing in drawings.liste])

                # Select another object with dropdown menu
                elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED :
                    optionpanel.update_lua_dct(drawings.get_dict_from_name(event.text))

                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED :

                    # edit properties manually with entry boxes
                    if event.ui_element in optionpanel.entrys :
                        name, new_value = optionpanel.get_new_entry(event.ui_element)
                        drawings.liste[drawings.selected_item].set_dct_item_from_lua({name:new_value})

                    # give/re name a drawing
                    elif event.ui_element == selectpanel.new_name_entry_box :
                        new_name = selectpanel.new_name_entry_box.get_text()
                        drawings.liste[drawings.selected_item].name = new_name
                        selectpanel.current_selection = new_name
                        selectpanel.update_list([drawing.name for drawing in drawings.liste])
                        selectpanel.new_name_entry_box.set_text("Enter new name")

                    # change grid_size for the object
                    elif event.ui_element == selectpanel.grid_step_entry :
                        grid_step = int(selectpanel.grid_step_entry.text)
                        selectpanel.grid_step_entry.set_text('enter an int')
                        drawings.liste[drawings.selected_item].grid_step = grid_step


            # Preview panel left click event
            if left_click(event) and previewpanel.rect.collidepoint(mouse_pos) :

                # Get events position and draw object there
                if drawings.buf.waiting_inputs :
                    drawings.buf.add_input(pp_mouse_pos) # store mouse position in a buffer
                    if not drawings.buf.waiting_inputs : # and buffer is non empty :
                        drawings.draw_from_buffer() # draw object
                        drawings.selected_item = -1
                        optionpanel.update_lua_dct(drawings.liste[-1].get_lua_dct())
                        selectpanel.current_selection = drawings.liste[-1].name
                        selectpanel.update_list([drawing.name for drawing in drawings.liste])

                # Or select/Deselect Object to make it move
                elif drawings.liste : # if an object exist
                    if drawings.an_object_is_moving : # stop moving at click
                        drawings.liste[drawings.selected_item].is_moving = False
                        #for drawing in drawings.liste :
                        if 1 :
                            drawings.an_object_is_moving = False
                            #drawing.is_moving = False
                    else : # click on object => start moving
                        for i, drawing in enumerate(drawings.liste) :
                            test_pos = (pp_mouse_pos[0]-drawing.pos[0],
                                        pp_mouse_pos[1]-drawing.pos[1]) # relatiive object rect position
                            if 1 :
                                if drawing.surface.get_rect().collidepoint(test_pos) : # in object rect
                                    if drawing.mask.get_at(test_pos) == True : # and in  non transparent area
                                        drawings.selected_item = i
                                        mouse_pos_start = mouse_pos
                                        drawing_pos_start = drawing.pos
                                        drawing.is_moving = True
                                        drawings.an_object_is_moving = True
                                        selectpanel.set_select_item(drawing.name)
                                        optionpanel.update_lua_dct(drawing.get_lua_dct())
                                        break

            # move object (follow mouse)
            if drawings.an_object_is_moving :
                for drawing in drawings.liste :
                    if drawing.is_moving :
                        drawing.pos = (drawing_pos_start[0] + (mouse_pos[0]-mouse_pos_start[0]),
                                   drawing_pos_start[1] + (mouse_pos[1]-mouse_pos_start[1]))
                        drawing.update()
                        optionpanel.update_position(drawing.get_lua_dct())

            mouse_display.update(pp_mouse_pos)

            manager.process_events(event)
        toc = time.time() - tic
        nb_loop += 1
        show += 1
        if show > 100 :
            show = 0
            average = toc*10
            tic = time.time()
            print("mean loop time = {:6.4}ms".format(average))

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        previewpanel.blit()
        previewpanel.clear()
        optionpanel.blit()
        for drawing in drawings.liste :
            drawing.blit()

        manager.draw_ui(window_surface)
        pygame.display.update()

def left_click(event) :
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
        return True
    else :
        return False

class MousePosPanel:
    def __init__(self, manager):

        rect = pygame.Rect((380,560),(240,25))
        self.label=pygame_gui.elements.UILabel(
                relative_rect = rect,
                text="mouse_pos",
                manager = manager)

#        rect = pygame.Rect((380,590),(120,25))
#        self.is_on=pygame_gui.elements.UILabel(
#                relative_rect = rect,
#                text="grid size",
#                manager = manager)
#
#        rect = pygame.Rect((500,590),(120,25))
#        self.grid_step_entry = pygame_gui.elements.UITextEntryLine(
#                relative_rect = pygame.Rect(rect),
#                manager = manager)
#
    def update(self,mouse_pos) :
        self.label.set_text('mouse position = {}'.format(mouse_pos))

    def show_is_on(self,on) :
        self.is_on.set_text(on)

main()

