#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
mother class of lua[drawings]
methods and properties :
    - save position value in PositionValueObject format
    - translate lua <=> pygame format
    - blit func
"""

from .parse_dct import lua2pil_dct, pil2lua_dct
from .math_tools import PositionValueObject as pval


class LuaGraph:
    def __init__(self):

        self._pos = pval((0, 0))
        self.is_moving = False
        self.is_resizing = False
        self.grid_step = 1

    @property
    def pos(self):
        return tuple(self._pos)

    @pos.setter
    def pos(self, pos):
        self._pos = pval(pos)

    def get_lua_dct(self):
        return pil2lua_dct(self.dct, self.pos)

    def set_pil_dct(self, lua_dct):
        return lua2pil_dct(lua_dct)

    def set_dct_item_from_lua(self, lua_dct_item):
        pil_dct_item = lua2pil_dct(lua_dct_item, self.pos)
        k, v = pil_dct_item.popitem()
        self.dct[k] = v

    def blit(self):
        try:
            self.update()
        except ValueError as err:
            print(
                "{} : thickness > radius\n you should give a larger value\n put your mouse away".format(
                    err
                )
            )
        self.draw_area.blit(self.surface, self.pos)
