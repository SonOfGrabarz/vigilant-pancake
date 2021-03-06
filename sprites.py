from settings import *
from random import choice

class PlayerClass(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, SCREEN_HEIGHT - 50)

        # position of player is calculated using a 2d vector
        self.position = vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        # player velocity
        self.velocity = vector(0, 0)
        # player acceleration
        self.acceleration = vector(0, 0)

    def jump(self):

        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1

        if len(collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.game.jump_sound.play()
            self.velocity.y = -10


    def update(self):

        self.calc_gravity()

        self.rect.x += self.velocity.x

        # checking vertical collisions
        collisions_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for plat in collisions_list:
            if self.velocity.x > 0:
                self.rect.right = plat.rect.left
            elif self.velocity.x < 0:
                self.rect.left = plat.rect.right

        self.rect.y += self.velocity.y

        # checking horizontal collisions
        collisions_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for plat in collisions_list:
            if self.velocity.y > 0:
                self.rect.bottom = plat.rect.top
            elif self.velocity.y < 0:
                self.rect.top = plat.rect.bottom

            self.velocity.y = 0

    def calc_gravity(self):

        if self.velocity.y == 0:
            self.velocity.y = 1
        else:
            self.velocity.y += 0.35

        # check if player standing on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.velocity.y >= 0:
            self.velocity.y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    # movement methods
    def left(self):
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert_alpha()
        self.velocity.x = -player_velocity

    def right(self):
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite2.png')).convert_alpha()
        self.velocity.x = player_velocity

    def stop(self):
        self.velocity.x = 0

# base level building objects
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, path, width=0, height=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites', path)).convert_alpha()
        platforma = pygame.Surface((width, height))

        platforma.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# when player touches EndPlatform, proceed to next level
class EndPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0):
        super(EndPlatform, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites', 'flag.png')).convert_alpha()
        flag = pygame.Surface((width, height))

        flag.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# kill player sprite when collision detected
class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y, path, width=0, height=0):
        super(Spikes, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites', path)).convert_alpha()
        spikes = pygame.Surface((width, height))

        spikes.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class GoldPoints(pygame.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0):
        super(GoldPoints, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites', 'item.png')).convert_alpha()
        point = pygame.Surface((width, height))

        point.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.type = choice(['gold'])

class SilverPoints(pygame.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0):
        super(SilverPoints, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites', 'item2.png')).convert_alpha()
        point = pygame.Surface((width, height))

        point.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.type = choice(['silver'])

class BoostPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, width=0, height=0):
        super(BoostPoint, self).__init__()
        self.image = pygame.image.load(os.path.join('sprites', 'cookie.png')).convert_alpha()
        point = pygame.Surface((width, height))

        point.blit(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
