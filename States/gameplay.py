import pygame, os
from States.state import State
from States.menu import Menu

class Gameplay(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.background = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))

    def update(self,delta_time, actions):
        # Check if the game was paused 
        if actions["enter"]:
            new_state = Menu(self.game)
            new_state.enter_state()
    def render(self, display):
        display.blit(self.background, (0,0))