import pygame as pg

def fill():
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            pg.draw.rect(window, (255*((i+j)%2), 0, 0), pg.Rect((winsize//8)*j, (winsize//8)*i, winsize//8, winsize//8))
            if col == '-': continue
            if col == 's':
                pg.draw.circle(window, (0, 255, 10), ((winsize//8)*(j+.5),(winsize//8)*(i+.5)), winsize//40)
                continue
            pg.draw.circle(window, (125*col, 125*col, 125*col), ((winsize//8)*(j+.5),(winsize//8)*(i+.5)), winsize//20)

def reset():
    for row in range(8):
        for col in range(8):
            if board[row][col] == 's': board[row][col] = '-'

pg.init()
winsize = 640
window = pg.display.set_mode((winsize, winsize))
p = 1
ns = [-1, 1]
board = [['-' for j in range(8)]for i in range(8)]
for row in range(8):
    for col in range(8):
        if (row+col)%2 == 1:
            if row < 3: board[row][col] = 1
            elif row > 4: board[row][col] = 0

clicked = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:  
                mouse_x, mouse_y = pg.mouse.get_pos()
                col = mouse_x//(winsize//8)
                row = mouse_y//(winsize//8)

                if board[row][col] == 's':
                    board[row][col] = p
                    board[oldspot[0]][oldspot[1]] = '-'
                    board[row-ns[p]][col-1 if col > oldspot[1] else col+1] = '-'
                    p = 1-p
                    reset()
                if board[row][col] == p:
                    reset()
                    for i in ns:
                        try:
                            if board[row+ns[p]][col+i] == '-':
                                if row+ns[p] != -1 and col+i != -1:
                                    board[row+ns[p]][col+i] = 's'
                                    oldspot = row, col
                            elif board[row+ns[p]*2][col+i*2] == '-' and board[row+ns[p]][col+i] != p:
                                if row+ns[p] != -1 and col+i*2 != -1:
                                    board[row+ns[p]*2][col+i*2] = 's'  
                                    oldspot = row, col
                        except:
                            pass

    window.fill('black')
    fill()
    pg.display.update()