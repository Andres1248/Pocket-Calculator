
import pygame
import cmath
import math
import os
from asset_loader import load_image, load_sound





# Función para la exponenciación.
def myExp(num1, num2):
    if type(num2) == int or type(num2) == float and (type(num1) == int or type(num1) == float):
        negative = False
        myVar = num1
        if num2 < 0:
            num2 = -num2
            negative = True
        if num1 == 0:
            return 0
        if num2 == 0:
            return 1
        if type(num2) == int and type(num1) == int:
            for i in range(num2 - 1):
                num1 *= myVar
        else:
            num1 = num1 ** num2
        if negative:
            return 1 / num1
        else:
            return num1


# Función para la división.
def myDiv(num1, num2):
    if num2 == 0:
        return ''
    if (type(num2) == float or type(num2) == int) and (type(num1) == int or type(num1) == float):
        return num1 / num2


# Función para obtener el inverso multiplicativo.
def myInv(num):
    if num == 0:
        return ''
    if (type(num) == int or type(num) == float):
        return 1 / num
    else:
        return ''


# Función para la multiplicación.
def myMult(num1, num2):
    if (type(num2) == float or type(num2) == int) and (type(num1) == int or type(num1) == float):
        if type(num1) == int or type(num2) == int:
            myVar = num1
            if num2 == 0:
                return 0
            elif num2 > 0:
                for i in range(num2 - 1):
                    num1 += myVar
                return num1
            else:
                num2 = -num2
                for i in range(num2 - 1):
                    num1 += myVar
                return -num1
        else:
            return num1 * num2

#Inicia el proyecto
pygame.init()

background = load_image("Fondo.jpg")
explosion_sound = load_sound("explosion.mp3")


#ubicacion del archivo que se usa en el fondo
script_dir = os.path.dirname(os.path.realpath(__file__))
#fondo_path = os.path.join(script_dir, 'imagenes', 'Fondo.jpg')

#fondo = pygame.image.load(fondo_path)
screen = pygame.display.set_mode(size=(255, 340))
pygame.display.set_caption('Calculadora')

# Declaramos los espacios donde se generan las interacciones.
rectangle = pygame.Rect(10, 10, 230, 80)

buttonCE = pygame.Rect(10, 98, 40, 40)
buttonC = pygame.Rect(58, 98, 40, 40)
buttonPlusMinus = pygame.Rect(106, 98, 40, 40)
buttonExp = pygame.Rect(154, 98, 40, 40)
buttonRoot = pygame.Rect(202, 98, 40, 40)

button7 = pygame.Rect(10, 146, 40, 40)
button8 = pygame.Rect(58, 146, 40, 40)
button9 = pygame.Rect(106, 146, 40, 40)
buttonDiv = pygame.Rect(154, 146, 40, 40)
buttonLog = pygame.Rect(202, 146, 40, 40)

button4 = pygame.Rect(10, 194, 40, 40)
button5 = pygame.Rect(58, 194, 40, 40)
button6 = pygame.Rect(106, 194, 40, 40)
buttonMult = pygame.Rect(154, 194, 40, 40)
buttonInv = pygame.Rect(202, 194, 40, 40)

button1 = pygame.Rect(10, 242, 40, 40)
button2 = pygame.Rect(58, 242, 40, 40)
button3 = pygame.Rect(106, 242, 40, 40)
buttonMinus = pygame.Rect(154, 242, 40, 40)
buttonEq = pygame.Rect(202, 242, 40, 88)

button0 = pygame.Rect(10, 290, 88, 40)
buttonDec = pygame.Rect(106, 290, 40, 40)
buttonPlus = pygame.Rect(154, 290, 40, 40)

# Declaramos fuentes de texto, que desplegaremos en la interfaz gráfica.
imgCE = pygame.font.SysFont(None, 35)

imgRoot = pygame.font.SysFont(None, 25)

my_text_display = pygame.font.SysFont(None, 100)

#Declaramos el texto que se le muestra al usuario
user_text_1 = ''

#Ruta para encontrar los archivos de audio
script_dir = os.path.dirname(os.path.realpath(__file__))
#musica_path = os.path.join(script_dir,'musica' ,'Musica.mp3')
#explosion_path = os.path.join(script_dir,'musica', 'explosion.mp3')

#musica que utiliza el programa y sus efectos de sonido (la canción se llama: Creative Exercise Mario Paint)
pygame.mixer.music.load(musica_path)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
Sound = pygame.mixer.Sound(explosion_path)
Sound.set_volume(0.90)

num1 = 0
num2 = 0

num1_used = False
num2_used = False

operator_add = False
operator_sub = False
operator_mult = False
operator_div = False
operator_exp = False
operator_inv = False

operator_log1 = False
operator_log2 = False

#funcion para el color transparente de los botones
def draw_transparent_rect(screen, rect, color_with_alpha):
    surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    surface.fill(color_with_alpha)
    screen.blit(surface, rect.topleft)

while True:
    # Desplegamos los rectángulos en la interfaz gráfica.
    fondo = pygame.transform.scale(fondo, (250, 250))

    #Se declara el fondo y el lugar donde pasan las operaciones
    screen.blit(fondo, (0, 93))
    pygame.draw.rect(screen, 'white', rectangle)

    #Se despliegan los cuadros

    draw_transparent_rect(screen, buttonDec, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonMinus, (255, 255, 255, 80))
    draw_transparent_rect(screen, buttonDiv, (255, 255, 255, 80))
    draw_transparent_rect(screen, buttonMult, (255, 255, 255, 80))
    draw_transparent_rect(screen, buttonRoot, (255, 255, 255, 80))
    draw_transparent_rect(screen, button0, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonC,(255, 255, 255, 100))
    draw_transparent_rect(screen, buttonPlusMinus,(255, 255, 255, 100))
    draw_transparent_rect(screen, buttonCE, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonExp, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonDiv, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonLog, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonInv, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonEq, (255, 255, 255, 100))
    draw_transparent_rect(screen, buttonPlus, (255, 255, 255, 100))

    # Desplegamos texto en los rectángulos.
    screen.blit(imgCE.render('CE', False, 'black'), (13, 98))
    screen.blit(imgCE.render('C', False, 'black'), (61, 98))
    screen.blit(imgCE.render('+/-', False, 'black'), (109, 98))
    screen.blit(imgCE.render('**', False, 'black'), (157, 98))
    screen.blit(imgRoot.render("√", False, 'black'), (205, 98))

    screen.blit(imgCE.render('7', False, 'black'), (13, 146))
    screen.blit(imgCE.render('8', False, 'black'), (61, 146))
    screen.blit(imgCE.render('9', False, 'black'), (109, 146))
    screen.blit(imgCE.render('/', False, 'black'), (157, 146))
    screen.blit(imgRoot.render('log', False, 'black'), (205, 146))

    screen.blit(imgCE.render('4', False, 'black'), (13, 194))
    screen.blit(imgCE.render('5', False, 'black'), (61, 194))
    screen.blit(imgCE.render('6', False, 'black'), (109, 194))
    screen.blit(imgCE.render('*', False, 'black'), (157, 194))
    screen.blit(imgCE.render('1/x', False, 'black'), (205, 194))

    screen.blit(imgCE.render('1', False, 'black'), (13, 242))
    screen.blit(imgCE.render('2', False, 'black'), (61, 242))
    screen.blit(imgCE.render('3', False, 'black'), (109, 242))
    screen.blit(imgCE.render('-', False, 'black'), (157, 242))
    screen.blit(imgCE.render('=', False, 'black'), (205, 266))

    screen.blit(imgCE.render('0', False, 'black'), (37, 290))
    screen.blit(imgCE.render('.', False, 'black'), (109, 290))
    screen.blit(imgCE.render('+', False, 'black'), (157, 290))

    visible_text = my_text_display.render(user_text_1, True, (0, 0, 0))
    screen.blit(visible_text, (10, 10))

#Reaccion de los botones ante un input
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button7.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '7'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button8.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '8'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button9.collidepoint(event.pos) and len(user_text_1) <= 6:

                user_text_1 += '9'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button4.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '4'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button5.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '5'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button6.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '6'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button1.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '1'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button2.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '2'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button3.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '3'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif button0.collidepoint(event.pos) and len(user_text_1) <= 6:
                user_text_1 += '0'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        if '.' in user_text_1:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)
                    elif not num2_used:
                        if '.' in user_text_1:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
            elif buttonDec.collidepoint(event.pos) and len(user_text_1) <= 6:
                if user_text_1 == '':
                    break
                if '.' not in user_text_1 and user_text_1:
                    user_text_1 += '.'
                if not operator_log1 and not operator_log2:
                    if not num1_used:
                        num1 = float(user_text_1)
                    else:
                        num2 = float(user_text_1)
            elif buttonCE.collidepoint(event.pos):
                if user_text_1 == 'x:' or user_text_1 == 'y:':
                    break
                user_text_1 = user_text_1[:-1]
                if 'x' in user_text_1 or 'y' in user_text_1:
                    break
                if num2_used and user_text_1 != '':
                    if type(num2) == float:
                        num2 = float(user_text_1)
                    else:
                        num2 = int(user_text_1)
                elif user_text_1 != '':
                    if type(num1) == float:
                        num1 = float(user_text_1)
                    else:
                        num1 = int(user_text_1)
            elif buttonC.collidepoint(event.pos):
                user_text_1 = ''
                num1 = 0
                num2 = 0
                num1_used = False
                num2_used = False
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = False
                operator_inv = False
                operator_log1 = False
                operator_log2 = False
                Sound.play()
            elif buttonPlusMinus.collidepoint(event.pos) and len(user_text_1) <= 6 and not operator_log1 and not operator_log2:
                if len(user_text_1) > 0:
                    if user_text_1[0] != '-':
                        user_text_1 = '-' + user_text_1
                    else:
                        user_text_1 = user_text_1[1:]
                else:
                    user_text_1 = '-'
                if user_text_1 != '-' and user_text_1 != '':
                    if num2_used:
                        if type(num2) == float:
                            num2 = float(user_text_1)
                        else:
                            num2 = int(user_text_1)
                    else:
                        if type(num1) == float:
                            num1 = float(user_text_1)
                        else:
                            num1 = int(user_text_1)


            elif buttonPlus.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                if user_text_1 == '':
                    break
                operator_add = True
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = False
                operator_inv = False
                if not num1_used:
                    num1_used = True
                    num2_used = False
                    user_text_1 = ''
                else:
                    num1_used = False
                    num2_used = True
                    num1 += num2
                    user_text_1 = str(num1)
                    if '.' in user_text_1:
                        num2 = float(user_text_1)
                    elif not 'j' in user_text_1:
                        num2 = int(user_text_1)
            elif buttonMinus.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                operator_add = False
                operator_sub = True
                operator_mult = False
                operator_div = False
                operator_exp = False
                operator_inv = False
                if not num1_used:
                    num1_used = True
                    num2_used = False
                    user_text_1 = ''
                else:
                    num1_used = False
                    num2_used = True
                    num1 -= num2
                    user_text_1 = str(num1)
                    if '.' in user_text_1:
                        num2 = float(user_text_1)
                    else:
                        num2 = int(user_text_1)
            elif buttonMult.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                operator_add = False
                operator_sub = False
                operator_mult = True
                operator_div = False
                operator_exp = False
                operator_inv = False
                if not num1_used:
                    num1_used = True
                    num2_used = False
                    user_text_1 = ''
                else:
                    num1_used = False
                    num2_used = True
                    num1 = myMult(num1, num2)
                    user_text_1 = str(num1)
                    if '.' in user_text_1:
                        num2 = float(user_text_1)
                    else:
                        num2 = int(user_text_1)
            elif buttonDiv.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                if user_text_1 == '':
                    break
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = True
                operator_exp = False
                operator_inv = False
                if not num1_used:
                    num1_used = True
                    num2_used = False
                    user_text_1 = ''
                else:
                    num1_used = False
                    num2_used = True
                    num1 = myDiv(num1, num2)
                    user_text_1 = str(num1)
                    if '.' in user_text_1:
                        num2 = float(user_text_1)
                    else:
                        num2 = int(user_text_1)
            elif buttonExp.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = True
                operator_inv = False
                if not num1_used:
                    num1_used = True
                    num2_used = False
                    user_text_1 = ''
                else:
                    num1_used = False
                    num2_used = True
                    num1 = myExp(num1, num2)
                    user_text_1 = str(num1)
                    if '.' in user_text_1:
                        num2 = float(user_text_1)
                    else:
                        num2 = int(user_text_1)
            elif buttonInv.collidepoint(event.pos) and not operator_log1 and not operator_log2:
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = False
                if '.' in user_text_1:
                    num2 = float(user_text_1)
                elif user_text_1 != '':
                    num2 = int(user_text_1)
                num1 = myInv(num1)
                if num1 == None:
                    num1 = 0
                if user_text_1 != '':
                    user_text_1 = str(num1)
                    Sound.play()
            elif buttonRoot.collidepoint(event.pos) and not operator_log1 and not operator_log2 and user_text_1 != '':
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = False
                if '.' in user_text_1:
                    num1 = float(user_text_1)
                    num1 = cmath.sqrt(num1)
                else:
                    num1 = cmath.sqrt(num1)
                num1validado = str(num1)
                if '+' in num1validado:
                    while '+' in num1validado:
                        num1validado = num1validado[:-1]
                    if '.' in num1validado:
                        num1 = float(num1validado[1:])
                    else:
                        num1 = int(num1validado[1:])
                Sound.play()
                user_text_1 = str(num1.real) if num2 >= 0 else str(num1)
            elif buttonLog.collidepoint(event.pos):
                operator_add = False
                operator_sub = False
                operator_mult = False
                operator_div = False
                operator_exp = False
                if not operator_log1:
                    operator_log1 = True
                    user_text_1 = 'x:'
                elif not operator_log2:
                    if user_text_1 == 'x:':
                        break
                    operator_log2 = True
                    if '.' in user_text_1:
                        num1 = float(user_text_1[2:])
                    else:
                        num1 = int(user_text_1[2:])
                    user_text_1 = 'y:'
                else:
                    operator_log1 = False
                    operator_log2 = False
                    if user_text_1 == 'y:':
                        break
                    if '.' in user_text_1:
                        num2 = float(user_text_1[2:])
                    else:
                        num2 = int(user_text_1[2:])
                    if num1 == 0 or num2 == 0:
                        user_text_1 = ''
                        break
                    user_text_1 = str(math.log(num1, num2))
                    Sound.play()
            elif buttonEq.collidepoint(event.pos):

                if operator_add:
                    if num1_used:
                        num1_used = False
                        num1 += num2
                        user_text_1 = str(num1)
                    else:
                        num1_used = True
                        num1 += num2
                        user_text_1 = str(num1)
                elif operator_sub:
                    if num1_used:
                        num1_used = False
                        num1 -= num2
                        user_text_1 = str(num1)
                    else:
                        num1_used = True
                        num1 -= num2
                        user_text_1 = str(num1)
                elif operator_mult:
                    if num1_used:
                        num1_used = False
                        num1 = myMult(num1, num2)
                        user_text_1 = str(num1)
                    else:
                        num1_used = True
                        num1 = myMult(num1, num2)
                        user_text_1 = str(num1)
                elif operator_div:
                    if num1_used:
                        num1_used = False
                        num1 = myDiv(num1, num2)
                        user_text_1 = str(num1)
                    else:
                        num1_used = True
                        num1 = myDiv(num1, num2)
                        user_text_1 = str(num1)
                elif operator_exp:
                    if num1_used:
                        num1_used = False
                        num1 = myExp(num1, num2)
                        user_text_1 = str(num1)
                    else:
                        num1_used = True
                        num1 = myExp(num1, num2)
                        user_text_1 = str(num1)
                Sound.play()






