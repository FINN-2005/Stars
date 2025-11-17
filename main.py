from pygame_template import *


# not very happy with this :(



SIZE = 15

def mm(x):
    return min(SIZE, max(0, x))

class Star(Sprite):

    b_vals = [[(i/SIZE-1)**2*(1-(j/SIZE)) for i in range(1, SIZE+1)] for j in range(int(SIZE//2))]
    b_vals = b_vals + list(reversed(b_vals))


    def __init__(self, pos = (APP.HW, APP.HH), *groups):
        super().__init__(*groups)

        self.image = pygame.Surface((SIZE*2,SIZE*2), pygame.SRCALPHA)
        self.rect = self.image.get_frect(center = pos)

        self.size = SIZE
        self.phase = 0

    def update(self, dt):
        self.rect.y += dt / 3
        if self.rect.y > APP.H + SIZE:
            self.kill()

        self.phase = (self.phase + 0.1337 * dt) % self.size

        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, Color.white, (self.size,self.size), 10)
        for r, b in enumerate(self.b_vals[int(mm(self.phase-1))], start=1): pygame.draw.circle(self.image, (255,255,255,int(b*255)), (self.size,self.size), r, 2)        



class run(APP):
    def setup(self):
        self.group = Group()

        for y in range(100):
            pos = random.randint(0, APP.W), random.randrange(0, 0 - APP.H, -1)
            self.group.add(Star(pos = pos))


    def update(self):
        self.group.update(self.dt)

    def draw(self):
        self.group.draw()

run()