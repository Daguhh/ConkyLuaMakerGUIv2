elements = {
-- cpu0
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 150, 
conky_value = 'cpu cpu0', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x9999DD, 
bar_alpha = 1.0, 
bar_thickness = 8, 
start_angle = 240, 
end_angle = 360, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 8, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- cpu1
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 160, 
conky_value = 'cpu cpu1', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x9999DD, 
bar_alpha = 1.0, 
bar_thickness = 8, 
start_angle = 240, 
end_angle = 360, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 8, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- cpu2
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 170, 
conky_value = 'cpu cpu2', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x9999DD, 
bar_alpha = 1.0, 
bar_thickness = 8, 
start_angle = 240, 
end_angle = 360, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 8, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- cpu3
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 180, 
conky_value = 'cpu cpu3', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x9999DD, 
bar_alpha = 1.0, 
bar_thickness = 8, 
start_angle = 240, 
end_angle = 360, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 8, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- home
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 175, 
conky_value = 'fs_used_perc /home/', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0xA62216, 
bar_alpha = 1.0, 
bar_thickness = 19, 
start_angle = 120, 
end_angle = 240, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 19, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- root
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 155, 
conky_value = 'fs_used_perc /', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0xD64416, 
bar_alpha = 1.0, 
bar_thickness = 19, 
start_angle = 120, 
end_angle = 240, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 19, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- swap
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 155, 
conky_value = 'swapperc', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x44DD44, 
bar_alpha = 1.0, 
bar_thickness = 19, 
start_angle = 0, 
end_angle = 120, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 19, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- ram
{
kind = 'ring_graph',
center = {x=200, y=300}, 
radius = 175, 
conky_value = 'memperc', 
max_value = 100, 
critical_threshold = 90, 
bar_color = 0x22A616, 
bar_alpha = 1.0, 
bar_thickness = 19, 
start_angle = 0, 
end_angle = 120, 
background_color = 0x222222, 
background_alpha = 1.0, 
background_thickness = 19, 
change_color_on_critical = false, 
change_alpha_on_critical = false, 
change_thickness_on_critical = false, 
background_color_critical = 0xFFFFFF, 
background_alpha_critical = 1.0, 
background_thickness_critical = 8, 
bar_color_critical = 0x000000, 
bar_alpha_critical = 1, 
bar_thickness_critical = 8, 
},
-- separator mem
{
kind = 'line',
from = {x=85, y=505}, 
to = {x=155, y=369}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- separator file
{
kind = 'line',
from = {x=158, y=232}, 
to = {x=72, y=78}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- separator cpu
{
kind = 'line',
from = {x=280, y=301}, 
to = {x=455, y=299}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- line home
{
kind = 'line',
from = {x=69, y=418}, 
to = {x=42, y=438}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text home
{
kind = 'static_text',
from = {x=10, y=455}, 
text = 'Home', 
color = 0xFFFFFF, 
fontsize = 16, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- line root
{
kind = 'line',
from = {x=59, y=241}, 
to = {x=92, y=233}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text root
{
kind = 'static_text',
from = {x=82, y=228}, 
text = 'Root', 
color = 0xFFFFFF, 
fontsize = 16, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- line ram
{
kind = 'line',
from = {x=186, y=474}, 
to = {x=235, y=504}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text ram
{
kind = 'static_text',
from = {x=240, y=511}, 
text = 'Ram', 
color = 0xFFFFFF, 
fontsize = 16, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- line swap
{
kind = 'line',
from = {x=318, y=347}, 
to = {x=335, y=377}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text swap
{
kind = 'static_text',
from = {x=292, y=344}, 
text = 'Swap', 
color = 0xFFFFFF, 
fontsize = 16, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- text CPU
{
kind = 'static_text',
from = {x=396, y=298}, 
text = 'CPU', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- line horiz FIle
{
kind = 'line',
from = {x=74, y=78}, 
to = {x=192, y=78}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text file sys
{
kind = 'static_text',
from = {x=80, y=77}, 
text = 'File System', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- line horiz mem
{
kind = 'line',
from = {x=86, y=504}, 
to = {x=183, y=504}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- text horiz mem
{
kind = 'static_text',
from = {x=105, y=502}, 
text = 'Mem', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- ring
{
kind = 'ring',
center = {x=454, y=123}, 
radius = 176, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 2, 
start_angle = 20, 
end_angle = 90, 
},
-- ring
{
kind = 'ring',
center = {x=693, y=223}, 
radius = 84, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 2, 
start_angle = 208, 
end_angle = 270, 
},
-- line
{
kind = 'line',
from = {x=692, y=138}, 
to = {x=780, y=138}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- ring
{
kind = 'ring',
center = {x=510, y=188}, 
radius = 90, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 2, 
start_angle = 270, 
end_angle = 405, 
},
-- line
{
kind = 'line',
from = {x=513, y=98}, 
to = {x=393, y=98}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- ring
{
kind = 'ring',
center = {x=486, y=395}, 
radius = 98, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 2, 
start_angle = 268, 
end_angle = 450, 
},
-- ring
{
kind = 'ring',
center = {x=699, y=105}, 
radius = 262, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 2, 
start_angle = 90, 
end_angle = 125, 
},
-- line
{
kind = 'line',
from = {x=696, y=366}, 
to = {x=769, y=366}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- line
{
kind = 'line',
from = {x=488, y=493}, 
to = {x=424, y=493}, 
bar_color = 0xFFFFFF, 
bar_alpha = 1.0, 
bar_thickness = 1, 
graduated = 1, 
number_graduation = 10, 
space_between_graduation = 1, 
},
-- mount disk
{
kind = 'static_text',
from = {x=403, y=94}, 
text = 'Mounted', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- network
{
kind = 'static_text',
from = {x=425, y=489}, 
text = 'Network', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- static_text
{
kind = 'static_text',
from = {x=690, y=134}, 
text = 'Download', 
color = 0xFFFFFF, 
fontsize = 20, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- top cpu 1
{
kind = 'variable_text',
from = {x=392, y=313}, 
conky_value = 'top cpu 1', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- top cpu 2
{
kind = 'variable_text',
from = {x=392, y=323}, 
conky_value = 'top cpu 2', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- copy of top cpu 2
{
kind = 'variable_text',
from = {x=392, y=333}, 
conky_value = 'top cpu 3', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- top name 1
{
kind = 'variable_text',
from = {x=452, y=313}, 
conky_value = 'top name 1', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- top name 3
{
kind = 'variable_text',
from = {x=452, y=333}, 
conky_value = 'top name 3', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
-- copy of top name 2
{
kind = 'variable_text',
from = {x=452, y=323}, 
conky_value = 'top name 2', 
color = 0xFFFFFF, 
fontsize = 12, 
rotation = 0, 
font = 'default font', 
alpha = 1, 
},
}