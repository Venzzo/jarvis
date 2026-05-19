import math
import random
import pygame
import numpy as np
import visual.state as state

# =========================
# INICIALIZAÇÃO
# =========================

pygame.init()

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Lary")

clock = pygame.time.Clock()


# =========================
# CENTRO DA TELA
# =========================

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


# =========================
# CONFIGURAÇÕES DA ORB
# =========================

RADIUS = 250
PARTICLE_COUNT = 900

PARTICLES = []


# =========================
# GERAR PARTÍCULAS
# =========================

for _ in range(PARTICLE_COUNT):

    theta = random.uniform(0, math.pi * 2)
    phi = random.uniform(0, math.pi)

    x = RADIUS * math.sin(phi) * math.cos(theta)
    y = RADIUS * math.cos(phi)
    z = RADIUS * math.sin(phi) * math.sin(theta)

    PARTICLES.append([x, y, z])


# =========================
# VARIÁVEIS DE ANIMAÇÃO
# =========================

angle = 0


# =========================
# LOOP PRINCIPAL
# =========================

running = True

while running:

    clock.tick(60)

    # fundo escuro
    screen.fill((8, 4, 18))

    # fechar janela
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # =========================
    # ESTADOS DA IA
    # =========================

    if state.STATE == "idle":

        rotation_speed = 0.008
        orb_color = (255, 120, 255)
        pulse_strength = 10

    elif state.STATE == "listening":

        rotation_speed = 0.015
        orb_color = (100, 180, 255)
        pulse_strength = 18

    elif state.STATE == "thinking":

        rotation_speed = 0.03
        orb_color = (180, 100, 255)
        pulse_strength = 25

    elif state.STATE == "speaking":

        rotation_speed = 0.02
        orb_color = (255, 180, 255)
        pulse_strength = 35 + state.VOLUME

    else:

        rotation_speed = 0.008
        orb_color = (255, 120, 255)
        pulse_strength = 10


    angle += rotation_speed

    # pulsação viva
    pulse = (
        math.sin(
            pygame.time.get_ticks() * 0.003
        ) * pulse_strength
)

    # desenhar partículas
    for particle in PARTICLES:

        x, y, z = particle

        # rotação eixo Y
        rotated_x = (
            x * math.cos(angle)
            - z * math.sin(angle)
        )

        rotated_z = (
            x * math.sin(angle)
            + z * math.cos(angle)
        )

        # profundidade fake 3D
        depth = 700 / (700 + rotated_z)

        projected_x = int(rotated_x * depth + CENTER_X)
        projected_y = int(y * depth + CENTER_Y)

        # tamanho baseado na profundidade
        size = max(
            1,
            int((4 * depth) + pulse * 0.05)
        )

        # brilho baseado na profundidade
        brightness = min(
            255,
            int((200 * depth) + 55)
        )

        # cor neon roxa
        color = (
            brightness,
            brightness // 2,
            255
        )

        pygame.draw.circle(
            screen,
            color,
            (projected_x, projected_y),
            size
        )

    # =========================
    # TEXTO STATUS
    # =========================

    font = pygame.font.SysFont(
        "Arial",
        30
    )

    text = font.render(
        "LARY ONLINE",
        True,
        (220, 180, 255)
    )

    screen.blit(
        text,
        (CENTER_X - 110, HEIGHT - 90)
    )

    # atualizar tela
    pygame.display.flip()


pygame.quit()