import random # Importa a biblioteca random
from pygame.image import load # Importa o método load do módulo image do pygame
from pygame.math import Vector2 # Importa o módulo math do pygame
from pygame.mixer import Sound # Importa o módulo mixer do pygame
import pygame

def load_sprite(name, scale, with_alpha=True): # Método carrega uma imagem
    """Carrega uma imagem
    :param name: nome do arquivo da imagem
    :type name: str
    :param scale: escala da imagem
    :type scale: float
    :param with_alpha: se a imagem possui transparência
    :type with_alpha: bool
    """
    path = f"Assets/Sprites/{name}.png" # Define o caminho da imagem
    loaded_sprite = load(path) # Carrega a imagem
    loaded_sprite = pygame.transform.scale(loaded_sprite, (loaded_sprite.get_size()[0]*scale, loaded_sprite.get_size()[1]*scale)) # Define o tamanho da imagem
    if with_alpha:
        return loaded_sprite.convert_alpha() # Retorna a imagem convertida com alpha
    else: 
        return loaded_sprite.convert() # Retorna a imagem convertida
    
def wrap_position(position, surface): # Método retorna a posição do objeto dentro da tela
    """Retorna a posição do objeto dentro da tela
    :param position: posição do objeto
    :type position: Vector2
    :param surface: superfície onde o objeto está
    :type surface: Surface
    """
    x, y = position # Desempacota a posição
    w, h = surface.get_size() # Calcula o tamanho da tela
    return Vector2(x % w, y % h) # Retorna a posição dentro da tela

def get_random_position(surface): # Método retorna uma posição aleatória dentro da tela
    """Retorna uma posição aleatória dentro da tela
    :param surface: superfície onde o objeto está
    :type surface: Surface
    """
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()))
    
def get_random_velocity(min_speed, max_speed): # Método retorna uma velocidade aleatória
    """Retorna uma velocidade aleatória
    :param min_speed: velocidade mínima
    :type min_speed: int
    :param max_speed: velocidade máxima
    :type max_speed: int
    """
    speed = random.randint(min_speed, max_speed) # Calcula a velocidade
    angle = random.randrange(0, 360) # Calcula o ângulo
    return Vector2(speed, 0).rotate(angle) # Retorna a velocidade

def load_sound(name): # Método para carregar músicas e sons do jogo
    """Carrega uma música ou som
    :param name: nome do arquivo da música ou som
    :type name: str
    """
    path = f"Assets/Soundtrack/{name}.mp3" # Especifica o caminho para acessar o arquivo de áudio
    return Sound(path) # Retorna o arquivo de áudio carregado
