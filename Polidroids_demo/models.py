from pygame.math import Vector2 # Importa o módulo math do pygame

class GameObject: # Classe base para todos os objetos do jogo
    def __init__(self, position, sprite, velocity): # Método construtor
        self.position = Vector2(position) # Define a posição do objeto
        self.sprite = sprite # Define a imagem do objeto
        self.radius = sprite.get_width() / 2 # Define o raio do objeto
        self.velocity = Vector2(velocity) # Define a velocidade do objeto

    def draw(self, surface): # Método desenha o objeto na tela
        blit_position = self.position - Vector2(self.radius) # Define a posição do objeto
        surface.blit(self.sprite, blit_position) # Desenha o objeto na tela

    def move(self): # Método move o objeto
        self.position = self.position + self.velocity # Atualiza a posição do objeto

    def collides_with(self, other_obj): # Método verifica se o objeto colidiu com outro objeto
        distance = self.position.distance_to(other_obj.position) # Calcula a distância entre os objetos
        return distance < self.radius + other_obj.radius # Retorna se a distância é menor que a soma dos raios