import enum

# game settings
WIDTH = 640
HEIGHT = 500
FPS = 30
TITLE = "Memory Game"

BOARD_WIDTH = 6  # number of columns
BOARD_HEIGHT = 6  # number of rows
TILESIZE = 40  # size of box height and width
GAPSIZE = 10  # size of the gap between boxes
MARGIN_X = int((WIDTH - (BOARD_WIDTH * (TILESIZE + GAPSIZE))) / 2)
MARGIN_Y = int((HEIGHT - (BOARD_HEIGHT * (TILESIZE + GAPSIZE))) / 2)
assert (
    BOARD_WIDTH * BOARD_HEIGHT
) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

# COLORS (r, g, b)
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
BGCOLOUR = DARKGREY


class Colours(enum.Enum):
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 0)
  ORANGE = (255, 128, 0)
  PURPLE = (255, 0, 255)
  CYAN = (0, 255, 255)


class Shapes(enum.Enum):
  DOUGHNUT = 'doughnut'
  SQUARE = 'square'
  DIAMOND = 'diamond'
  LINES = 'lines'
  OVAL = 'oval'
