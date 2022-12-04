import pygame, os
from States.state import State
from States.menu import Menu

class Gameplay(State):
    def __init__(self, game):
        State.__init__(self,game)
        self.backgroung = pygame.image.load(os.path.join(self.game.assets_dir, "Sprites", "background_space.png"))

    def update(self,delta_time, actions):
        # Check if the game was paused 
        if actions["start"]:
            new_state = Menu(self.game)
            new_state.enter_state()
        self.player.update(delta_time, actions)
    def render(self, display):
        display.blit(self.background, (0,0))