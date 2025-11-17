from pygame_template import *

class Star(Sprite):
    def __init__(self, pos=(APP.HW, APP.HH), *groups):
        super().__init__(*groups)
        self.size = random.randint(8, 20)
        self.image = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        self.rect = self.image.get_frect(center=pos)

        self.phase = random.random() * math.tau  # tau = 2*pi

    def update(self, dt):
        self.rect.y += dt / 3
        if self.rect.y > APP.H + self.size:
            self.kill()

        self.phase = (self.phase + 0.003 * dt) % math.tau

        self.image.fill((0,0,0,0))
        for r in range(1, self.size):
            brightness = (math.sin((r / self.size) * math.pi + self.phase) + 1) / 2
            color = (255, 255, 255, int(brightness * 255))
            pygame.draw.circle(self.image, color, (self.size, self.size), r, 1)

class run(APP):
    def setup(self):
        self.group = Group()
        for _ in range(100):
            pos = random.randint(0, APP.W), random.randrange(-APP.H, 0)
            self.group.add(Star(pos=pos))

    def update(self):
        self.group.update(self.dt)

    def draw(self):
        self.group.draw()

run()
