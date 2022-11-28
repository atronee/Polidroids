import pygame # Importa o módulo pygame

from models import GameObject, Spaceship # Importa as classes GameObject e Spaceship do módulo models
from utils import load_sprite # Importa o método load_sprite do módulo utils

class Polidroids: # Classe principal do jogo
    def __init__(self): # Método construtor
        self._init_pygame() # Inicializa o pygame
        self.screen = pygame.display.set_mode((800, 600)) # Cria uma tela de 800x600
        self.background = load_sprite("background_space", False) # Carrega a imagem de fundo
        self.clock = pygame.time.Clock() # Cria um objeto Clock
        self.spaceship = Spaceship((400, 300)) # Cria uma instância da classe Spaceship
        self.asteroid = GameObject(
            (400, 300), load_sprite("hexagoid"), (1, 0)
        ) # Cria uma instância da classe GameObject para o asteroide
        self.enemy = GameObject(
            (400, 300), load_sprite("enemy_spaceship"), (0, 1)
        ) # Cria uma instância da classe GameObject para o inimigo

    def main_loop(self): # Método principal do jogo
        while True: # Cria um loop infinito
            self._handle_input() # Trata os eventos
            self._process_game_logic() # Processa a lógica do jogo
            self._draw() # Desenha na tela

    def _init_pygame(self): # Método inicializa o pygame
        pygame.init() # Inicializa o pygame
        pygame.display.set_caption("Polidroids") # Define o título da janela

    def _handle_input(self): # Método trata os eventos
        for event in pygame.event.get(): # Percorre todos os eventos
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ): # Verifica se o evento é de fechar a janela ou apertar a tecla ESC
                pygame.quit() # Fecha o jogo
                
        is_key_pressed = pygame.key.get_pressed() # Pega todas as teclas pressionadas

        if is_key_pressed[pygame.K_RIGHT]: # Verifica se a tecla direita está pressionada
            self.spaceship.rotate(clockwise=True) # Rotaciona a nave no sentido horário
        elif is_key_pressed[pygame.K_LEFT]: # Verifica se a tecla esquerda está pressionada
            self.spaceship.rotate(clockwise=False) # Rotaciona a nave no sentido anti-horário
        if is_key_pressed[pygame.K_UP]: # Verifica se a tecla para cima está pressionada
            self.spaceship.accelerate() # Acelera a nave

    def _process_game_logic(self): # Método processa a lógica do jogo
        self.spaceship.move(self.screen) # Move a nave

    def _draw(self): # Método desenha na tela
        self.screen.blit(self.background, (0, 0)) # Desenha a imagem de fundo na tela
        self.spaceship.draw(self.screen) # Desenha a nave na tela
        self.asteroid.draw(self.screen) # Desenha o asteroide na tela
        pygame.display.flip() # Atualiza a tela
        self.clock.tick(60)