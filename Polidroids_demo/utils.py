from pygame.image import load # Importa o método load do módulo image do pygame
from pygame.math import Vector2 # Importa o módulo math do pygame

def load_sprite(name, with_alpha=True): # Método carrega uma imagem
    path = f"Assets/Sprites/{name}.png" # Define o caminho da imagem
    loaded_sprite = load(path) # Carrega a imagem

    if with_alpha:
        return loaded_sprite.convert_alpha() # Retorna a imagem convertida com alpha
    else: 
        return loaded_sprite.convert() # Retorna a imagem convertida
    
def wrap_position(position, surface): # Método retorna a posição do objeto dentro da tela
    x, y = position # Desempacota a posição
    w, h = surface.get_size() # Calcula o tamanho da tela
    return Vector2(x % w, y % h) # Retorna a posição dentro da tela