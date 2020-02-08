#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .parse_dct import lua2pil_dct, pil2lua_dct

class LuaGraph:
    def __init__(self) :

        self.pos = (0,0)
        self.is_moving = False
        self.position_list=[]

    def get_lua_dct(self) :
        return pil2lua_dct(self.dct, self.pos)

    def set_pil_dct(self, lua_dct) :
        return lua2pil_dct(lua_dct)

    def set_dct_item_from_lua(self, lua_dct_item) :
        pil_dct_item = lua2pil_dct(lua_dct_item, self.pos)
        k, v = pil_dct_item.popitem()
        self.dct[k] = v

    def blit(self):

        self.update()
        self.draw_area.blit(self.surface,self.pos)









