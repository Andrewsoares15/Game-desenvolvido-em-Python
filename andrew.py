import pygame 

pygame.init()

win = pygame.display.set_mode((1282, 770))  # tamanho da tela
pygame.display.set_caption("FXP DA UNI")
pygame.mixer.music.load('Restos/music.mp3')
pygame.mixer.music.play(-1)
from inimigoAndrew import RedGuy
from inimigoAndrew import RedGuy2
from inimigoAndrew import RedGuy3
from inimigoAndrew import RedGuy4
from inimigoAndrew import RedGuy5
from inimigoAndrew import RedGuy6
from inimigoAndrew import RedGuy7
from inimigoAndrew import RedGuy8
from inimigoAndrew import RedGuy9
from inimigoAndrew import RedGuy10
from inimigoAndrew import RedGuy11
from inimigoAndrew import RedGuy12
from persoAndrew import Guy
from persoAndrew import Guy2
from persoAndrew import Guy3
from persoAndrew import Guy4
from persoAndrew import Guy5
from persoAndrew import Guy6
from persoAndrew import Guy7
from persoAndrew import Guy8
from persoAndrew import Guy9
from persoAndrew import Guy10
from persoAndrew import Guy11
from persoAndrew import Guy12
#jogarp = pygame.image.load("data/Imagens/jogarmarrom.png")
#jogarb = pygame.image.load("data/Imagens/jogarbranco.png")
#sairp = pygame.image.load("data/Imagens/SAIRp.png")
#sairb = pygame.image.load("data/Imagens/SAIRb.png")

ACERTOU = pygame.image.load('Restos/ACERTOU.png')

erroubotao = pygame.image.load('Restos/ERROUbotao.png')
acertoubotao = pygame.image.load('Restos/acertoubotao.png')


def jogo1():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg1()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

perguntafundo = pygame.image.load('Restos/pergunta.png')


def jogo2():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy2(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy2(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg2()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

def jogo3():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy3 = Guy3(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy3(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy3, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg3()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

def jogo4():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy3 = Guy4(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy4(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy3, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg4()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

def jogo5():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy5(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy5(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg5()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()
#perg1fundo = pygame.image.load('Restos/1pergunta.png')
#certo = pygame.image.load('Restos/certo.png')
#errado = pygame.image.load('Restos/errado.png')
def jogo6():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy6(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy6(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg6()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()
def jogo7():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 =Guy7(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy7(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg7()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()   

def jogo8():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy8(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy8(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg8()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()


def jogo9():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy9(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy9(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg9()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()
def jogo10():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy10(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy10(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg10()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()
def jogo11():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy11(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy11(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg11()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

def jogo12():
    fundo = pygame.image.load('Restos/mapacentral.jpg')
    # screen.blit(porqueimagem, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    # screen.blit(jogarp, (150, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    # screen.blit(sairp, (500, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    guy2 = Guy12(objectGroup)
    pygame.display.flip()
    nome = 0

    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False

        objectGroup.update()

        if nome == 0:
            RedGuy12(objectGroup, redguyGroup)

        collision = pygame.sprite.spritecollide(guy2, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            perg12()

        win.blit(fundo, (0, 0))  # Background
        # display.blit(texto, pos_texto)
        # display.blit(relogioimg, pos_relogio)
        # screen.blit(som, (870, 15))
        # display.blit(text, textRect)
        objectGroup.draw(win)
        pygame.display.update()

perguntafundo = pygame.image.load('Restos/pergunta.png')
perg1fundo = pygame.image.load('Restos/1pergunta.png')
certo = pygame.image.load('Restos/certo.png')
errado = pygame.image.load('Restos/errado.png')
errou = pygame.image.load('Restos/ERROU.png')
def perg1():
    win.blit(perg1fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                win.blit(errou, (0, 0))
                #quit()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                credito()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()

perg2fundo = pygame.image.load('Restos/2pergunta.png')

def perg2():
    win.blit(perg2fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito2()

            else:
                win.blit(certo, (300, 500))


        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()

perg3fundo = pygame.image.load('Restos/3pergunta.png')

def perg3():
    win.blit(perg3fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito3()

            else:
                win.blit(certo, (300, 500))


        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()

perg4fundo = pygame.image.load('Restos/4pergunta.png')

def perg4():
    win.blit(perg4fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                credito4()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg5fundo =  pygame.image.load('Restos/5pergunta.png')

def perg5():
    win.blit(perg5fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                credito5()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg6fundo = pygame.image.load('Restos/6pergunta.png')
def perg6():
    win.blit(perg6fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito6()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg7fundo = pygame.image.load('Restos/7pergunta.png')
def perg7():
    win.blit(perg7fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                credito7()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg8fundo = pygame.image.load('Restos/8pergunta.png')       
def perg8():
    win.blit(perg8fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito8()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg9fundo = pygame.image.load('Restos/9pergunta.png')       
def perg9():
    win.blit(perg9fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito9()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip() 
perg10fundo = pygame.image.load('Restos/10pergunta.png')
def perg10():
    win.blit(perg10fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito10()

            else:
                win.blit(certo, (300, 500))


        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()
perg11fundo = pygame.image.load('Restos/11pergunta.png')
def perg11():
    win.blit(perg11fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                credito11()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()

perg12fundo = pygame.image.load('Restos/12pergunta.png')
def perg12():
    win.blit(perg12fundo, (0, 0))
    # screen.blit(titulo, (WIDTH / 4, 50))
    win.blit(certo, (300, 500))
    # screen.blit(jogarb,(WIDTH /3,600))
    win.blit(errado, (650, 500))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()


    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 300 + 308 > mouse[0] > 300 and 500 + 112 > mouse[1] > 500:
            win.blit(certo, (300, 500))
            if pygame.mouse.get_pressed()[0]:
                credito12()

            else:
                win.blit(certo, (300, 500))

        if 650 + 215 > mouse[0] > 650 and 500 + 83 > mouse[1] > 500:
            win.blit(errado, (650, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            win.blit(errado, (650, 500))

        pygame.display.flip()            
vitoria = pygame.image.load('Restos/venceu.png')
def vitoriaf():
    win.fill((0,0,0))
    win.blit(vitoria, (0, 0))
    #win.blit(acertoubotao, (130, 400))
    win.blit(erroubotao, (600, 400))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        '''if 130 + 147 > mouse[0] > 130 and 400 + 148 > mouse[1] > 400:
            win.blit(acertoubotao, (130, 400))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(acertoubotao, (130, 400))
'''
        #347,348

        if 600 + 147 > mouse[0] > 600 and 400 + 148 > mouse[1] > 400:
            win.blit(erroubotao, (600, 400))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (600, 400))

        pygame.display.flip()

def credito12():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 400))
    win.blit(erroubotao, (740, 400))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 400 + 148 > mouse[1] > 400:
            win.blit(acertoubotao, (270, 400))
            if pygame.mouse.get_pressed()[0]:
                vitoriaf()


        else:
            win.blit(acertoubotao, (270, 400))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 400 + 148 > mouse[1] > 400:
            win.blit(erroubotao, (740, 400))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 400))

        pygame.display.flip()
def credito11():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo12()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()
def credito10():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo11()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()                
def credito9():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo10()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()         
def credito8():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo9()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()        
def credito7():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo8()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()
def credito6():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo7()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()        
def credito5():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo6()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()

def credito4():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo5()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()

def credito3():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo4()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()

def credito2():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo3()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()

def credito():
    win.fill((0,0,0))
    win.blit(ACERTOU, (0, 0))
    win.blit(acertoubotao, (270, 500))
    win.blit(erroubotao, (740, 500))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 270 + 147 > mouse[0] > 270 and 500 + 148 > mouse[1] > 500:
            win.blit(acertoubotao, (270, 500))
            if pygame.mouse.get_pressed()[0]:
                jogo2()


        else:
            win.blit(acertoubotao, (270, 500))

        #347,348

        if 740 + 147 > mouse[0] > 740 and 500 + 148 > mouse[1] > 500:
            win.blit(erroubotao, (740, 500))
            if pygame.mouse.get_pressed()[0]:
                win.blit(erroubotao, (740, 500))
                #0quit()


        else:
            win.blit(erroubotao, (740, 500))

        pygame.display.flip()

pygame.display.flip()

jogo1()
pygame.quit()
