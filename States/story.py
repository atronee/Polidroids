import pygame, os
from States.state import State
from States.gameplay import Gameplay
from States.utils import load_sound, load_sprite 

class Story(State):
    def __init__(self, game, type):
        State.__init__(self, game)
        self.type = type
        self.background = load_sprite("background_space", 1)
        self.text_height = self.game.GAME_H
        self.clock = pygame.time.Clock() # Cria um objeto Clock
        self.font_size = 30
        self.soundtrack = load_sound("Game_soundtrack_2")

    def update(self, actions):     
        if actions["enter"]:
            self.transition_state()
        self.game.reset_keys()


    def render(self, display):
        self.soundtrack.play(20)
        display.blit(self.background, (0,0))
        self.game.draw_text(display, "Poligolândia era um planeta central", (255,255,255), self.game.GAME_W/2, (self.text_height), self.font_size)
        self.game.draw_text(display, "na galáxia em que tudo era feito de polígonos.", (255,255,255), self.game.GAME_W/2, (self.text_height + 50), self.font_size)
        self.game.draw_text(display, "Era um reino grande e rico,", (255,255,255), self.game.GAME_W/2, (self.text_height + 100), self.font_size)
        self.game.draw_text(display, "porém um dia foi destruído, já que não", (255,255,255), self.game.GAME_W/2, (self.text_height + 150), self.font_size)
        self.game.draw_text(display, "conseguirão evitar a chuva de asteroides", (255,255,255), self.game.GAME_W/2, (self.text_height + 200), self.font_size)
        self.game.draw_text(display, "que caiu sobre o planeta. Passam se 10 anos", (255,255,255), self.game.GAME_W/2, (self.text_height + 250), self.font_size)
        self.game.draw_text(display, "e agora os destroços do planeta estão", (255,255,255), self.game.GAME_W/2, (self.text_height + 300), self.font_size)
        self.game.draw_text(display, "espalhados pelo espaço.", (255,255,255), self.game.GAME_W/2, (self.text_height + 350), self.font_size)
        self.game.draw_text(display, "Milhões de pessoas de planetas próximos", (255,255,255), self.game.GAME_W/2, (self.text_height + 400), self.font_size)
        self.game.draw_text(display, "sofrem com as chuvas de polígonos", (255,255,255), self.game.GAME_W/2, (self.text_height + 450), self.font_size)
        self.game.draw_text(display, "que caem sobre eles. Então, você é", (255,255,255), self.game.GAME_W/2, (self.text_height + 500), self.font_size)
        self.game.draw_text(display, "contratado pelo Império Galáctico para", (255,255,255), self.game.GAME_W/2, (self.text_height + 550), self.font_size)
        self.game.draw_text(display, "destruir os asteroides que estão ameaçando", (255,255,255), self.game.GAME_W/2, (self.text_height + 600), self.font_size)
        self.game.draw_text(display, "a galáxia. Muitos falharam antes, levando", (255,255,255), self.game.GAME_W/2, (self.text_height + 650), self.font_size)
        self.game.draw_text(display, "então ao sumiço da Poligolândia.", (255,255,255), self.game.GAME_W/2, (self.text_height + 700), self.font_size)
        self.game.draw_text(display, "Lembre-se que estes polígonos não são mais", (255,255,255), self.game.GAME_W/2, (self.text_height + 750), self.font_size)
        self.game.draw_text(display, "pessoas, apenas uma sombra do que", (255,255,255), self.game.GAME_W/2, (self.text_height + 800), self.font_size)
        self.game.draw_text(display, "já foram. Você é o último herói que pode", (255,255,255), self.game.GAME_W/2, (self.text_height + 850), self.font_size)
        self.game.draw_text(display, "salvar a galáxia.", (255,255,255), self.game.GAME_W/2, (self.text_height + 900), self.font_size)
        self.game.draw_text(display, "Boa sorte!", (255,255,255), self.game.GAME_W/2, (self.text_height + 950), self.font_size)
        pygame.display.flip()
        self.text_height -= 0.5
        self.clock.tick(60) # Define o FPS

    def transition_state(self):
        self.soundtrack.stop()
        new_state = Gameplay(self.game, self.type)
        new_state.enter_state()