import os
import pygame

# Absolute path to the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset_path(*relative_path_parts):
    """
    Builds an absolute path to an asset located in the ../assets directory.
    Works regardless of the working directory or OS.
    
    Example:
        image = pygame.image.load(asset_path("images", "Fondo.jpg"))
    """
    return os.path.join(BASE_DIR, "..", "assets", *relative_path_parts)


def load_image(filename):
    """
    Loads an image from the assets/images directory.
    """
    return pygame.image.load(asset_path("images", filename))


def load_sound(filename):
    """
    Loads a sound from the assets/audio directory.
    """
    return pygame.mixer.Sound(asset_path("audio", filename))
