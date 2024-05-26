
class ScreenBase():
    
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
    
    
    def handle_events(self, events):
        pass
    
    
    def update(self):
        pass
    
    
    def render(self, screen):
        pass
