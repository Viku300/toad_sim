import pygame
import math
import sys
import random
import os
pygame.init()
SCREEN_W, SCREEN_H = 1920, 1080
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Toad Sim")
clock = pygame.time.Clock()
WORLD_W, WORLD_H = 8192, 2304
BASE = os.path.dirname(os.path.abspath(__file__))
BG_PATH               = os.path.join(BASE, "pond_background.png")
MASK_PATH             = os.path.join(BASE, "pond_mask.png")
DIRTY_PATH            = os.path.join(BASE, "pond_dirty.png")
FISHZONE_PATH         = os.path.join(BASE, "pond_fishzone.png")
CRABZONE_PATH         = os.path.join(BASE, "crab_zone.png")
GRASSHOPPER_SPAWN_PATH= os.path.join(BASE, "grasshopper_spawn.png")
TADPOLE_R             = os.path.join(BASE, "tadpole_right.png")
FROGLET_R             = os.path.join(BASE, "froglet_right.png")
FROGLET_BOOST_R       = os.path.join(BASE, "froglet_boost_right.png")
FROGLET_EAT_PATH      = os.path.join(BASE, "froglet_eat.png")
TOAD_R                = os.path.join(BASE, "toad_right.png")
TOAD_L                = os.path.join(BASE, "toad_left.png")
TOAD_EAT_PATH         = os.path.join(BASE, "toad_eat.png")
FISH_L                = os.path.join(BASE, "fish_left1.png")
FISH_ANGRY_L          = os.path.join(BASE, "fish_left_angry1.png")
CRAB_R                = os.path.join(BASE, "crab_right.png")
GRASSHOPPER_R         = os.path.join(BASE, "grasshopper_right.png")
GRASSHOPPER_L         = os.path.join(BASE, "grasshopper_left.png")
LARVAE_COL = (20, 20, 20)
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
GOLD       = (255, 215, 0)
TADPOLE_MAX_HP      = 100
TADPOLE_MAX_HUNGER  = 100
TADPOLE_SPEED       = 4.5
TADPOLE_FRAME_W     = 64
TADPOLE_FRAME_H     = 64
TADPOLE_FRAME_COUNT = 4
FROGLET_MAX_HP      = 150
FROGLET_MAX_HUNGER  = 200
FROGLET_SPEED       = 4.5
FROGLET_BOOST_SPEED = 9.0
FROGLET_FRAME_W     = 128
FROGLET_FRAME_H     = 128
FROGLET_FRAME_COUNT = 6
BOOST_FRAME_W     = 128
BOOST_FRAME_H     = 128
BOOST_FRAME_COUNT = 15
BOOST_FRAME_DELAY = 8
BOOST_COOLDOWN    = 600
TOAD_MAX_HP      = 200
TOAD_MAX_HUNGER  = 300
TOAD_SPEED       = 3.5
TOAD_FRAME_W     = 128
TOAD_FRAME_H     = 128
TOAD_FRAME_COUNT = 5
FISH_FRAME_W     = 256
FISH_FRAME_H     = 256
FISH_FRAME_COUNT = 13
FISH_FRAME_DELAY = 6
CRAB_FRAME_W     = 256
CRAB_FRAME_H     = 256
CRAB_FRAME_COUNT = 9
CRAB_FRAME_DELAY = 5
CRAB_SPEED       = 6.5
CRAB_PATROL_SPEED= 1.8
CRAB_SIGHT_RANGE = 220
CRAB_HALF_CONE   = math.radians(90)
CRAB_BITE_DIST   = 60
CRAB_DAMAGE      = 30
CRAB_RETURN_TIME = 360
GRASSHOPPER_FRAME_W     = 60                    
GRASSHOPPER_FRAME_H     = 36
GRASSHOPPER_FRAME_COUNT = 4
GRASSHOPPER_FRAME_DELAY = 18                         
GRASSHOPPER_SPEED       = 0.6                     
GRASSHOPPER_WANDER_RAD  = 70                                                 
GRASSHOPPER_HITBOX      = 22                                             
GRASSHOPPER_POINTS      = 15                                     
GRASSHOPPER_MAX         = 2                                
GRASSHOPPER_RESPAWN     = 420                                               
FROGLET_EAT_FRAME_W     = 256                    
FROGLET_EAT_FRAME_H     = 128
FROGLET_EAT_FRAME_COUNT = 7
FROGLET_EAT_FRAME_DELAY = 5                                                     
TOAD_EAT_FRAME_W     = 256                    
TOAD_EAT_FRAME_H     = 128
TOAD_EAT_FRAME_COUNT = 7
TOAD_EAT_FRAME_DELAY = 5
TONGUE_MAX_LENGTH        = 200                                                       
TONGUE_EXTENSION = [0.0, 0.35, 0.70, 1.0, 0.70, 0.35, 0.0]
FRAME_DELAY       = 8
DIRTY_DAMAGE      = 15
FISH_PATROL_SPEED = 1.4
FISH_CHASE_SPEED  = TADPOLE_SPEED
FISH_SEP_RADIUS   = 80
FISH_SEP_STRENGTH = 0.6
LARVAE_COUNT      = 25
LARVAE_POINTS     = 2
EAT_RADIUS        = 18
RETURN_TIMEOUT    = 420
FISH_TURN_PATROL       = 0.025
FISH_TURN_CHASE        = 0.11
FISH_TURN_RETURN       = 0.04
FISH_CHASE_SLOW_RADIUS = 140
FISH_CHASE_STOP_RADIUS = 28
BITE_DIST              = 50
print("Loading pond assets... please wait")
background    = pygame.image.load(BG_PATH).convert()
mask_surf     = pygame.image.load(MASK_PATH).convert()
dirty_surf    = pygame.image.load(DIRTY_PATH).convert()
fishzone_surf = pygame.image.load(FISHZONE_PATH).convert()
crabzone_surf = pygame.image.load(CRABZONE_PATH).convert()
gh_spawn_surf = pygame.image.load(GRASSHOPPER_SPAWN_PATH).convert()
pond_mask      = pygame.mask.from_threshold(mask_surf,     (255, 255, 255), (40, 40, 40))
dirty_mask     = pygame.mask.from_threshold(dirty_surf,    (255,   0,   0), (40, 40, 40))
fishzone_mask  = pygame.mask.from_threshold(fishzone_surf, (  0,   0, 255), (40, 40, 40))
crab_zone_mask = pygame.mask.from_threshold(crabzone_surf, (255, 128,   0), (55, 80, 50))
gh_zone_mask   = pygame.mask.from_threshold(gh_spawn_surf, (  0, 255,   0), (15, 15, 15))
del mask_surf, dirty_surf, fishzone_surf
def load_frames(path, frame_w, frame_h, count, flip_h=False):
    sheet  = pygame.image.load(path).convert_alpha()
    frames = []
    for i in range(count):
        frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
        frame.blit(sheet, (0, 0), (i * frame_w, 0, frame_w, frame_h))
        if flip_h:
            frame = pygame.transform.flip(frame, True, False)
        frames.append(frame)
    return frames
tadpole_frames       = load_frames(TADPOLE_R,       TADPOLE_FRAME_W,  TADPOLE_FRAME_H,  TADPOLE_FRAME_COUNT)
froglet_frames       = load_frames(FROGLET_R,       FROGLET_FRAME_W,  FROGLET_FRAME_H,  FROGLET_FRAME_COUNT)
froglet_boost_frames = load_frames(FROGLET_BOOST_R, BOOST_FRAME_W,    BOOST_FRAME_H,    BOOST_FRAME_COUNT)
toad_frames          = load_frames(TOAD_R,           TOAD_FRAME_W,     TOAD_FRAME_H,     TOAD_FRAME_COUNT)
fish_frames_base     = load_frames(FISH_L,       FISH_FRAME_W, FISH_FRAME_H, FISH_FRAME_COUNT, flip_h=True)
fish_angry_frames    = load_frames(FISH_ANGRY_L, FISH_FRAME_W, FISH_FRAME_H, FISH_FRAME_COUNT, flip_h=True)
crab_frames          = load_frames(CRAB_R, CRAB_FRAME_W, CRAB_FRAME_H, CRAB_FRAME_COUNT)
grasshopper_r_frames = load_frames(GRASSHOPPER_R, GRASSHOPPER_FRAME_W, GRASSHOPPER_FRAME_H, GRASSHOPPER_FRAME_COUNT)
grasshopper_l_frames = load_frames(GRASSHOPPER_L, GRASSHOPPER_FRAME_W, GRASSHOPPER_FRAME_H, GRASSHOPPER_FRAME_COUNT)
froglet_eat_frames = load_frames(FROGLET_EAT_PATH, FROGLET_EAT_FRAME_W, FROGLET_EAT_FRAME_H,
                                  FROGLET_EAT_FRAME_COUNT, flip_h=True)
toad_eat_frames = load_frames(TOAD_EAT_PATH, TOAD_EAT_FRAME_W, TOAD_EAT_FRAME_H,
                               TOAD_EAT_FRAME_COUNT, flip_h=True)
print("Assets ready!")
def find_blob_centres(surf, is_target_fn, skip_r=200, scan_step=6):
    w, h = surf.get_size()
    centres = []
    for y in range(0, h, scan_step):
        for x in range(0, w, scan_step):
            if not is_target_fn(x, y, surf):
                continue
            if any(math.hypot(x - cx, y - cy) < skip_r for cx, cy in centres):
                continue
            sx = sy = count = 0
            r = int(skip_r)
            for by in range(max(0, y - r), min(h, y + r), 4):
                for bx in range(max(0, x - r), min(w, x + r), 4):
                    if math.hypot(bx - x, by - y) < r and is_target_fn(bx, by, surf):
                        sx += bx; sy += by; count += 1
            if count > 0:
                centres.append((float(sx // count), float(sy // count)))
    return centres
def _is_orange(x, y, surf):
    r, g, b = surf.get_at((x, y))[:3]
    return r > 200 and 60 < g < 200 and b < 60
def _is_green(x, y, surf):
    r, g, b = surf.get_at((x, y))[:3]
    return r < 20 and g > 200 and b < 20
print("Scanning crab zones...")
crab_spawn_positions = find_blob_centres(crabzone_surf, _is_orange, skip_r=600, scan_step=6)
print(f"  {len(crab_spawn_positions)} crab spawns found")
print("Scanning lily pad positions...")
lily_pad_positions = find_blob_centres(gh_spawn_surf, _is_green, skip_r=180, scan_step=6)
print(f"  {len(lily_pad_positions)} lily pads found")
del crabzone_surf, gh_spawn_surf                                   
def is_in_water(x, y):
    ix, iy = int(x), int(y)
    if 0 <= ix < WORLD_W and 0 <= iy < WORLD_H:
        return pond_mask.get_at((ix, iy)) == 1
    return False
def is_dirty(x, y):
    ix, iy = int(x), int(y)
    if 0 <= ix < WORLD_W and 0 <= iy < WORLD_H:
        return dirty_mask.get_at((ix, iy)) == 1
    return False
def is_in_fishzone(x, y):
    ix, iy = int(x), int(y)
    if 0 <= ix < WORLD_W and 0 <= iy < WORLD_H:
        return fishzone_mask.get_at((ix, iy)) == 1
    return False
def is_in_crab_zone(x, y):
    ix, iy = int(x), int(y)
    if 0 <= ix < WORLD_W and 0 <= iy < WORLD_H:
        return crab_zone_mask.get_at((ix, iy)) == 1
    return False
def is_in_gh_zone(x, y):
    ix, iy = int(x), int(y)
    if 0 <= ix < WORLD_W and 0 <= iy < WORLD_H:
        return gh_zone_mask.get_at((ix, iy)) == 1
    return False
def lerp_angle(current, target, speed):
    diff = (target - current + math.pi) % (2 * math.pi) - math.pi
    return current + diff * speed
def find_water_pos(px, py, need_fishzone=False):
    check = lambda x, y: is_in_water(x, y) and (not need_fishzone or is_in_fishzone(x, y))
    if check(px, py): return px, py
    for r in range(20, 600, 20):
        for deg in range(0, 360, 10):
            tx = px + r * math.cos(math.radians(deg))
            ty = py + r * math.sin(math.radians(deg))
            if check(tx, ty): return tx, ty
    return px, py
def draw_at_head(surface, frame, angle_deg, sx, sy, frame_w):
    """Rotate sprite so its right-edge head stays at (sx, sy)."""
    half_w  = frame_w // 2
    rad     = math.radians(-angle_deg)
    ox      = half_w * math.cos(rad)
    oy      = half_w * math.sin(rad)
    rotated = pygame.transform.rotate(frame, angle_deg)
    rw, rh  = rotated.get_size()
    surface.blit(rotated, (int(sx - ox - rw // 2), int(sy - oy - rh // 2)))
def draw_at_center(surface, frame, angle_deg, sx, sy):
    """Rotate sprite around its own centre and place centre at (sx, sy)."""
    rotated = pygame.transform.rotate(frame, angle_deg)
    surface.blit(rotated, rotated.get_rect(center=(sx, sy)))
class Larva:
    def __init__(self):
        self.x, self.y  = self._random_water_pos()
        self.angle      = random.uniform(0, 2 * math.pi)
        self.speed      = random.uniform(0.4, 1.0)
        self.turn_timer = random.randint(30, 120)
        self.length     = random.randint(6, 10)
        self.alive      = True
    def _random_water_pos(self):
        for _ in range(200):
            x = random.randint(100, WORLD_W - 100)
            y = random.randint(100, WORLD_H - 100)
            if is_in_water(x, y) and not is_dirty(x, y):
                return float(x), float(y)
        return float(WORLD_W // 2), float(WORLD_H // 2)
    def update(self):
        self.turn_timer -= 1
        if self.turn_timer <= 0:
            self.angle     += random.uniform(-math.pi * 0.6, math.pi * 0.6)
            self.turn_timer = random.randint(40, 140)
        nx = self.x + math.cos(self.angle) * self.speed
        ny = self.y + math.sin(self.angle) * self.speed
        if is_in_water(nx, ny): self.x, self.y = nx, ny
        else: self.angle += math.pi + random.uniform(-0.5, 0.5)
    def draw(self, surface, cam):
        sx = int(self.x - cam.x); sy = int(self.y - cam.y)
        if not (-20 < sx < SCREEN_W + 20 and -20 < sy < SCREEN_H + 20): return
        tx = int(sx - math.cos(self.angle) * self.length)
        ty = int(sy - math.sin(self.angle) * self.length)
        pygame.draw.line(surface, LARVAE_COL, (sx, sy), (tx, ty), 2)
        pygame.draw.circle(surface, LARVAE_COL, (sx, sy), 3)
def make_larvae():
    return [Larva() for _ in range(LARVAE_COUNT)]
class Grasshopper:
    def __init__(self, origin_x, origin_y):
        self.origin_x    = float(origin_x)
        self.origin_y    = float(origin_y)
        self.x           = float(origin_x)
        self.y           = float(origin_y)
        self.angle       = random.uniform(0, 2 * math.pi)
        self.facing_right= True                                             
        self.wander_timer= random.randint(60, 200)
        self.anim_frame  = 0
        self.anim_timer  = 0
        self.alive       = True
    def update(self):
        self.wander_timer -= 1
        if self.wander_timer <= 0:
            self.angle       = random.uniform(0, 2 * math.pi)
            self.wander_timer= random.randint(60, 200)
        self.facing_right = math.cos(self.angle) >= 0
        nx = self.x + math.cos(self.angle) * GRASSHOPPER_SPEED
        ny = self.y + math.sin(self.angle) * GRASSHOPPER_SPEED
        dist_from_origin = math.hypot(nx - self.origin_x, ny - self.origin_y)
        if is_in_gh_zone(nx, ny) and dist_from_origin <= GRASSHOPPER_WANDER_RAD:
            self.x, self.y = nx, ny
        else:
            self.angle = random.uniform(0, 2 * math.pi)
        self.anim_timer += 1
        if self.anim_timer >= GRASSHOPPER_FRAME_DELAY:
            self.anim_timer = 0
            self.anim_frame = (self.anim_frame + 1) % GRASSHOPPER_FRAME_COUNT
    def draw(self, surface, cam):
        sx = int(self.x - cam.x); sy = int(self.y - cam.y)
        if not (-100 < sx < SCREEN_W + 100 and -100 < sy < SCREEN_H + 100): return
        frames = grasshopper_r_frames if self.facing_right else grasshopper_l_frames
        frame  = frames[self.anim_frame]
        surface.blit(frame, frame.get_rect(center=(sx, sy)))
class Camera:
    def __init__(self):
        self.x = float(WORLD_W // 2)
        self.y = float(WORLD_H // 2)
    def update(self, target_x, target_y):
        tx = max(0, min(WORLD_W - SCREEN_W, target_x - SCREEN_W // 2))
        ty = max(0, min(WORLD_H - SCREEN_H, target_y - SCREEN_H // 2))
        self.x += (tx - self.x) * 0.10
        self.y += (ty - self.y) * 0.10
    @property
    def ix(self): return int(self.x)
    @property
    def iy(self): return int(self.y)
class Player:
    def __init__(self):
        sx, sy = find_water_pos(WORLD_W * 0.12, WORLD_H * 0.5)
        self.x  = float(sx); self.y = float(sy)
        self.vx = 0.0;       self.vy = 0.0
        self.stage      = "tadpole"
        self.max_health = TADPOLE_MAX_HP
        self.max_hunger = TADPOLE_MAX_HUNGER
        self.base_speed = TADPOLE_SPEED
        self.health     = float(TADPOLE_MAX_HP)
        self.hunger     = 0.0
        self.angle_deg    = 0.0
        self.hit_timer    = 0
        self.dirty_timer  = 0
        self.anim_frame   = 0
        self.anim_timer   = 0
        self.moving       = False
        self.evolve_flash = 0
        self.won          = False
        self.boosting         = False
        self.boost_frame      = 0
        self.boost_anim_timer = 0
        self.boost_cooldown   = 0
        self.boost_angle_deg  = 0.0
        self.eating        = False
        self.eat_frame     = 0
        self.eat_anim_timer= 0
        self.tongue_hit_done = False                                                           
    def evolve_to_froglet(self):
        self.stage = "froglet"; self.max_health = FROGLET_MAX_HP
        self.max_hunger = FROGLET_MAX_HUNGER; self.base_speed = FROGLET_SPEED
        self.health = min(self.health + 50, FROGLET_MAX_HP)
        self.hunger = 0.0; self.anim_frame = 0; self.anim_timer = 0
        self.evolve_flash = 90
    def evolve_to_toad(self):
        self.stage = "toad"; self.max_health = TOAD_MAX_HP
        self.max_hunger = TOAD_MAX_HUNGER; self.base_speed = TOAD_SPEED
        self.health = min(self.health + 50, TOAD_MAX_HP)
        self.hunger = 0.0; self.anim_frame = 0; self.anim_timer = 0
        self.evolve_flash = 90; self.boosting = False; self.boost_cooldown = 0
        self.eating = False; self.eat_frame = 0; self.tongue_hit_done = False
    def eat(self, points):
        if self.health < self.max_health:
            heal = min(points, self.max_health - self.health)
            self.health += heal; points -= heal
        if points > 0:
            self.hunger = min(self.max_hunger, self.hunger + points)
        if   self.stage == "tadpole" and self.hunger >= self.max_hunger: self.evolve_to_froglet()
        elif self.stage == "froglet" and self.hunger >= self.max_hunger: self.evolve_to_toad()
        elif self.stage == "toad":                                        self._check_win()
    def _check_win(self):
        if self.health >= self.max_health and self.hunger >= self.max_hunger:
            self.won = True
    def try_boost(self):
        if self.stage == "froglet" and self.boost_cooldown == 0 and not self.boosting and not self.eating:
            self.boosting = True; self.boost_frame = 0
            self.boost_anim_timer = 0; self.boost_angle_deg = self.angle_deg
    def try_eat(self):
        if self.stage in ("froglet", "toad") and not self.boosting and not self.eating:
            self.eating         = True
            self.eat_frame      = 0
            self.eat_anim_timer = 0
            self.tongue_hit_done= False                                    
    def _eat_frame_count(self):
        return TOAD_EAT_FRAME_COUNT if self.stage == "toad" else FROGLET_EAT_FRAME_COUNT
    def _eat_frame_delay(self):
        return TOAD_EAT_FRAME_DELAY if self.stage == "toad" else FROGLET_EAT_FRAME_DELAY
    def tongue_tip_world(self):
        """Returns the world-space position of the tongue tip for the current eat frame."""
        count  = self._eat_frame_count()
        frac   = TONGUE_EXTENSION[min(self.eat_frame, count - 1)]
        length = TONGUE_MAX_LENGTH * frac
        rad    = math.radians(-self.angle_deg)                                      
        return self.x + math.cos(rad) * length, self.y + math.sin(rad) * length
    def update(self, keys):
        accel = 1.2; friction = 0.88
        if self.boosting:
            bx = math.cos(math.radians(-self.boost_angle_deg))
            by = math.sin(math.radians(-self.boost_angle_deg))
            nx = self.x + bx * FROGLET_BOOST_SPEED
            ny = self.y + by * FROGLET_BOOST_SPEED
            if is_in_water(nx, ny):        self.x, self.y = nx, ny
            elif is_in_water(nx, self.y):  self.x = nx
            elif is_in_water(self.x, ny):  self.y = ny
            self.boost_anim_timer += 1
            if self.boost_anim_timer >= BOOST_FRAME_DELAY:
                self.boost_anim_timer = 0; self.boost_frame += 1
                if self.boost_frame >= BOOST_FRAME_COUNT:
                    self.boosting = False; self.boost_frame = 0
                    self.boost_cooldown = BOOST_COOLDOWN
                    self.vx = bx * self.base_speed; self.vy = by * self.base_speed
            if self.hit_timer    > 0: self.hit_timer    -= 1
            if self.evolve_flash > 0: self.evolve_flash -= 1
            return
        if self.boost_cooldown > 0: self.boost_cooldown -= 1
        if self.eating:
            frame_count = self._eat_frame_count()
            frame_delay = self._eat_frame_delay()
            self.eat_anim_timer += 1
            if self.eat_anim_timer >= frame_delay:
                self.eat_anim_timer = 0
                self.eat_frame += 1
                if self.eat_frame >= frame_count:
                    self.eating        = False
                    self.eat_frame     = 0
                    self.tongue_hit_done = False
        dx_in, dy_in = 0, 0
        if keys[pygame.K_w]: dy_in -= 1
        if keys[pygame.K_s]: dy_in += 1
        if keys[pygame.K_a]: dx_in -= 1
        if keys[pygame.K_d]: dx_in += 1
        self.moving = dx_in != 0 or dy_in != 0
        self.vx += dx_in * accel; self.vy += dy_in * accel
        spd = math.hypot(self.vx, self.vy)
        if spd > self.base_speed:
            self.vx = self.vx / spd * self.base_speed
            self.vy = self.vy / spd * self.base_speed
        self.vx *= friction; self.vy *= friction
        if abs(self.vx) > 0.15 or abs(self.vy) > 0.15:
            self.angle_deg = -math.degrees(math.atan2(self.vy, self.vx))
        nx, ny = self.x + self.vx, self.y + self.vy
        if is_in_water(nx, ny):                self.x, self.y = nx, ny
        elif is_in_water(self.x + self.vx, self.y): self.x += self.vx; self.vy = 0
        elif is_in_water(self.x, self.y + self.vy): self.y += self.vy; self.vx = 0
        else:                                   self.vx = self.vy = 0
        fc = TADPOLE_FRAME_COUNT if self.stage == "tadpole" else\
             FROGLET_FRAME_COUNT if self.stage == "froglet" else TOAD_FRAME_COUNT
        if self.moving:
            self.anim_timer += 1
            if self.anim_timer >= FRAME_DELAY:
                self.anim_timer = 0; self.anim_frame = (self.anim_frame + 1) % fc
        else: self.anim_frame = 0
        if is_dirty(self.x, self.y):
            self.dirty_timer += 1
            if self.dirty_timer >= 60: self.take_damage(DIRTY_DAMAGE); self.dirty_timer = 0
        else: self.dirty_timer = 0
        if self.stage == "toad": self._check_win()
        if self.hit_timer    > 0: self.hit_timer    -= 1
        if self.evolve_flash > 0: self.evolve_flash -= 1
    def take_damage(self, amount):
        self.health = max(0, self.health - amount); self.hit_timer = 10
    def check_tongue_hits(self, grasshopper_list):
        """
        Called every frame while eating (froglet or toad).
        Checks if the tongue tip is close enough to any live grasshopper.
        Only one grasshopper can be eaten per tongue animation (tongue_hit_done flag).
        Only checks during the frames where the tongue is actually extended.
        """
        if not self.eating or self.tongue_hit_done:
            return
        count = self._eat_frame_count()
        frac = TONGUE_EXTENSION[min(self.eat_frame, count - 1)]
        if frac < 0.3:                                             
            return
        tip_x, tip_y = self.tongue_tip_world()
        for gh in grasshopper_list:
            if gh.alive:
                dist = math.hypot(tip_x - gh.x, tip_y - gh.y)
                if dist < GRASSHOPPER_HITBOX:
                    gh.alive         = False
                    self.tongue_hit_done = True                                 
                    self.eat(GRASSHOPPER_POINTS)
                    break                                     
    def draw(self, surface, cam):
        sx = int(self.x - cam.x); sy = int(self.y - cam.y)
        if self.boosting:
            frame   = froglet_boost_frames[min(self.boost_frame, BOOST_FRAME_COUNT - 1)]
            angle   = self.boost_angle_deg
            frame_w = BOOST_FRAME_W
            if self.hit_timer > 0:
                frame = frame.copy()
                frame.fill((255, 80, 80, 120), special_flags=pygame.BLEND_RGBA_MULT)
            draw_at_head(surface, frame, angle, sx, sy, frame_w)
        elif self.eating:
            if self.stage == "toad":
                frames = toad_eat_frames
                count  = TOAD_EAT_FRAME_COUNT
            else:
                frames = froglet_eat_frames
                count  = FROGLET_EAT_FRAME_COUNT
            frame = frames[min(self.eat_frame, count - 1)]
            if self.hit_timer > 0:
                frame = frame.copy()
                frame.fill((255, 80, 80, 120), special_flags=pygame.BLEND_RGBA_MULT)
            draw_at_center(surface, frame, self.angle_deg, sx, sy)
        else:
            if self.stage == "tadpole":
                frame = tadpole_frames[self.anim_frame % TADPOLE_FRAME_COUNT]
                frame_w = TADPOLE_FRAME_W
            elif self.stage == "froglet":
                frame = froglet_frames[self.anim_frame % FROGLET_FRAME_COUNT]
                frame_w = FROGLET_FRAME_W
            else:
                frame = toad_frames[self.anim_frame % TOAD_FRAME_COUNT]
                frame_w = TOAD_FRAME_W
            if self.hit_timer > 0:
                frame = frame.copy()
                frame.fill((255, 80, 80, 120), special_flags=pygame.BLEND_RGBA_MULT)
            if self.evolve_flash > 0 and self.evolve_flash % 6 < 3:
                frame = frame.copy()
                frame.fill((255, 215, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
            draw_at_head(surface, frame, self.angle_deg, sx, sy, frame_w)
class Fish:
    SIGHT_RANGE  = 220
    SIGHT_ANGLE  = math.radians(50)
    SPEED_RETURN = 2.0
    GIVE_UP_DIST = 300
    def __init__(self, x, y, patrol_range=180):
        self.x = float(x); self.y = float(y)
        self.angle = random.uniform(0, 2 * math.pi)
        self.desired_angle = self.angle
        self.turn_dir = random.choice([-1, 1])
        self.state = "patrol"
        self.origin_x = float(x); self.origin_y = float(y)
        self.patrol_range = patrol_range
        self.patrol_timer = random.randint(40, 120)
        self.stuck_timer = 0
        self.anim_frame = 0; self.anim_timer = 0
    def can_see_player(self, px, py):
        dx, dy = px - self.x, py - self.y
        dist = math.hypot(dx, dy)
        if dist > self.SIGHT_RANGE: return False
        diff = abs((math.atan2(dy, dx) - self.angle + math.pi) % (2 * math.pi) - math.pi)
        return diff < self.SIGHT_ANGLE
    def separate(self, all_fish):
        sx = sy = 0.0
        for other in all_fish:
            if other is self: continue
            dx, dy = self.x - other.x, self.y - other.y
            dist = math.hypot(dx, dy)
            if 0 < dist < FISH_SEP_RADIUS:
                f = (FISH_SEP_RADIUS - dist) / FISH_SEP_RADIUS
                sx += (dx/dist)*f; sy += (dy/dist)*f
        if sx or sy:
            mag = math.hypot(sx, sy)
            nx = self.x + (sx/mag)*FISH_SEP_STRENGTH
            ny = self.y + (sy/mag)*FISH_SEP_STRENGTH
            if is_in_water(nx, ny): self.x, self.y = nx, ny
    def reset_to_origin(self):
        self.x = self.origin_x; self.y = self.origin_y
        self.state = "patrol"; self.patrol_timer = random.randint(40, 120)
        self.angle = random.uniform(0, 2*math.pi)
        self.desired_angle = self.angle; self.stuck_timer = 0
    def try_move(self, nx, ny):
        if is_in_water(nx, ny) and is_in_fishzone(nx, ny):
            self.x, self.y = nx, ny; return True
        return False
    def update(self, player, all_fish):
        px, py = player.x, player.y
        dx, dy = px - self.x, py - self.y
        dist = math.hypot(dx, dy)
        piz  = is_in_fishzone(px, py)
        self.anim_timer += 1
        if self.anim_timer >= FISH_FRAME_DELAY:
            self.anim_timer = 0
            self.anim_frame = (self.anim_frame + 1) % FISH_FRAME_COUNT
        if self.state == "patrol":
            if self.can_see_player(px, py) and piz: self.state = "chase"
            else:
                self.patrol_timer -= 1
                if self.patrol_timer <= 0:
                    self.desired_angle += random.uniform(-math.pi*.5, math.pi*.5)
                    self.patrol_timer = random.randint(60, 160)
                    self.turn_dir = random.choice([-1, 1])
                self.angle = lerp_angle(self.angle, self.desired_angle, FISH_TURN_PATROL)
                nx = self.x + math.cos(self.angle)*FISH_PATROL_SPEED
                ny = self.y + math.sin(self.angle)*FISH_PATROL_SPEED
                if not self.try_move(nx, ny): self.desired_angle += 0.06 * self.turn_dir
        elif self.state == "chase":
            if not piz or dist > self.GIVE_UP_DIST:
                self.state = "return"; self.stuck_timer = 0
            else:
                if dist > 0:
                    ca = math.atan2(dy, dx)
                    self.angle = lerp_angle(self.angle, ca, FISH_TURN_CHASE)
                    self.desired_angle = ca
                    ad = abs((ca - self.angle + math.pi) % (2*math.pi) - math.pi)
                    af = max(0.2, math.cos(ad))
                    ar = max(0.15, dist/FISH_CHASE_SLOW_RADIUS) if dist < FISH_CHASE_SLOW_RADIUS else 1.0
                    spd = FISH_CHASE_SPEED * af * ar
                    if dist > FISH_CHASE_STOP_RADIUS:
                        nx = self.x + math.cos(self.angle)*spd
                        ny = self.y + math.sin(self.angle)*spd
                        if   is_in_water(nx,ny) and is_in_fishzone(nx,ny): self.x,self.y=nx,ny
                        elif is_in_water(nx,self.y) and is_in_fishzone(nx,self.y): self.x=nx
                        elif is_in_water(self.x,ny) and is_in_fishzone(self.x,ny): self.y=ny
                        else: self.desired_angle += 0.06*self.turn_dir
                if dist < BITE_DIST: player.take_damage(25/60)
        elif self.state == "return":
            self.stuck_timer += 1
            rx, ry = self.origin_x-self.x, self.origin_y-self.y
            rd = math.hypot(rx, ry)
            if rd < 5 or self.stuck_timer > RETURN_TIMEOUT: self.reset_to_origin()
            else:
                ra = math.atan2(ry, rx)
                self.desired_angle = ra
                self.angle = lerp_angle(self.angle, ra, FISH_TURN_RETURN)
                nx = self.x + math.cos(self.angle)*self.SPEED_RETURN
                ny = self.y + math.sin(self.angle)*self.SPEED_RETURN
                if is_in_water(nx, ny): self.x, self.y = nx, ny
                else:
                    self.desired_angle += 0.06*self.turn_dir
                    wx = self.x + math.cos(self.angle)*self.SPEED_RETURN
                    wy = self.y + math.sin(self.angle)*self.SPEED_RETURN
                    if is_in_water(wx, wy): self.x, self.y = wx, wy
            if self.can_see_player(px, py) and piz: self.state = "chase"; self.stuck_timer = 0
        self.separate(all_fish)
    def draw(self, surface, cam):
        sx = int(self.x - cam.x); sy = int(self.y - cam.y)
        if not (-300 < sx < SCREEN_W+300 and -300 < sy < SCREEN_H+300): return
        frames = fish_angry_frames if self.state == "chase" else fish_frames_base
        draw_at_head(surface, frames[self.anim_frame], -math.degrees(self.angle), sx, sy, FISH_FRAME_W)
class Crab:
    def __init__(self, x, y):
        self.x = float(x); self.y = float(y)
        self.origin_x = float(x); self.origin_y = float(y)
        self.move_angle = random.uniform(0, 2 * math.pi)
        self.body_angle = self.move_angle + math.pi / 2
        self.desired_move_angle = self.move_angle
        self.state = "patrol"; self.stuck_timer = 0
        self.anim_frame = 0; self.anim_timer = 0
        self.turn_dir = random.choice([-1, 1])
    def can_see_player(self, px, py):
        dx, dy = px - self.x, py - self.y
        if math.hypot(dx, dy) > CRAB_SIGHT_RANGE: return False
        diff = abs((math.atan2(dy, dx) - self.body_angle + math.pi) % (2*math.pi) - math.pi)
        return diff < CRAB_HALF_CONE
    def _try_crab_move(self, nx, ny):
        if is_in_crab_zone(nx, ny): self.x, self.y = nx, ny; return True
        return False
    def update(self, player):
        px, py = player.x, player.y
        dx, dy = px - self.x, py - self.y
        dist   = math.hypot(dx, dy)
        self.anim_timer += 1
        if self.anim_timer >= CRAB_FRAME_DELAY:
            self.anim_timer = 0; self.anim_frame = (self.anim_frame + 1) % CRAB_FRAME_COUNT
        if self.state == "patrol":
            if self.can_see_player(px, py): self.state = "chase"
            else:
                if math.hypot(self.x-self.origin_x, self.y-self.origin_y) > 200:
                    self.desired_move_angle = math.atan2(self.origin_y-self.y, self.origin_x-self.x)
                elif random.random() < 0.008:
                    self.desired_move_angle += random.uniform(-math.pi*.5, math.pi*.5)
                    self.turn_dir = random.choice([-1, 1])
                self.move_angle = lerp_angle(self.move_angle, self.desired_move_angle, 0.04)
                self.body_angle = self.move_angle + math.pi / 2
                nx = self.x + math.cos(self.move_angle) * CRAB_PATROL_SPEED
                ny = self.y + math.sin(self.move_angle) * CRAB_PATROL_SPEED
                if not self._try_crab_move(nx, ny): self.desired_move_angle += 0.10 * self.turn_dir
        elif self.state == "chase":
            if dist > CRAB_SIGHT_RANGE * 1.3: self.state = "return"; self.stuck_timer = 0
            else:
                if dist > 0:
                    cd = math.atan2(dy, dx)
                    self.desired_move_angle = cd
                    self.move_angle = lerp_angle(self.move_angle, cd, 0.09)
                    self.body_angle = self.move_angle + math.pi / 2
                    nx = self.x + math.cos(self.move_angle)*CRAB_SPEED
                    ny = self.y + math.sin(self.move_angle)*CRAB_SPEED
                    if   self._try_crab_move(nx, ny): pass
                    elif self._try_crab_move(nx, self.y): pass
                    elif self._try_crab_move(self.x, ny): pass
                    else: self.desired_move_angle += 0.10 * self.turn_dir
                if dist < CRAB_BITE_DIST: player.take_damage(CRAB_DAMAGE / 60)
        elif self.state == "return":
            self.stuck_timer += 1
            rx, ry = self.origin_x-self.x, self.origin_y-self.y
            if math.hypot(rx, ry) < 5 or self.stuck_timer > CRAB_RETURN_TIME:
                self.x, self.y = self.origin_x, self.origin_y
                self.state = "patrol"; self.stuck_timer = 0
            else:
                ra = math.atan2(ry, rx)
                self.move_angle = lerp_angle(self.move_angle, ra, 0.05)
                self.body_angle = self.move_angle + math.pi / 2
                nx = self.x + math.cos(self.move_angle)*CRAB_PATROL_SPEED
                ny = self.y + math.sin(self.move_angle)*CRAB_PATROL_SPEED
                if not self._try_crab_move(nx, ny): self.desired_move_angle += 0.10*self.turn_dir
            if self.can_see_player(px, py): self.state = "chase"; self.stuck_timer = 0
    def draw(self, surface, cam):
        sx = int(self.x - cam.x); sy = int(self.y - cam.y)
        if not (-300 < sx < SCREEN_W+300 and -300 < sy < SCREEN_H+300): return
        draw_at_center(surface, crab_frames[self.anim_frame], -math.degrees(self.body_angle), sx, sy)
def make_fish():
    pts = [
        (WORLD_W*0.30, WORLD_H*0.45), (WORLD_W*0.38, WORLD_H*0.55),
        (WORLD_W*0.46, WORLD_H*0.42), (WORLD_W*0.54, WORLD_H*0.58),
        (WORLD_W*0.62, WORLD_H*0.45), (WORLD_W*0.70, WORLD_H*0.52),
    ]
    return [Fish(*find_water_pos(px, py, need_fishzone=True), patrol_range=200) for px, py in pts]
def make_crabs():
    crabs = []
    for sx, sy in crab_spawn_positions:
        placed = False
        for r in range(0, 200, 8):
            for deg in range(0, 360, 20):
                tx = sx + r * math.cos(math.radians(deg))
                ty = sy + r * math.sin(math.radians(deg))
                if is_in_crab_zone(tx, ty):
                    crabs.append(Crab(tx, ty)); placed = True; break
            if placed: break
        if not placed: crabs.append(Crab(sx, sy))
    print(f"Spawned {len(crabs)} crabs")
    return crabs
def make_grasshoppers():
    """
    Pick GRASSHOPPER_MAX random lily pads and place one grasshopper on each.
    Each grasshopper stays within its own lily pad zone.
    """
    if not lily_pad_positions:
        print("No lily pad positions found — no grasshoppers spawned")
        return []
    chosen = random.sample(lily_pad_positions, min(GRASSHOPPER_MAX, len(lily_pad_positions)))
    hoppers = []
    for ox, oy in chosen:
        placed = False
        for r in range(0, int(GRASSHOPPER_WANDER_RAD), 4):
            for deg in range(0, 360, 15):
                tx = ox + r * math.cos(math.radians(deg))
                ty = oy + r * math.sin(math.radians(deg))
                if is_in_gh_zone(tx, ty):
                    hoppers.append(Grasshopper(ox, oy))
                    hoppers[-1].x = tx; hoppers[-1].y = ty
                    placed = True; break
            if placed: break
        if not placed:
            hoppers.append(Grasshopper(ox, oy))
    print(f"Spawned {len(hoppers)} grasshoppers")
    return hoppers
font_ui  = pygame.font.SysFont("monospace", 16, bold=True)
font_big = pygame.font.SysFont("monospace", 72, bold=True)
font_med = pygame.font.SysFont("monospace", 36, bold=True)
def draw_bar(surface, x, y, w, h, value, max_value, fill_col, label):
    pygame.draw.rect(surface, (40,40,40), (x, y, w+4, h+4), border_radius=5)
    pygame.draw.rect(surface, (20,20,20), (x+2, y+2, w, h), border_radius=4)
    bw = int(w * (value / max_value))
    if bw > 0: pygame.draw.rect(surface, fill_col, (x+2, y+2, bw, h), border_radius=4)
    pygame.draw.rect(surface, WHITE, (x, y, w+4, h+4), 2, border_radius=5)
    surface.blit(font_ui.render(label, True, WHITE), (x+w+14, y+2))
def draw_ui(surface, player):
    hc = (80,220,80) if player.health > player.max_health*.5 else\
         (220,180,0) if player.health > player.max_health*.25 else (220,50,50)
    draw_bar(surface, 20, 20, 200, 20, player.health, player.max_health, hc,
             f"HP  {int(player.health)}/{int(player.max_health)}")
    draw_bar(surface, 20, 52, 200, 20, player.hunger, player.max_hunger, (255,180,30),
             f"HUNGER  {int(player.hunger)}/{int(player.max_hunger)}")
    if player.evolve_flash > 0:
        msg = "EVOLVED TO FROGLET!" if player.stage=="froglet" else "EVOLVED TO TOAD!"
        evo = font_big.render(msg, True, GOLD)
        surface.blit(evo, (SCREEN_W//2 - evo.get_width()//2, SCREEN_H//2 - 80))
    if player.stage == "toad" and not player.won:
        surface.blit(font_ui.render("Fill BOTH bars to escape the pond",
                                    True, (200,255,200)), (20, 84))
    if player.stage in ("froglet", "toad"):
        y = 108 if player.stage == "toad" else 84                                                
        if player.stage == "froglet":
            if player.boosting:
                surface.blit(font_ui.render(">> BOOSTING <<", True, (100,200,255)), (20, y))
            elif player.boost_cooldown > 0:
                secs = math.ceil(player.boost_cooldown / 60)
                draw_bar(surface, 20, y, 200, 18, player.boost_cooldown, BOOST_COOLDOWN,
                         (180,80,80), f"BOOST  {secs}s")
            else:
                surface.blit(font_ui.render("SPACE  BOOST  READY", True, (100,255,150)), (20, y))
            y += 26
        if player.eating:
            surface.blit(font_ui.render("*TONGUE*", True, (255, 200, 100)), (20, y))
        else:
            surface.blit(font_ui.render("E  eat grasshopper", True, (180,255,180)), (20, y))
    surface.blit(font_ui.render("WASD move  |  E eat  |  SPACE boost  |  R restart  |  ESC quit",
                                True, (150,200,255)), (20, SCREEN_H-34))
    if player.won:
        ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        ov.fill((0,0,0,180)); surface.blit(ov, (0,0))
        win = font_big.render("YOU ESCAPED!", True, GOLD)
        surface.blit(win, (SCREEN_W//2-win.get_width()//2, SCREEN_H//2-60))
        sub = font_med.render("The toad is free.", True, WHITE)
        surface.blit(sub, (SCREEN_W//2-sub.get_width()//2, SCREEN_H//2+30))
        rs = font_ui.render("press  R  to play again", True, (180,180,180))
        surface.blit(rs, (SCREEN_W//2-rs.get_width()//2, SCREEN_H//2+90))
    if player.health <= 0:
        ov = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        ov.fill((0,0,0,170)); surface.blit(ov, (0,0))
        go = font_big.render("GAME OVER", True, (255,50,50))
        surface.blit(go, (SCREEN_W//2-go.get_width()//2, SCREEN_H//2-50))
        rs = font_ui.render("press  R  to restart", True, WHITE)
        surface.blit(rs, (SCREEN_W//2-rs.get_width()//2, SCREEN_H//2+50))
camera           = Camera()
fish_list        = make_fish()
crab_list        = make_crabs()
larvae_list      = make_larvae()
grasshopper_list = make_grasshoppers()
player           = Player()
camera.x = max(0, min(WORLD_W-SCREEN_W, player.x-SCREEN_W//2))
camera.y = max(0, min(WORLD_H-SCREEN_H, player.y-SCREEN_H//2))
print(f"Player start: ({int(player.x)}, {int(player.y)})")
gh_respawn_timer = 0
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
            if event.key == pygame.K_r:
                player           = Player()
                fish_list        = make_fish()
                crab_list        = make_crabs()
                larvae_list      = make_larvae()
                grasshopper_list = make_grasshoppers()
                camera           = Camera()
                gh_respawn_timer = 0
                camera.x = max(0, min(WORLD_W-SCREEN_W, player.x-SCREEN_W//2))
                camera.y = max(0, min(WORLD_H-SCREEN_H, player.y-SCREEN_H//2))
            if event.key == pygame.K_SPACE:
                player.try_boost()
            if event.key == pygame.K_e:
                player.try_eat()
            if event.key == pygame.K_F6:
                if player.stage == "tadpole":
                    player.evolve_to_froglet()
                elif player.stage == "froglet":
                    player.evolve_to_toad()
    keys = pygame.key.get_pressed()
    if player.health > 0 and not player.won:
        player.update(keys)
        if player.eating:
            player.check_tongue_hits(grasshopper_list)
        for fish in fish_list:  fish.update(player, fish_list)
        for crab in crab_list:  crab.update(player)
        for larva in larvae_list:
            if larva.alive:
                larva.update()
                if math.hypot(player.x-larva.x, player.y-larva.y) < EAT_RADIUS:
                    larva.alive = False
                    player.eat(LARVAE_POINTS)
        dead_larvae = sum(1 for l in larvae_list if not l.alive)
        if dead_larvae > 5:
            for larva in larvae_list:
                if not larva.alive: larva.__init__(); break
        for gh in grasshopper_list:
            if gh.alive: gh.update()
        gh_alive = sum(1 for gh in grasshopper_list if gh.alive)
        if gh_alive < GRASSHOPPER_MAX:
            gh_respawn_timer += 1
            if gh_respawn_timer >= GRASSHOPPER_RESPAWN and lily_pad_positions:
                gh_respawn_timer = 0
                occupied = {(int(gh.origin_x), int(gh.origin_y))
                            for gh in grasshopper_list if gh.alive}
                available = [(x, y) for x, y in lily_pad_positions
                             if (int(x), int(y)) not in occupied]
                if available:
                    nx, ny = random.choice(available)
                    for gh in grasshopper_list:
                        if not gh.alive:
                            gh.__init__(nx, ny)
                            break
                    else:
                        grasshopper_list.append(Grasshopper(nx, ny))
    camera.update(player.x, player.y)
    screen.blit(background, (0,0), (camera.ix, camera.iy, SCREEN_W, SCREEN_H))
    for larva in larvae_list:
        if larva.alive: larva.draw(screen, camera)
    for gh in grasshopper_list:
        if gh.alive: gh.draw(screen, camera)
    for fish in fish_list:  fish.draw(screen, camera)
    for crab in crab_list:  crab.draw(screen, camera)
    player.draw(screen, camera)
    draw_ui(screen, player)
    pygame.display.flip()