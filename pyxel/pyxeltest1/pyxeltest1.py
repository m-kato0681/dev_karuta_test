import pyxel

WINDOW_H = 120
WINDOW_W = 160
CAT_H = 32
CAT_W = 32
 
class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, caption="Hello Pyxel")
        pyxel.image(0).load(0, 0, "d:/work/pyxel/pyxeltest1/megaman.png")
        pyxel.image(1).load(0, 0, "d:/work/pyxel/pyxeltest1/blues.png")
 
        pyxel.run(self.update, self.draw)
 
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 
    def draw(self):
        pyxel.cls(0)
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(60, 65, 0, 0, 0, 38, 32)
        pyxel.blt(75, 45, 1, 0, 0, CAT_W, CAT_H, 5)
 
App()