import pygame
from pygame.locals import *
import random

pygame.init()

# Cores
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Configuração da tela
LARGURA, ALTURA = 640, 480
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Cobrinha')

# Inicialização da cobra
cobra = [pygame.Rect(100, 50, 20, 20)]
cobra_direcao = (1, 0)

# Inicialização do alimento
alimento = pygame.Rect(random.randint(0, LARGURA // 20 - 1) * 20, random.randint(0, ALTURA // 20 - 1) * 20, 20, 20)

# Variável de velocidade
velocidade = 5

def colisao_cobrinha():
    return any(segment.colliderect(cobra[0]) for segment in cobra[1:])

pontos = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[K_LEFT] and cobra_direcao != (1, 0):
        cobra_direcao = (-1, 0)
    if teclas[K_RIGHT] and cobra_direcao != (-1, 0):
        cobra_direcao = (1, 0)
    if teclas[K_UP] and cobra_direcao != (0, 1):
        cobra_direcao = (0, -1)
    if teclas[K_DOWN] and cobra_direcao != (0, -1):
        cobra_direcao = (0, 1)

    nova_cabeca = pygame.Rect(cobra[0].x + cobra_direcao[0] * velocidade, cobra[0].y + cobra_direcao[1] * velocidade, 20, 20)
    cobra.insert(0, nova_cabeca)

    if cobra[0].colliderect(alimento):
        pontos += 1
        alimento = pygame.Rect(random.randint(0, LARGURA // 20 - 1) * 20, random.randint(0, ALTURA // 20 - 1) * 20, 20, 20)
    else:
        cobra.pop()

    if colisao_cobrinha() or cobra[0].left < 0 or cobra[0].right > LARGURA or cobra[0].top < 0 or cobra[0].bottom > ALTURA:
        rodando = False

    TELA.fill(PRETO)
    pygame.draw.rect(TELA, VERMELHO, alimento)
    for segment in cobra:
        pygame.draw.rect(TELA, VERMELHO, segment)

    pygame.display.flip()

pygame.quit()
