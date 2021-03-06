import pygame
import helpers.game_functions as gf
from helpers.settings import Settings
from classes.ship import Ship
from pygame.sprite import Group

def run_game():
    # Initialize background settings for pygame functionality
    pygame.init()

    # Initialize settings object
    settings = Settings()

    # Initialize screen object of 1200x800 and add caption
    screen = pygame.display.set_mode((settings.screen_w, settings.screen_h))
    pygame.display.set_caption("Alien Invasion")
    
    # Initialize ship
    ship = Ship(settings, screen)

    # Initialize alien and create fleet
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # Create group for bullets
    bullets = Group()

    # Main loop for game
    # Surfaces are redrawn on every pass of our loop
    while True:

        # Check for events
        gf.check_events(screen, settings, ship, bullets)

        # Update ship
        ship.update(settings)

        # Update bullets
        bullets.update()

        # get rid of off-screen bullets
        gf.update_bullets(aliens, bullets)

        # Update aliens
        gf.update_aliens(settings, aliens)

        # Flip to new screen, ship position, etc.
        gf.update_screen(settings, screen, ship, bullets, aliens)

# call program
run_game()
