#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""

"""

import pygame
import pygame_gui
import time

from interfaceclasses import PreviewPanel, ChoiceButtonPanel, OptionPanel,\
                             SelectPanel, MenuButtons, INTERFACE_SIZE, MP_RECT
from luadrawings import LuaDrawings


class main_interface :

    def __init__(self) :

        pygame.init()

        pygame.display.set_caption('ConkyLuaMakerGui')

        self.window_surface = pygame.display.set_mode(INTERFACE_SIZE)
        self.manager = pygame_gui.UIManager(INTERFACE_SIZE, 'themes/label_theme.json')

        self.background = pygame.Surface(INTERFACE_SIZE)
        self.background.fill(pygame.Color('#222222'))
        self.window_surface.blit(self.background, (0, 0))

        # Inferface init
        self.menupanel = MenuButtons(self.manager)
        self.previewpanel = PreviewPanel(self.window_surface, self.manager)
        self.choicepanel = ChoiceButtonPanel(self.window_surface, self.manager)
        self.optionpanel = OptionPanel(self.manager, self.window_surface)
        self.selectpanel = SelectPanel(self.manager, self.window_surface)

        # Store drawings that will create lua conf file
        self.drawings = LuaDrawings(self.previewpanel.background)

        self.clock = pygame.time.Clock()
        self.timer = Timer()

        self.update_graph = 2
        self.mouse = Mouse(self.manager, self.window_surface,  self.previewpanel.rect)

    def loop(self) :
        is_running = True
        while is_running:
            time_delta = self.clock.tick(15)/1000.0

            self.keys = pygame.key.get_pressed()

            self.timer.print_loop_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                elif event.type == pygame.USEREVENT:

                    self.update_graph = 2

                    if event.user_type == 'ui_button_pressed':

                        if event.ui_element in self.choicepanel.buttons :
                            self.create_new_draw(event.ui_element)

                        elif event.ui_element.text == "Load config" :
                            self.load_conf_file()

                        elif event.ui_element.text == "Generate luaconf" :
                            self.generate_conf_file()

                        elif event.ui_element.text == "?" :
                            self.show_help()

                        elif event.ui_element.text == "Del" :
                            self.delete_selected_object()

                        elif self.previewpanel.grid_size_as_changed() :
                            self.change_grid_size()

                    elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED :
                        self.drop_down_menu_select(event.text)

                    elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED :
                        if event.ui_element in self.optionpanel.entrys :
                            self.change_selected_object_property(event.ui_element)

                        elif event.ui_element == self.selectpanel.new_name_entry_box :
                            self.rename_selected_object()

                    elif event.user_type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED :
                        self.help_box_show_new_page(event)

                elif self.mouse.on_previewpanel :
                #elif self.mouse.left_click_on_previewpanel(event) :
                    self.update_graph = 2

                    if self.mouse.left_click(event) :
                        if self.drawings.buf.waiting_inputs :
                            self.add_input_to_buffer()

                        elif self.drawings.objects : # if an object exist
                            self.toggle_object_motion()

                    elif self.drawings.buf.waiting_inputs :
                        self.dynamic_draw_preview()

                    elif self.drawings.an_object_is_moving :
                        self.move_object()

                    elif self.drawings.an_object_is_resizing :
                        self.resize_object()

                self.manager.process_events(event)
            self.manager.update(time_delta)

            if self.update_graph > 0   :

                self.update_interface()

            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

    def create_new_draw(self, ui_element) :

        ID = self.choicepanel.get_name(ui_element)
        self.drawings.create(ID)

    def load_conf_file(self) :

        dct_list = self.menupanel.load()
        for ID, dct in dct_list.items() :
            self.drawings.create_from_dct(dct, ID)
            self.selectpanel.update_list(list(self.drawings.objects.keys()))

    def generate_conf_file(self) :

        self.menupanel.gen_luaconf(self.drawings.objects)

    def show_help(self) :

        self.menupanel.display_help()

    def delete_selected_object(self) :

        del(self.drawings.objects[self.drawings.selected_item_ID])
        self.selectpanel.drawing_name_list.remove(self.drawings.selected_item_ID)
        self.selectpanel.update_list(list(self.drawings.objects.keys()))
        self.drawings.selected_item_ID = list(self.drawings.objects.keys())[-1]
        self.selectpanel.current_selection = self.drawings.selected_item_ID
        self.optionpanel.update_lua_dct(self.drawings.selected_draw.get_lua_dct())

    def change_grid_size(self) :

        if self.drawings.objects :
            self.drawings.selected_draw.grid_step = self.previewpanel.grid_size
            self.mouse.pp_grid_size = self.previewpanel.grid_size

    def drop_down_menu_select(self, ID) :

        self.drawings.selected_item_ID = ID
        self.optionpanel.update_lua_dct(self.drawings.selected_draw.get_lua_dct())
        self.previewpanel.grid_size = self.drawings.selected_draw.grid_step
        self.mouse.pp_grid_size = self.drawings.selected_draw.grid_step

    def change_selected_object_property(self, ui_element) :

        name, new_value = self.optionpanel.get_new_entry(ui_element)
        self.drawings.selected_draw.set_dct_item_from_lua({name:new_value})
        self.update_graph = 2

    def rename_selected_object(self) :

        new_name = self.selectpanel.new_name_entry_box.get_text()
        self.drawings.objects[new_name] = self.drawings.objects.pop(self.drawings.selected_item_ID)
        self.drawings.selected_item_ID = new_name
        self.selectpanel.current_selection = new_name
        self.selectpanel.update_list(list(self.drawings.objects.keys()))
        self.selectpanel.new_name_entry_box.set_text("Rename")

    def help_box_show_new_page(self, event) :

        self.menupanel.display_link(event.link_target)

    def add_input_to_buffer(self) :
        #if self.drawings.buf.waiting_inputs :

        self.drawings.buf.add_input(self.mouse.pp_grid_pos) # store mouse position in a buffer
        if not self.drawings.buf.waiting_inputs : # and buffer is non empty :
            self.drawings.draw_from_buffer() # draw object
            self.drawings.selected_item_ID = list(self.drawings.objects.keys())[-1]
            self.optionpanel.update_lua_dct(self.drawings.selected_draw.get_lua_dct())
            self.selectpanel.current_selection = self.drawings.selected_item_ID
            self.selectpanel.update_list(list(self.drawings.objects.keys()))
            self.drawings.selected_draw.grid_step = self.previewpanel.grid_size

    def toggle_object_motion(self) :

        #elif self.drawings.objects : # if an object exist

        if self.drawings.an_object_is_moving : # stop moving at click
            self.drawings.an_object_is_moving = False

        elif self.drawings.an_object_is_resizing :
            self.drawings.an_object_is_resizing = False

        else : # click on object => start moving
            for ID, drawing in self.drawings.objects.items() :
                test_pos = (int(self.mouse.pp_rel_pos[0]-drawing.pos[0]),
                            int(self.mouse.pp_rel_pos[1]-drawing.pos[1]))
                if drawing.surface.get_rect().collidepoint(test_pos) :
                    if drawing.mask.get_at(test_pos) == True :
                        self.drawings.selected_item_ID = ID
                        self.selectpanel.set_select_item(ID)
                        self.optionpanel.update_lua_dct(drawing.get_lua_dct())
                        self.previewpanel.grid_size = drawing.grid_step
                        self.mouse.pp_grid_size = drawing.grid_step
                        if self.keys[pygame.K_LCTRL] :
                            self.mouse.store_click_pos(drawing.pos)
                            self.drawings.an_object_is_moving = True
                            break
                        elif self.keys[pygame.K_LSHIFT] :
                            self.mouse.store_click_pos()
                            self.drawings.an_object_is_resizing = True
                            break

    def dynamic_draw_preview(self):

        self.drawings.preview_from_buffer(self.mouse.pp_grid_pos)
        self.update_graph = 2

    def move_object(self) :

        self.drawings.selected_draw.pos = self.mouse.displacment_since_last_click()
        self.optionpanel.update_position(self.drawings.selected_draw.get_lua_dct())
        self.update_graph = 2

    def resize_object(self) :

        self.drawings.selected_draw.resize(self.mouse.pp_grid_pos)
        self.optionpanel.update_size(self.drawings.selected_draw.get_lua_dct())
        self.update_graph = 2

    def update_interface(self) :

        self.update_graph -= 1
        self.window_surface.blit(self.background, (0, 0))
        self.previewpanel.blit()
        self.previewpanel.clear()
        #optionpanel.blit()
        for name, drawing in self.drawings.objects.items() :
            drawing.blit()
        if self.drawings.buf.input_remaning == 1 :
            try :
                self.drawings.buf.drawing.blit()
            except :
                print('thickness is bigger than size :\n    =>  enlarge your draw')

class Mouse :

    def __init__(self, manager, background, previewpanel_rect) :

        self.pp_rect = previewpanel_rect
        self.pp_pos = previewpanel_rect[0:2]
        self.pp_grid_size = 20
        self.prev_obj_pos = (0,0)
        self.background = background

        rect = MP_RECT
        self.manager = manager
        self.mouse_label=pygame_gui.elements.UILabel(
                relative_rect = rect,
                text="mouse_pos",
                manager = self.manager)

    @property
    def abs_pos(self) :
        pos = pygame.mouse.get_pos()
        self.mouse_label.set_text('mouse position = {}'.format(pos))
        return pos # absolute mouse pos

    @property
    def pp_rel_pos(self) :
        return (self.abs_pos[0]-self.pp_pos[0],
                self.abs_pos[1]-self.pp_pos[1])

    @property
    def pp_grid_pos(self) :
        return ((self.abs_pos[0]-self.pp_pos[0])//self.pp_grid_size*self.pp_grid_size,
                (self.abs_pos[1]-self.pp_pos[1])//self.pp_grid_size*self.pp_grid_size)

    @property
    def on_previewpanel(self) :
        return self.pp_rect.collidepoint(self.abs_pos)

    def left_click(self, event) :
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

    def store_click_pos(self, obj_pos=(0,0)) :
        self.prev_obj_pos = obj_pos
        self.pp_prev_pos = self.pp_rel_pos

    def displacment_since_last_click(self) :
        return (self.prev_obj_pos[0] + self.pp_rel_pos[0] - self.pp_prev_pos[0],
                self.prev_obj_pos[1] + self.pp_rel_pos[1] - self.pp_prev_pos[1])

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

if __name__ == "__main__" :
    interface = main_interface()
    interface.loop()

main()

