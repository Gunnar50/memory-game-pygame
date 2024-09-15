import time

import pygame
from settings import *
from sprites import *
import random


class Game:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    self.clock = pygame.time.Clock()

  def new(self):
    self.board = Board()
    self.start_game()
    self.first_selection = None  # stores the (x, y) of the first box selected.
    self.second_selection = None

  def run(self):
    self.playing = True
    while self.playing:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()
    else:
      self.end_game()

  def has_won(self):
    for row in self.board.data:
      for icon in row:
        if not icon.revealed:
          return False
    return True

  def update(self):
    if self.has_won():
      self.playing = False

    if self.first_selection and self.second_selection:
      if self.first_selection.shape != self.second_selection.shape or \
          self.first_selection.colour != self.second_selection.colour:
        self.screen.fill(BGCOLOUR)
        self.board.draw_board(self.screen)
        pygame.display.update()
        pygame.time.wait(1000)
        self.board.reset_icons(self.first_selection, self.second_selection)

      self.first_selection = None
      self.second_selection = None

  def highlight_tile(self):
    mx, my = pygame.mouse.get_pos()
    for row in self.board.data:
      for icon in row:
        if icon.x <= mx <= icon.x + TILESIZE and icon.y <= my <= icon.y + TILESIZE:
          if not icon.revealed:
            pygame.draw.rect(
                self.screen, Colours.CYAN.value,
                (icon.x - 5, icon.y - 5, TILESIZE + 10, TILESIZE + 10), 4)

  def draw(self):
    self.screen.fill(BGCOLOUR)
    self.board.draw_board(self.screen)
    self.highlight_tile()
    pygame.display.update()

  def events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit(0)

      if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        if self.first_selection is None:
          self.first_selection = self.board.is_clicked(mx, my)
        else:
          self.second_selection = self.board.is_clicked(mx, my)
          if self.first_selection == self.second_selection:
            self.second_selection = None

  def start_game(self):
    for _ in range(5):
      # choose 10 cards at random
      for _ in range(10):
        random_row = random.choice(self.board.data)
        random_card = random.choice(random_row)
        random_card.revealed = True

      # draw the board
      self.screen.fill(BGCOLOUR)
      self.board.draw_board(self.screen)
      pygame.display.update()

      # hide the cards back after 1sec
      pygame.time.wait(1000)
      for row in self.board.data:
        for icon in row:
          icon.revealed = False

  def end_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
          return


if __name__ == "__main__":
  game = Game()
  while True:
    game.new()
    game.run()
