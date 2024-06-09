
class ScreenManager():
    
    def __init__(self):
        self.screens = {}
        self.current_screen = None
        self.running = True
        
    
    def add_screen(self, name, screen):
        self.screens[name] = screen

    
    def set_screen(self, name):
        self.current_screen = self.screens[name]
        
    
    def handle_events(self, events):
        if self.current_screen:
            self.current_screen.handle_events(events)
            
    
    def update(self):
        if self.current_screen:
            self.current_screen.update()


    def render(self, screen):
        if self.current_screen:
            self.current_screen.render(screen)