from pygame.image import load # Importa o método load do módulo image do pygame

def load_sprite(name, with_alpha=True): # Método carrega uma imagem
    path = f"Assets/Sprites/{name}.png" # Define o caminho da imagem
    loaded_sprite = load(path) # Carrega a imagem

    if with_alpha:
        return loaded_sprite.convert_alpha() # Retorna a imagem convertida com alpha
    else: 
        return loaded_sprite.convert() # Retorna a imagem convertida