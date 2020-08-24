from tkinter import *
import time
import random
import pickle
print("@Dasun2020")

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas =  canvas
        self.paddle = paddle
        self.id = canvas.create_rectangle(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.speed = 3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        global x
        x = 0
        
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
    
    
    
    
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = self.speed * -1
            global x
            x = x + 1
            self.speed = self.speed + 0.1
        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= self.canvas_width:
            self.x = self.speed * -1


            
            

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.speed = 4
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

            
    def turn_left(self, evt):
        self.x = self.speed * -1
    
    def turn_right(self, evt):
        self.x = self.speed
        
def kill():
    tk.destroy()
    print("Your score was %s" % x)
    
def SAVE():
    save_file = open('save.dat', 'wb')
    pickle.dump(x, save_file)
    save_file.close()
    
def loadSave():
    load_file = open('save.dat', 'rb')
    global LOAD
    LOAD = pickle.load(load_file)
    load_file.close()
    print(LOAD)


        
tk = Tk()
tk.title("PONG")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
btn = Button(tk, text="Quit?(note: quiting will not save your high score!)", command=kill).pack()
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if ball.hit_bottom == True:
        loadSave()
        text = canvas.create_text(200, 200, text='Game over')
        text = canvas.create_text(200, 250, text="Your score is %s" % x)
        if x > LOAD:
            SAVE()
            text = canvas.create_text(200, 270, text="You set a high score!")
        else:
            text = canvas.create_text(200, 270, text="highest score is %s" % LOAD)

        
