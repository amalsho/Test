import pygame as pg
import numpy as np
import pygame .camera
class Matrix:
    def __init__(self,app,font_size=8):
        self.app = app
        self.FONT_SIZE = font_size
        self.size = self.ROWS,self.COLS = app.HEIGHT // font_size,app.WIDTH // font_size
        self.katakana = np.array([chr(int('0x30a0',16) + i) for i in range(96)] + [''for i in range(20)] + ['A'for i in range(10)] + ['B'for i in range(10)] + ['C'for i in range(10)] + ['D'for i in range(10)] + ['E'for i in range(10)] + ['F'for i in range(10)] + ['G'for i in range(10)] + ['H'for i in range(10)] + ['I'for i in range(10)] + ['J'for i in range(10)] + ['K'for i in range(10)] + ['L'for i in range(10)] + ['M'for i in range(10)] + ['N'for i in range(10)] + ['O'for i in range(10)] + ['P'for i in range(10)] + ['Q'for i in range(10)] + ['R'for i in range(10)] + ['S'for i in range(10)] + ['T'for i in range(10)] + ['V'for i in range(10)] + ['W'for i in range(10)] + ['X'for i in range(10)] + ['Y'for i in range(10)] + ['Z'for i in range(10)] + ['1'for i in range(10)] + ['2'for i in range(10)] + ['3'for i in range(10)] + ['4'for i in range(10)] + ['5'for i in range(10)] + ['6'for i in range(10)] + ['7'for i in range(10)] + ['8'for i in range(10)] + ['9'for i in range(10)] + ['0'for i in range(10)])
        self.font=pg.font.SysFont('ms mincho' , font_size , bold=True)

        self.matrix = np.random.choice(self.katakana, self.size)
        self.char_intervals = np.random.randint(25,50,size=self.size)
        self.cols_speed = np.random.randint(100,250,size=self.size)
        self.prerendred_chars=self.get_prerendred_chars()
        
        self.image = self.get_image('images.jpg')

    def get_frame(self):
        image = app.cam.get_image()
        image = pg.transform.scale(image,self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array


    def get_image(self,path_to_file):
        image = pg.image.load(path_to_file)
        image = pg.transform.scale(image,self.app.RES)
        pixel_array = pg.pixelarray.PixelArray(image)
        return pixel_array

    def get_prerendred_chars(self):
        char_colors=[(0,green,0)for green in range(256)]
        prerendred_chars={}
        for char in self.katakana:
            prerendred_chars = {(char,color): self.font.render(char,True,color)for color in char_colors}
            prerendred_chars.update(prerendred_chars)
        return prerendred_chars

    def run(self):
        frames=pg.time.get_ticks()
        # self.change_chars(frames)
        self.shift_colums(frames)
        self.draw()

    def shift_colums(self,frames):
        num_cols = np.argwhere(frames%self.cols_speed==0)
        num_cols = num_cols[:,1]
        num_cols = np.unique(num_cols)
        self.matrix[:,num_cols]=np.roll(self.matrix[:,num_cols],shift=1,axis=0)

    def change_chars(self,frames):
        mask=np.argwhere(frames%self.char_intervals==0)
        new_chars=np.random.choice(self.katakana,mask.shape[0])
        self.matrix[mask[:,0],mask[:,1]]=new_chars

    def draw(self):
        self.image = self.get_frame()
        for y,row in enumerate(self.matrix):
            for x,char in enumerate(row):
                if char:
                    pos = x * self.FONT_SIZE,y * self.FONT_SIZE
                    _, red, green, blue = pg.Color(self.image[pos])
                    if red and green and blue:
                        color=(red + green + blue) // 3
                        color = 220 if 160 < color < 220 else color
                        char = self.font.render(char,False,(0,color,0))
                        # char = self.prerendred_chars[(char,(0,color,0))]
                        char.set_alpha(color + 60)
                        self.app.surface.blit(char, pos)

class MatrixVision:
    def __init__(self):
        self.RES=self.WIDTH,self.HEIGHT=1000,800
        pg.init()
        self.screen=pg.display.set_mode(self.RES)
        self.surface =pg.Surface(self.RES)
        self.clock=pg.time.Clock()
        self.matrix=Matrix(self)

        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()

    def draw(self):
        self.surface.fill(pg.Color("black"))
        self.matrix.run()
        self.screen.blit(self.surface,(0,0))
    
    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            pg.display.set_caption(str(self.clock.get_fps()))
            self.clock.tick(30)

if __name__=="__main__":
    app=MatrixVision()
    app.run()
