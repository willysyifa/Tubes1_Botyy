from typing import Optional, List

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import clamp

def indexValid(x, y: int, width, height):
    return 0 <= x < width and 0 <= y < height

class GreedyValueBot(BaseLogic):
    def __init__(self):
        self.directions = [(1,0), (0,1), (-1,0), (0,-1)]
        self.bot = None
        self.board_width = 0
        self.board_height = 0
        self.diamonds: List[GameObject] = []
        self.redButton = None
    
    def distance(self, pos1: Position, pos2: Position) -> int:
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
    
    def get_direction_towards(self, curr: Position, dest: Position) -> (int, int):
        dx = clamp(dest.x - curr.x, -1, 1)
        dy = clamp(dest.y - curr.y, -1, 1)
        if dx != 0:
            return dx, 0
        else:
            return 0, dy
    
    def next_move(self, board_bot: GameObject, board: Board):
        self.bot = board_bot
        self.board_width = board.width
        self.board_height = board.height
        self.diamonds = []
        self.redButton = None
        
        for obj in board.game_objects:
            if obj.type == "DiamondGameObject":
                self.diamonds.append(obj)
            elif obj.type == "DiamondButtonGameObject":
                self.redButton = obj
        
        time_left = board_bot.properties.milliseconds_left // 1000
        dist_to_base = self.distance(board_bot.position, board_bot.properties.base)
        if board_bot.properties.diamonds >= board_bot.properties.inventory_size or time_left <= dist_to_base + 1:
            if not self.positions_equal(board_bot.position, board_bot.properties.base):
                return self.get_direction_towards(board_bot.position, board_bot.properties.base)
            else:
                return 0, 0
        
        max_point = -1
        candidate_diamonds = []
        for diamond in self.diamonds:
            if board_bot.properties.diamonds + diamond.properties.points <= board_bot.properties.inventory_size:
                if diamond.properties.points > max_point:
                    max_point = diamond.properties.points
                    candidate_diamonds = [diamond]
                elif diamond.properties.points == max_point:
                    candidate_diamonds.append(diamond)
        
        if not candidate_diamonds:
            if not self.positions_equal(board_bot.position, board_bot.properties.base):
                return self.get_direction_towards(board_bot.position, board_bot.properties.base)
            else:
                return 0, 0
        
        # Pilih yang terdekat di antara diamond dengan poin tertinggi
        min_dist = float('inf')
        target = None
        for diamond in candidate_diamonds:
            dist = self.distance(board_bot.position, diamond.position)
            if dist < min_dist:
                min_dist = dist
                target = diamond
        
        return self.get_direction_towards(board_bot.position, target.position)
    
    def positions_equal(self, pos1: Position, pos2: Position) -> bool:
        return pos1.x == pos2.x and pos1.y == pos2.y
