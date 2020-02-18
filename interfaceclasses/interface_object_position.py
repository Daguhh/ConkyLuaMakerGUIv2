#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Edit this file to configure position of interface elements
"""

import pygame

# Interface

INTERFACE_SIZE = (1000, 650)

# ChoiceButtonPanel

CBP_HEIGHT = 40
CBP_WIDTH = 85
CBP_OFFSET = 100
CBP_SPACING = 5

# OptionPanel
OP_BOX_HEIGHT = 18
OP_BOX_NUMBER = 25
OP_LABEL_BOX_WIDTH = 140
OP_ENTRY_BOX_WIDTH = 120
x0 = INTERFACE_SIZE[0] - (OP_LABEL_BOX_WIDTH + OP_ENTRY_BOX_WIDTH + 0)
OP_PANEL_POS = (x0, 120)
OP_PANEL_BACKGROUND_COLOR = (150, 150, 150)

# PreviewPanel
PP_POS = (CBP_WIDTH + 2 * 5, 50)
x = (
    INTERFACE_SIZE[0]
    - PP_POS[0]
    - (OP_ENTRY_BOX_WIDTH + 15)
    - (OP_ENTRY_BOX_WIDTH + 10)
)
y = INTERFACE_SIZE[1] - PP_POS[1] - 50
PP_SIZE = (x, y)
PP_COLOR = pygame.Color("#555555FF")

# SelectPanel
x0 = INTERFACE_SIZE[0] - 240
x1 = INTERFACE_SIZE[0] - 45
SP_DROPDOWN_RECT = pygame.Rect((x0, 10), (235, 40))
SP_RENAME_BOX_RECT = pygame.Rect((x0, 50), (200, 40))
SP_DELETE_BUTTON_RECT = pygame.Rect((x1, 50), (40, 40))
SP_LABEL_GRID_SIZE_RECT = pygame.Rect((x0, 80), (100, 25))
SP_ENTRY_GRID_SIZE_RECT = pygame.Rect((x0 + 100, 80), (100, 25))

# MenuButtons

MB_MENU_RECT = pygame.Rect((10, 10), (110, 30))
MB_GEN_RECT = pygame.Rect((130, 10), (150, 30))
MB_SAVE_RECT = pygame.Rect((290, 10), (130, 30))
MB_LOAD_RECT = pygame.Rect((430, 10), (150, 30))
MB_HELP_RECT = pygame.Rect((590, 10), (50, 30))

# MousePositionDisplay
x = PP_POS[0] + PP_SIZE[0] - 240
y = PP_POS[1] + PP_SIZE[1] + 10
MP_RECT = pygame.Rect((x, y), (240, 25))
