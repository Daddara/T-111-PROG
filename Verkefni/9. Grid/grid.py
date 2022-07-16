DEFAULT = 'o'
TRAVELER = 'x'

class Grid:
    
    
    def __init__ (self, row=1, col=1):
        self.row = row
        self.col = col
        self.grid = [[DEFAULT for _ in range(self.col)] for _ in range(self.row)]
        self.grid[0][0] = TRAVELER
        self.result = ''
        self.x = 0
        self.y = 0
        
    def current_pos(self):
        x_current = self.x + 1
        y_current = self.y + 1
        return (x_current, y_current)
    
    def move_left(self):
        self.grid[self.x][self.y] = DEFAULT
        if self.y == 0:
            self.y = (self.col -1)
        else:
            self.y -= 1
        self.grid[self.x][self.y] = TRAVELER
        
    def move_right(self):
        self.grid[self.x][self.y] = DEFAULT
        if self.y == (self.col -1):
            self.y = 0
        else:
            self.y += 1
        self.grid[self.x][self.y] = TRAVELER
                
    def move_up(self):
        self.grid[self.x][self.y] = DEFAULT
        if self.x == 0:
            self.x = (self.row -1)
        else:
            self.x -= 1
        self.grid[self.x][self.y] = TRAVELER
        
    def move_down(self):
        self.grid[self.x][self.y] = DEFAULT
        if self.x == (self.row -1):
            self.x = 0
        else:
            self.x += 1
        self.grid[self.x][self.y] = TRAVELER
    
    def __str__(self):
        self.result = ''
        for i in self.grid:
            for j in i:
                self.result += j
            self.result += '\n'
        return self.result
    
    
a_grid = Grid(4,4)
print(a_grid)
print(a_grid.current_pos())
a_grid.move_down()
print(a_grid)
print(a_grid.current_pos())
a_grid.move_up()
print(a_grid)
print(a_grid.current_pos())
a_grid.move_left()
print(a_grid)
print(a_grid.current_pos())
a_grid.move_up()
a_grid.move_up()
a_grid.move_up()
print(a_grid)
print(a_grid.current_pos())
