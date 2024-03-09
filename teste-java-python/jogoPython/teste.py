import requests
import json
import pygame
from io import StringIO

#resposta = requests.get("http://localhost:8080/demo/all")
#resposta = StringIO(resposta.content.decode(encoding="utf-8"))

#json_banco = json.load(resposta)

#for i in json_banco:
#    print(i["name"])

pygame.init()

pygame.display.set_caption("My Game")


#Instancias
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700,500))
font = pygame.font.SysFont(None, 100)
get_key = ""
key_of_event = None

#Classes
class TextInput():
    def __init__(self):
        self.text = ""
        self.input_active = True
        self.box = pygame.Rect(100,100, 500, 200)
        self.font = pygame.font.SysFont(None, 100)
        
    def get_chosen(self):
        pos = pygame.mouse.get_pos()
        key = pygame.mouse.get_pressed()
        
        if pos[0] > 100 and pos[0] < 600 and pos[1] > 100 and pos[1] < 300:
            if key[0] == True:
                self.input_active = True
        elif key[0] == True:
            self.input_active = False
            
    def write(self, key):
        if self.input_active == True:  
            self.text += key
        
    def apagar(self):
        if self.input_active == True:  
            self.text = self.text[:-1]
        
    def update(self, screen, event_key):
        self.get_chosen()
        
        if event_key != None:
            if event_key.key == pygame.K_BACKSPACE:
                self.apagar()
            elif event_key.key != pygame.K_RETURN or event_key.key != pygame.K_BACKSPACE:
                self.write(event_key.unicode)
    

        pygame.draw.rect(screen, (200,20,20), self.box)
        self.text_surf = font.render(self.text, True, (255, 255, 255))
        screen.blit(self.text_surf, self.text_surf.get_rect(center = self.box.center))



class Botao():
    def __init__(self):
        self.box = pygame.Rect(250,350, 200, 100)
        self.click = False
        
        
    def update(self, screen, func, *args):
        pos = pygame.mouse.get_pos()
        key = pygame.mouse.get_pressed()
        
        
        if pos[0] > 250 and pos[0] < 450 and pos[1] > 350 and pos[1] < 450:
            if key[0] == True and self.click == False:
                self.click = True
                print('Clicado')
                func(args)
                
            elif key[0] == False:
                self.click = False

            
            
        pygame.draw.rect(screen, (100,100,0), self.box)
        
        
#Funções
def salvar(texto):
    requests.get(f"http://localhost:8080/demo/add/{texto}")

tx1 = TextInput()
b1 = Botao()

while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key_of_event = event

    tx1.update(screen, key_of_event)
    key_of_event = None
    
    b1.update(screen, salvar, tx1.text)
    pygame.display.flip()

    clock.tick(60)