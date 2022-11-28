# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *
import yaml

WIDTH=900
HEIGHT=600

panel1Fn = 'clemsonGuide.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)
panel1z=panel1Y['groups']
keys, values = list(panel1z.keys()), panel1z.values()
global panel
panel = []

dy = 50; idx = 0

for key in values: #values for value of dict, use keys if keys needed
    ba = enoButtonArray(key, buttonDim=(150, 30), dx=160, 
                           basePos=(0, dy*idx))
    panel.append(ba); idx += 1


def draw(): 
  global panel
  for ba in panel: ba.draw(screen)

def on_mouse_down(pos):
  global panel
  for ba in panel: ba.on_mouse_down(pos)

### end ###               