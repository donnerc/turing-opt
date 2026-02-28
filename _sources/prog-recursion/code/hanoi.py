from gpanel import *
from time import sleep


class MyFont:
    font = Font("Arial", Font.BOLD, 36)
    
class EmptyStickError(RuntimeError):
    def __init__(self):
        super(EmptyStickError, self).__init__("Unable to peek empty stick")
        
    

class HanoiTowers:
    
    def __init__(self, n, x_max=999, y_max=500, stick_width=15, names=None, speed=1):
        self.x_max = x_max
        self.y_max = y_max
        self.stick_width = stick_width
        self.names = names or ["A", "B", "C"]
        self.set_speed(speed)
        
        self.panel = makeGPanel(0, self.x_max, 0, self.y_max)
        self.panel.windowSize(1200, 600)
        self.sticks = {}
        
        self.reset(n)   
        
             
    def get_total_moves(self):
        return Stick.nb_moves     
        
        
        
    def set_speed(self, speed):
        if speed < 1:
            speed = 1
        elif speed > 50:
            speed = 50
        self.speed = speed
        
    def reset(self, n):
        clear()
        self.n = n
        self.draw()
        self._stick_list = self.sticks_in_order()
        Stick.nb_moves = 0
        
        
    def sticks_in_order(self):
        return [self.sticks[x] for x in self.names]
    
        
    def stick(self, name):
        if name in self.sticks:
            return self.sticks[name]
        else:
            raise KeyError("No stick named '{}'".format(name))
            
    def move(self, A, B):
        self.sticks[A].move_to(self.sticks[B])
        

    def draw(self):
        # draw the floor
        move(self.x_max // 2, 0)
        fillRectangle(self.x_max - 100, 30)
        
        # draw the sticks
        for i, name in enumerate(self.names):
            x_pos = (i+1) * ((self.x_max) // 4)
            
            if name in self.sticks:
                self.sticks[name].reset(self.n if i == 0 else 0)
            else:
                stick = Stick(
                    name=name,
                    x_pos=x_pos,
                    y_pos=30 // 2,
                    nb_disks=self.n if i == 0 else 0,
                    width=self.stick_width,
                    height=self.y_max - 100,
                    speed=self.speed
                )
            
                self.sticks[name] = stick
            
        
class Stick:
    
    # height of disks
    rectangle_height = 30
    margin = 5
    diskColor = "red"
    base_sleep = 2
    
    nb_moves = 0
    
    def __init__(self, name, x_pos, y_pos=0, nb_disks=0, speed=1, width=15, height=300):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.width = width
        self.height = height
        self.disks = []
        self.speed = speed      
        
        # private instance variables  
        self._top_disk_position = 0
        
        self.reset(nb_disks)
        
        
        
    def reset(self, n):
        self._top_disk_position = Stick.rectangle_height // 2
        self.disks = []
        self.draw()
        self.fill(n)
        
        
    def fill(self, n):
        for r in range(n + 1, 1, -1):
            self.push(r)
            
    def move_to(self, b):        
        if not self.is_empty():
            r = self.pop()
            b.push(r)
        sleep(Stick.base_sleep / self.speed)
        Stick.nb_moves += 1
        print("move from {} to {}".format(self.name, b.name))
        
    def __gt__(self, other):
        self.move_to(other)
        
    def __lt__(self, other):
        other.move_to(self)
        
    def draw(self):
        fillRectangle(self.x_pos - self.width // 2, self.y_pos, self.x_pos + self.width // 2, self.y_pos + self.height)
        text(self.x_pos, self.y_pos + self.height + 10, self.name, MyFont.font, "black", "white")
        
    def add_disk_avatar(self, r):
        previousColor = setColor(Stick.diskColor)
        move(self.x_pos, self._top_disk_position + Stick.rectangle_height // 2)
        fillRectangle(r, Stick.rectangle_height)
        self._top_disk_position += Stick.rectangle_height + Stick.margin
        setColor(previousColor)
        
    def remove_top_disk_avatar(self, r):
        self._top_disk_position -= (Stick.rectangle_height + Stick.margin)
        move(self.x_pos, self._top_disk_position + Stick.rectangle_height // 2)
        previousColor = setColor("white")
        # add 2 pixels to avoid pixel artifacts
        fillRectangle(r * 25 + 2, Stick.rectangle_height)
        setColor("black")
        fillRectangle(self.width, Stick.rectangle_height)
        setColor(previousColor)
        
        
    def push(self, r):
        '''
        
        Push disk of radius r on top of the pile
        
        '''
        if not self.is_empty() and r >= self.peek():
            raise ValueError("Unable to push disk of radius {} on top of pile {} : actual state : {}".format(r, self.name, self.disks))
        self.add_disk_avatar(25 * r)
        self.disks.append(r)
        
    def is_empty(self):
        return len(self.disks) == 0
    
    def pop(self):
        if not self.is_empty():
            top = self.disks.pop()
            self.remove_top_disk_avatar(top)
        else:
            raise EmptyStickError()
            
        return top
    
    def peek(self):
        try:
            return self.disks[-1]
        except Exception as e:
            raise EmptyStickError()
            
    def __repr__(self):
        return "Stick([{}])".format(",".join([str(x) for x in self.disks]))
    
    def __str__(self):
        return self.__repr__()
    
                      
if __name__ == '__main__':
    hanoi = HanoiTowers(n=3, names=["A", "B", "C"], speed=50)
    [A, B, C] = hanoi.sticks_in_order()
    sleep(1)
    
    # moves to solve the game for n=3
    A > C
    A > B
    C > B
    A > C
    B > A
    B > C
    A > C
    
    print("Nombre de mouvements necessaires : ", Stick.nb_moves)
    
   
    
    