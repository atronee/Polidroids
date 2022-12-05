class State():
    def __init__(self, game):
        """Construtor da classe State"""
        self.game = game
        self.prev_state = None

    def update(self, actions):
        """Atualiza o estado do jogo
        param actions: dicionário de ações
        """
        pass
    def render(self, surface):
        """Renderiza o estado.
        param surface: tela do jogo
        """
        pass

    def enter_state(self):
        """Método chamado quando o estado é inserido na pilha de estados
        """
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        """Método chamado quando o estado é removido da pilha de estados
        """
        self.game.state_stack.pop()