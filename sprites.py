from typing import Optional, Union
import pygame
import random
from settings import *


class Icon:

  def __init__(
      self,
      x: int,
      y: int,
      shape: Shapes,
      colour: tuple[int, int, int],
      revealed: bool = False,
  ):
    self.x, self.y = x, y
    self.shape, self.colour = shape, colour
    self.revealed = revealed

  def draw(self, screen):
    if self.revealed:
      if self.shape == Shapes.DOUGHNUT:
        pygame.draw.circle(
            screen, self.colour,
            (self.x + int(TILESIZE * 0.5), self.y + int(TILESIZE * 0.5)),
            int(TILESIZE * 0.5) - 5)
        pygame.draw.circle(
            screen, BGCOLOUR,
            (self.x + int(TILESIZE * 0.5), self.y + int(TILESIZE * 0.5)),
            int(TILESIZE * 0.25) - 5)
      elif self.shape == Shapes.SQUARE:
        pygame.draw.rect(
            screen, self.colour,
            (self.x + int(TILESIZE * 0.25), self.y + int(TILESIZE * 0.25),
             TILESIZE - int(TILESIZE * 0.5), TILESIZE - int(TILESIZE * 0.5)))
      elif self.shape == Shapes.DIAMOND:
        pygame.draw.polygon(
            screen, self.colour,
            ((self.x + int(TILESIZE * 0.5), self.y),
             (self.x + TILESIZE - 1, self.y + int(TILESIZE * 0.5)),
             (self.x + int(TILESIZE * 0.5), self.y + TILESIZE - 1),
             (self.x, self.y + int(TILESIZE * 0.5))))
      elif self.shape == Shapes.LINES:
        for i in range(0, TILESIZE, 4):
          pygame.draw.line(screen, self.colour, (self.x, self.y + i),
                           (self.x + i, self.y))
          pygame.draw.line(screen, self.colour,
                           (self.x + i, self.y + TILESIZE - 1),
                           (self.x + TILESIZE - 1, self.y + i))
      elif self.shape == Shapes.OVAL:
        pygame.draw.ellipse(screen, self.colour,
                            (self.x, self.y + int(TILESIZE * 0.25), TILESIZE,
                             int(TILESIZE * 0.5)))
    else:
      pygame.draw.rect(screen, WHITE, (self.x, self.y, TILESIZE, TILESIZE))

    # Draw the box
    pygame.draw.rect(screen, WHITE, (self.x, self.y, TILESIZE, TILESIZE), 1)

  def is_mouse_over(self, mx, my):
    return self.x <= mx <= self.x + TILESIZE and \
            self.y <= my <= self.y + TILESIZE


class Board:

  def __init__(self):
    self.create_icons()
    self.create_board()

  def create_icons(self):
    # create a list of every possible shape in every colour
    self.icons: list[tuple[Shapes, Colours]] = []
    for colour in Colours:
      for shape in Shapes:
        self.icons
        self.icons.append((shape, colour))

    # Calculate how many icons are needed
    number_icons = int(BOARD_WIDTH * BOARD_HEIGHT / 2)
    # Make two of each icons
    self.icons = self.icons[:number_icons] * 2
    random.shuffle(self.icons)

  def create_board(self):
    # Create the board data structure, with randomly placed icons
    self.data: list[list[Icon]] = []
    for tile_x in range(BOARD_WIDTH):
      row: list[Icon] = []
      for tile_y in range(BOARD_HEIGHT):
        x = tile_x * (TILESIZE + GAPSIZE) + MARGIN_X
        y = tile_y * (TILESIZE + GAPSIZE) + MARGIN_Y
        icon = self.icons.pop(0)
        shape = icon[0]
        colour = icon[1]
        row.append(Icon(x, y, shape, colour.value))
      self.data.append(row)

  def draw_board(self, screen):
    for row in self.data:
      for icon in row:
        icon.draw(screen)

  def is_clicked(self, mx, my) -> Optional[Icon]:
    for row in self.data:
      for icon in row:
        if icon.is_mouse_over(mx, my) and not icon.revealed:
          icon.revealed = True
          return icon
    return None

  def reset_icons(self, first_selection: Icon, second_selection: Icon):
    for row in self.data:
      for icon in row:
        if icon in [first_selection, second_selection]:
          icon.revealed = False
