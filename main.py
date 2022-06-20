from tkinter import *
from tkinter import ttk

win = Tk()

win.geometry("250x150")

def display_text():
   global entry
   global string
   string = entry.get()
   win.destroy()
entry = Entry(win, width = 20)
entry.focus_set()
def make_label():
    global label
    label = Label(win, text = "Enter the amount of rings")
    label.pack()
make_label()
entry.pack()
ttk.Label()
enter = ttk.Button(win, text = "Enter",width = 20, command = display_text)
enter.pack(pady=20)

win.mainloop()
rings = int(string)
import pygame
from logic import *
pygame.init()
win = pygame.display.set_mode((1024,650))
pygame.display.set_caption("Hanoi Towers")
def number_of_moves(N):
    return 2**N - 1


towers = [[],[],[]]

def ring_amount(num):
    for x in range(1, num+1):
        towers[0].append(x)

ring_amount(rings)
tower1 = Tower(350, 30, 201, 300)

tower2 = Tower(350, 30, 482, 300)

tower3 = Tower(350, 30, 763, 300)
run = True

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Optimal amount of moves: '+str(number_of_moves(rings)), True, "red")

while run:
    win.fill((199, 213, 245))
    win.blit(text, (230, 50))
    tower1.draw(win)
    tower2.draw(win)
    tower3.draw(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()

