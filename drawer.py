import pygame,math
from tkinter import *


pygame.init()
window = pygame.display.set_mode((800, 750))
pygame.display.set_caption("drawer")


font = pygame.font.SysFont('Corbel', 30)
font2 = pygame.font.SysFont('Corbel', 20)
global draw_colors
draw_colors = True
def redraw_color_buttons_window():
    """this function redraw the colors buttons and the text that above them"""
    if draw_colors == True:
        pygame.draw.rect(window,(0,0,0), [0,40, 40,60])
        pygame.draw.rect(window, (105,105,105), [41, 40, 40, 60])
        pygame.draw.rect(window,(255,255,255), [82,40, 40,60])
        pygame.draw.rect(window,(255,0,0), [123,40, 40,60])
        pygame.draw.rect(window, (205,133,63), [164, 40, 40, 60])
        pygame.draw.rect(window, (255,165,0), [205, 40, 40, 60])
        pygame.draw.rect(window, (255,255,0), [246, 40, 40, 60])
        pygame.draw.rect(window, (255,222,173), [287, 40, 40, 60])
        pygame.draw.rect(window, (128,0,128), [328, 40, 40, 60])
        pygame.draw.rect(window,(132,112,255), [369,40, 40,60])
        pygame.draw.rect(window, (255,0,255), [410, 40, 40, 60])
        pygame.draw.rect(window,(0,0,255), [451,40, 40,60])
        pygame.draw.rect(window,(16,78,139), [492,40, 40,60])
        pygame.draw.rect(window,(16,128,128), [533,40, 40,60])
        pygame.draw.rect(window,(32,178,170), [574,40, 40,60])
        pygame.draw.rect(window, (64,224,208), [615, 40, 40, 60])
        pygame.draw.rect(window,(0,255,255), [656,40, 40,60])
        pygame.draw.rect(window, (0,255,0), [697, 40, 40, 60])
        pygame.draw.rect(window,(0,128,0), [738,40, 40,60])

    pygame.draw.circle(window, (0,0,0), (270,120),5) # draw the smallest circle
    pygame.draw.circle(window, (0,0,0), (300,120),10)
    pygame.draw.circle(window, (0,0,0), (340,120),15) # draw the bigest circle

    window.blit(font.render("press on the color that you want to draw with", True, (0, 0, 0)), (0, 0))
    pygame.draw.rect(window, (173,216,230), [0, 105, 250, 30])
    window.blit(font2.render("has your own color? press here", True, (0, 0, 0)), (0, 110)) # if press on the sentence a tkinter window with a place to write the numbers is show
    pygame.draw.rect(window, (173,216,230), [630, 105, 60, 30])
    window.blit(font2.render("clean",True,(0,0,0)), (640,110))
    pygame.draw.rect(window, (173,216,230), [700, 105, 95, 30])
    window.blit(font2.render("save draw",True,(0,0,0)), (710,110))
    pygame.draw.rect(window, (173,216,230), [520, 105, 90, 30])
    window.blit(font2.render("open file:",True,(0,0,0)), (530,110))
    pygame.draw.rect(window, (173,216,230), [400, 105, 90, 30])
    window.blit(font2.render("cut bg",True,(0,0,0)), (410,110))
    pygame.display.update()


def check_mouse_on_circle(circle_x,circle_y,circle_radios):
    """this function check if the player press inside a circle of a letter"""
    x = pygame.mouse.get_pos()[0] # mouse posision in x line
    y = pygame.mouse.get_pos()[1] # mouse posision in y line
    sqx = (x - circle_x) ** 2
    sqy = (y - circle_y) ** 2
    if math.sqrt(sqx + sqy) < circle_radios:
        return True
    else:
        return False

def save_file(main_folder,seconderi_folder,file_name,file_type): # the best you can put here is main_folder = D seconderi_folder = python file name = test file_type = jpeg
    """this function sace the draw"""
    rect = pygame.Rect(0,135, 800, 615)
    sub = window.subsurface(rect)
    pygame.image.save(sub, str(main_folder) + ":\\" + str(seconderi_folder) + "\\" + str(file_name) + "." + str(file_type))
global new_background
new_background = ""
def openfile():
    global open_file,open_file_drive,press_open_file_drive,open_file_folder,press_open_file_folder,open_file_name,press_open_file_name,open_file_type,press_open_file_type,new_background
    print(str(open_file_drive) + ":\\" + str(open_file_folder) + "\\" + str(open_file_name) + "." + str(open_file_type))
    new_background = pygame.image.load(str(open_file_drive) + ":\\" + str(open_file_folder) + "\\" + str(open_file_name) + "." + str(open_file_type))
    new_background = pygame.transform.smoothscale(new_background, (800,614))  # change the size of the picture
    window.blit(new_background, (0, 136))

def main():
    drawing_on = True

    clock = pygame.time.Clock()


    press_down = False
    press_up = False

    global clean_screen,color,can_draw,radios_size,press_main_folder,press_seconderi_folder,press_file_name,press_file_type,draw_over,save_file2,write_color_numbers,final_color,open_file,open_file_drive,press_open_file_drive,open_file_folder,press_open_file_folder,open_file_name,press_open_file_name,open_file_type,press_open_file_type
    can_draw = True
    clean_screen = False
    color = (0,0,0)
    radios_size = 10
    draw_over = False
    save_file2 = False
    write_color_numbers = False
    final_color = ""


    press_main_folder = False
    main_folder = ""
    press_seconderi_folder = False
    seconderi_folder = ""
    press_file_name = False
    file_name = ""
    press_file_type = False
    file_type = ""

    open_file = False

    open_file_drive = ""
    press_open_file_drive = False
    open_file_folder = ""
    press_open_file_folder = False
    open_file_name = ""
    press_open_file_name = False
    open_file_type = ""
    press_open_file_type = False

    def set_line():
        global can_draw,color,clean_screen,radios_size,draw_colors,press_main_folder,press_seconderi_folder,press_file_name,press_file_type,draw_over,save_file2,write_color_numbers,final_color,open_file,open_file_drive,press_open_file_drive,open_file_folder,press_open_file_folder,open_file_name,press_open_file_name,open_file_type,press_open_file_type,new_background
        if press_down == True:
            mouse = pygame.mouse.get_pos()
            if 0 <= mouse[0] <= 800 and 0 <= mouse[1] <= 135:
                can_draw = False
            else:
                can_draw = True
            if 630 < mouse[0] < 630 + 60 and 105 < mouse[1] < 105 + 30:
                """if the player press on the clean button than clear screen become True"""
                clean_screen = True
            else:
                clean_screen = False
            if 400 < mouse[0] < 490 and 105 < mouse[1] < 135:
                clean_screen = True
                new_background = ""
            if 520 < mouse[0] < 610 and 105 < mouse[1] < 135:
                open_file = True
                draw_colors = False
            if check_mouse_on_circle(270,120,5) == True:
                """if press in the smallest circle"""
                radios_size = 5
            if check_mouse_on_circle(300,120,10) == True:
                """if press in the 10 radios circle"""
                radios_size = 10
            if check_mouse_on_circle(340,120,15) == True:
                """if press in the biggest circle"""
                radios_size = 15
            if 700 < mouse[0] < 700 + 95 and 105 < mouse[1] < 105 + 30:
                """if press to save the draw"""
                draw_colors = False
                save_file2 = True
            if 0 < mouse[0] < 250 and 105 < mouse[1] < 105 + 30:
                """if the player press on has your own color? press here"""
                draw_colors = False
                write_color_numbers = True
            if draw_colors == True and write_color_numbers == False and seconds >= 1: # this if check if the player can draw
                if draw_over == True:
                    pygame.draw.rect(window, (255,255,255) , [0,0, 800,100]) # put white on all of the colors
                    draw_over = False
                if 0 < mouse[0] < 40 and 40 < mouse[1] < 100:
                    color = (0,0,0)
                if 41 < mouse[0] < 41 + 40 and 40 < mouse[1] < 100:
                    color = (105,105,105)
                if 82 < mouse[0] < 82 + 40 and 40 < mouse[1] < 100:
                    color = (255,255,255)
                if 123 < mouse[0] < 123 + 40 and 40 < mouse[1] < 100:
                    color = (255,0,0)
                if 164 < mouse[0] < 164 + 40 and 40 < mouse[1] < 100:
                    color = (205,133,63)
                if 205 < mouse[0] < 205 + 40 and 40 < mouse[1] < 100:
                    color = (255,165,0)
                if 246 < mouse[0] < 246 + 40 and 40 < mouse[1] < 100:
                    color = (255,255,0)
                if 287 < mouse[0] < 287 + 40 and 40 < mouse[1] < 100:\
                    color = (255,222,173)
                if 328 < mouse[0] < 328 + 40 and 40 < mouse[1] < 100:
                    color = (128,0,128)
                if 369 < mouse[0] < 369 + 40 and 40 < mouse[1] < 100:
                    color = (132,112,255)
                if 410 < mouse[0] < 410 + 40 and 40 < mouse[1] < 100:
                    color = (255,0,255)
                if 451 < mouse[0] < 451 + 40 and 40 < mouse[1] < 100:
                    color = (0,0,255)
                if 492 < mouse[0] < 492 + 40 and 40 < mouse[1] < 100:
                    color = (16,78,139)
                if 533 < mouse[0] < 533 + 40 and 40 < mouse[1] < 100:
                    color = (16,128,128)
                if 574 < mouse[0] < 574 + 40 and 40 < mouse[1] < 100:
                    color = (32,178,170)
                if 615 < mouse[0] < 615 + 40 and 40 < mouse[1] < 100:
                    color = (64,224,208)
                if 656 < mouse[0] < 656 + 40 and 40 < mouse[1] < 100:
                    color = (0,255,255)
                if 697 < mouse[0] < 697 + 40 and 40 < mouse[1] < 100:
                    color = (0,255,0)
                if 738 < mouse[0] < 738 + 40 and 40 < mouse[1] < 100:
                    color = (0,128,0)
                if can_draw == True:
                    pygame.draw.circle(window, color,(mouse[0],mouse[1]), radios_size)
                    print(color)
                    pygame.display.update()
            if draw_colors == False and save_file2 == True: # this if check if the player want to save the draw

                pygame.draw.rect(window, (255,255,255) , [0,0, 800,100]) # put white on all of the colors
                window.blit(font2.render("drive(D/C):", True, (0, 0, 0)), (0, 10))
                pygame.draw.rect(window, (150,150,150), [0,30, 130,30])

                window.blit(font2.render("folder(in D/C):", True, (0, 0, 0)), (160, 10))
                pygame.draw.rect(window, (150,150,150), [160,30, 130,30])

                window.blit(font2.render("file name:", True, (0, 0, 0)), (370, 10))
                pygame.draw.rect(window, (150,150,150), [370,30, 130,30])

                window.blit(font2.render("file type:", True, (0, 0, 0)), (530, 10))
                pygame.draw.rect(window, (150,150,150), [530,30, 130,30])

                pygame.draw.rect(window, (173,216,230), [370,70, 80,30])
                window.blit(font2.render("submit:", True, (0, 0, 0)), (380, 75))

                pygame.draw.rect(window, (173,216,230), [670,10, 120,30])
                window.blit(font2.render("return drawing", True, (0, 0, 0)), (670, 10))

                if 670 < mouse[0] < 670 + 120 and 10 < mouse[1] < 10 + 30:
                    """return button"""
                    pygame.draw.rect(window, (255, 255, 255), [0, 0, 800, 100])
                    draw_colors = True
                    save_file2 = False

                if 370 < mouse[0] < 370 + 80 and 70 < mouse[1] < 100:
                    """if press submit"""
                    save_file(main_folder,seconderi_folder,file_name,file_type)
                    draw_colors = True
                    draw_over = True

                if 0 < mouse[0] < 130 and 30 < mouse[1] < 60:
                    press_main_folder = True
                    press_seconderi_folder = False
                    press_file_name = False
                    press_file_type = False
                    pygame.draw.rect(window, (0,0,0), [0,28,130,32],2)
                if 160 < mouse[0] < 290 and 30 < mouse[1] < 60:
                    press_main_folder = False
                    press_seconderi_folder = True
                    press_file_name = False
                    press_file_type = False
                    pygame.draw.rect(window, (0,0,0), [158,28,130,32],2)
                if 370 < mouse[0] < 500 and 30 < mouse[1] < 60:
                    press_main_folder = False
                    press_seconderi_folder = False
                    press_file_name = True
                    press_file_type = False
                    pygame.draw.rect(window, (0,0,0), [368,28,130,32],2)
                if 530 < mouse[0] < 660 and 30 < mouse[1] < 60:
                    press_main_folder = False
                    press_seconderi_folder = False
                    press_file_name = False
                    press_file_type = True
                    pygame.draw.rect(window, (0,0,0), [528,28,130,32],2)
            if draw_colors == False and write_color_numbers == True: # this if check if the player want to write his own color
                pygame.draw.rect(window, (255,255,255) , [0,0, 800,100]) # put white on all of the colors
                window.blit(font2.render("write the numbers like this 255,255,255 the numbers have to be beetwin 0 to 255", True, (0, 0, 0)), (10, 10))
                pygame.draw.rect(window, (173,216,230), [300,50, 120,30])

                pygame.draw.rect(window, (173,216,230), [480,50, 80,30])
                window.blit(font2.render("submit:", True, (0, 0, 0)), (490, 55))

                pygame.draw.rect(window, (173,216,230), [670,10, 120,30])
                window.blit(font2.render("return drawing", True, (0, 0, 0)), (670, 10))
                if 670 < mouse[0] < 670 + 120 and 10 < mouse[1] < 10 + 30:
                    """return button"""
                    pygame.draw.rect(window, (255, 255, 255), [0, 0, 800, 100])
                    draw_colors = True
                    write_color_numbers = False
                if 480 < mouse[0] < 560 and 50 < mouse[1] < 80:
                    if final_color != "":
                        color = final_color
                    final_color = ""
                    try:
                        color = color.split(",")
                        color = (int(color[0]),int(color[1]),int(color[2]))
                        draw_colors = True
                        write_color_numbers = False
                        pygame.draw.rect(window, (255, 255, 255), [0, 0, 800, 100])  # put white on all of the colors
                    except AttributeError:
                        pass
                if 300 < mouse[0] < 420 and 50 < mouse[1] < 80:
                    pygame.draw.rect(window, (0,0,0), [298,48, 122,32],2)
            if draw_colors == False and open_file == True:
                pygame.draw.rect(window, (255,255,255) , [0,0, 800,100]) # put white on all of the colors
                window.blit(font2.render("drive(D/C):", True, (0, 0, 0)), (0, 10))
                pygame.draw.rect(window, (150,150,150), [0,30, 130,30])

                window.blit(font2.render("folder(in D/C):", True, (0, 0, 0)), (160, 10))
                pygame.draw.rect(window, (150,150,150), [160,30, 130,30])

                window.blit(font2.render("file name:", True, (0, 0, 0)), (370, 10))
                pygame.draw.rect(window, (150,150,150), [370,30, 130,30])

                window.blit(font2.render("file type:", True, (0, 0, 0)), (530, 10))
                pygame.draw.rect(window, (150,150,150), [530,30, 130,30])

                pygame.draw.rect(window, (173,216,230), [370,70, 80,30])
                window.blit(font2.render("submit:", True, (0, 0, 0)), (380, 75))

                pygame.draw.rect(window, (173,216,230), [670,10, 120,30])
                window.blit(font2.render("return drawing", True, (0, 0, 0)), (670, 10))

                if 670 < mouse[0] < 790 and 10 < mouse[1] < 40:
                    """return button"""
                    pygame.draw.rect(window, (255, 255, 255), [0, 0, 800, 100]) # put white
                    draw_colors = True
                    open_file = False
                if 370 < mouse[0] < 450 and 70 < mouse[1] < 100:
                    """submit button"""
                    openfile()
                    open_file = False
                    draw_colors = True
                    pygame.draw.rect(window, (255, 255, 255), [0, 0, 800, 100]) # put white
                if 0 < mouse[0] < 130 and 30 < mouse[1] < 60:
                    press_open_file_drive = True
                    press_open_file_folder = False
                    press_open_file_name = False
                    press_open_file_type = False
                    pygame.draw.rect(window, (0,0,0), [0,28,130,32],2)
                if 160 < mouse[0] < 290 and 30 < mouse[1] < 60:
                    press_open_file_drive = False
                    press_open_file_folder = True
                    press_open_file_name = False
                    press_open_file_type = False
                    pygame.draw.rect(window, (0,0,0), [158,28,130,32],2)
                if 370 < mouse[0] < 500 and 30 < mouse[1] < 60:
                    press_open_file_drive = False
                    press_open_file_folder = False
                    press_open_file_name = True
                    press_open_file_type = False
                    pygame.draw.rect(window, (0,0,0), [368,28,130,32],2)
                if 530 < mouse[0] < 660 and 30 < mouse[1] < 60:
                    press_open_file_drive = False
                    press_open_file_folder = False
                    press_open_file_name = False
                    press_open_file_type = True
                    pygame.draw.rect(window, (0,0,0), [528,28,130,32],2)
        if draw_colors == False and write_color_numbers == True:
            pygame.draw.rect(window, (173, 216, 230), [300, 50, 120, 30])
            window.blit(font2.render(final_color, True, (0, 0, 0)), (305, 55))
        if draw_colors == False and save_file2 == True:
            window.blit(font2.render(main_folder, True, (0, 0, 0)), (5, 40))
            window.blit(font2.render(seconderi_folder, True, (0, 0, 0)), (165, 40))
            window.blit(font2.render(file_name, True, (0, 0, 0)), (375, 40))
            window.blit(font2.render(file_type, True, (0, 0, 0)), (535, 40))
        if draw_colors == False and open_file == True:
            window.blit(font2.render(open_file_drive, True, (0, 0, 0)), (5, 35))
            window.blit(font2.render(open_file_folder, True, (0, 0, 0)), (165, 35))
            window.blit(font2.render(open_file_name, True, (0, 0, 0)), (375, 35))
            window.blit(font2.render(open_file_type, True, (0, 0, 0)), (535, 35))
        pygame.display.update()

    global mystring,seconds,new_background
    start = True # start is create for it will draw the background and the buttons when the code starts
    ticks = 0
    seconds = 0
    while drawing_on:
        clock.tick(60)
        if write_color_numbers == True:
            ticks = 0
            seconds = 0
        if write_color_numbers == False:
            ticks += 1
        if ticks == 60:
            seconds += 1
            ticks = 0
        if clean_screen == True or start == True:
            """if clean_screen == True so it draw the background and the buttons again"""
            if new_background == "" and start == True:
                window.fill((255,255,255))
            if new_background == "" and start == False:
                pygame.draw.rect(window, (255,255,255), [0,136, 800, 614])
            if new_background != "":
                window.blit(new_background, (0, 136))
            clean_screen = False
            start = False # after the background,buttons draw in the first time start become False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                drawing_on = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                press_down = True
                press_up = False
            if event.type == pygame.MOUSEBUTTONUP:
                press_up = True
                press_down = False
            if press_main_folder == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        main_folder += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(main_folder)  > 0:
                        pygame.draw.rect(window, (150, 150, 150), [0, 30, 130, 30])
                        main_folder = main_folder[0:-1]
            if press_seconderi_folder == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        seconderi_folder += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(seconderi_folder) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [160, 30, 130, 30])
                        seconderi_folder = seconderi_folder[0:-1]
            if press_file_name == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        file_name += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(file_name) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [370, 30, 130, 30])
                        file_name = file_name[0:-1]
            if press_file_type == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        file_type += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(file_type) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [530, 30, 130, 30])
                        file_type = file_type[0:-1]

            if write_color_numbers == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        print(chr(event.key))
                        final_color += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(final_color) > 0:
                        pygame.draw.rect(window, (173, 216, 230), [300, 50, 120, 30])
                        final_color = final_color[0:-1]

            if press_open_file_drive == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        open_file_drive += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(open_file_drive) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [0, 30, 130, 30])
                        open_file_drive = open_file_drive[0:-1]
            if press_open_file_folder == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        open_file_folder += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(open_file_folder) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [160, 30, 130, 30])
                        open_file_folder = open_file_folder[0:-1]
            if press_open_file_name == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        open_file_name += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(open_file_name) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [370, 30, 130, 30])
                        open_file_name = open_file_name[0:-1]
            if press_open_file_type == True:
                if event.type == pygame.KEYDOWN:
                    if not event.key == pygame.K_BACKSPACE:
                        open_file_type += chr(event.key)
                    if event.key == pygame.K_BACKSPACE and len(open_file_type) > 0:
                        pygame.draw.rect(window, (150, 150, 150), [530, 30, 130, 30])
                        open_file_type = open_file_type[0:-1]
            if open_file == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        pygame.draw.rect(window, (255, 255, 255),[130, 30, 30, 30])  # from the first qube to the second
                        pygame.draw.rect(window, (255, 255, 255), [290, 30, 80, 30])  # from the second to the third
                        pygame.draw.rect(window, (255, 255, 255), [500, 30, 30, 30])  # from the third to the 4

                        pygame.draw.rect(window, (150, 150, 150), [0, 30, 130, 30])
                        pygame.draw.rect(window, (150, 150, 150), [160, 30, 130, 30])
                        pygame.draw.rect(window, (150, 150, 150), [370, 30, 130, 30])
                        pygame.draw.rect(window, (150, 150, 150), [530, 30, 130, 30])
                        pygame.draw.rect(window, (255,255,255), [660,30,140,30])

                        pygame.draw.rect(window, (173, 216, 230), [670, 10, 120, 30])
                        window.blit(font2.render("return drawing", True, (0, 0, 0)), (670, 10))

        set_line()
        if draw_colors == True:
            redraw_color_buttons_window()
        pygame.display.update()
main()