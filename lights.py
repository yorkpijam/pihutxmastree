from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep

# groups the LEDS from each wing of the tree so I can 
# make them do things together or individually
tree = LEDBoard(
    star=LEDBoard(2),
    brancha=LEDBoard(top=17, middle=4, bottom=14),
    branchb=LEDBoard(top=9, middle=22, bottom=10),
    branchc=LEDBoard(top=25, middle=24, bottom=23),
    branchd=LEDBoard(top=16, middle=13, bottom=20),
    branche=LEDBoard(top=19, middle=26, bottom=21),
    branchf=LEDBoard(top=11, middle=5, bottom=12),
    branchg=LEDBoard(top=8, middle=6, bottom=7),
    branchh=LEDBoard(top=27, middle=18, bottom=15)
)

def flasha():
    tree.star.on()
    tree.brancha.top.on()
    tree.branchb.middle.on()
    tree.brancha.bottom.on()
    tree.branchc.top.on()
    tree.branchd.middle.on()
    tree.branchc.bottom.on()
    tree.branche.top.on()
    tree.branchf.middle.on()
    tree.branche.bottom.on()
    tree.branchg.top.on()
    tree.branchh.middle.on()
    tree.branchg.bottom.on()
    sleep(0.5)
    tree.brancha.top.off()
    tree.branchb.middle.off()
    tree.brancha.bottom.off()
    tree.branchc.top.off()
    tree.branchd.middle.off()
    tree.branchc.bottom.off()
    tree.branche.top.off()
    tree.branchf.middle.off()
    tree.branche.bottom.off()
    tree.branchg.top.off()
    tree.branchh.middle.off()
    tree.branchg.bottom.off()
    tree.star.off()

def flashb():
    tree.star.on()
    tree.branchb.top.on()
    tree.brancha.middle.on()
    tree.branchb.bottom.on()
    tree.branchd.top.on()
    tree.branchc.middle.on()
    tree.branchd.bottom.on()
    tree.branchf.top.on()
    tree.branche.middle.on()
    tree.branchf.bottom.on()
    tree.branchh.top.on()
    tree.branchg.middle.on()
    tree.branchh.bottom.on()
    sleep(0.5)
    tree.branchb.top.off()
    tree.brancha.middle.off()
    tree.branchb.bottom.off()
    tree.branchd.top.off()
    tree.branchc.middle.off()
    tree.branchd.bottom.off()
    tree.branchf.top.off()
    tree.branche.middle.off()
    tree.branchf.bottom.off()
    tree.branchh.top.off()
    tree.branchg.middle.off()
    tree.branchh.bottom.off()
    tree.star.off()
    
def layers():
    tree.star.on()
    tree.brancha.bottom.on()
    tree.branchb.bottom.on()
    tree.branchc.bottom.on()
    tree.branchd.bottom.on()
    tree.branche.bottom.on()
    tree.branchf.bottom.on()
    tree.branchg.bottom.on()
    tree.branchh.bottom.on()
    sleep(0.5)
    tree.brancha.bottom.off()
    tree.branchb.bottom.off()
    tree.branchc.bottom.off()
    tree.branchd.bottom.off()
    tree.branche.bottom.off()
    tree.branchf.bottom.off()
    tree.branchg.bottom.off()
    tree.branchh.bottom.off()
    tree.brancha.middle.on()
    tree.branchb.middle.on()
    tree.branchc.middle.on()
    tree.branchd.middle.on()
    tree.branche.middle.on()
    tree.branchf.middle.on()
    tree.branchg.middle.on()
    tree.branchh.middle.on()
    sleep(0.5)
    tree.brancha.middle.off()
    tree.branchb.middle.off()
    tree.branchc.middle.off()
    tree.branchd.middle.off()
    tree.branche.middle.off()
    tree.branchf.middle.off()
    tree.branchg.middle.off()
    tree.branchh.middle.off()
    tree.brancha.top.on()
    tree.branchb.top.on()
    tree.branchc.top.on()
    tree.branchd.top.on()
    tree.branche.top.on()
    tree.branchf.top.on()
    tree.branchg.top.on()
    tree.branchh.top.on()
    sleep(0.5)
    tree.brancha.top.off()
    tree.branchb.top.off()
    tree.branchc.top.off()
    tree.branchd.top.off()
    tree.branche.top.off()
    tree.branchf.top.off()
    tree.branchg.top.off()
    tree.branchh.top.off()
    tree.star.off

while True:
    for x in range (0, 9):
        flasha()
        flashb()
    for x in range (0, 9):
        layers()
