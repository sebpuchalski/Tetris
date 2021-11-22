#Tetris


import pygame
import sys
import random


class Fallen_Blocks():
    '''class is responsible for drawing spaces where blocks have fallen previously.'''

    def __init__(self, lista):
        self.size = 10
        self.positions = lista

    def draw(self, surface):
        for i in self.positions:
            r = pygame.Rect((i[0], i[1]), (self.size, self.size))
            pygame.draw.rect(surface, ORANGE ,r)


class Rectangle():
    def __init__(self, covered_area):
        self.size = 10
        self.position = [SCREEN_WIDTH/2, self.size]
        self.pos = 0
        self.covered_area = covered_area

    def draw(self, surface):
        if self.pos%2==0: #vertical position
            r = pygame.Rect((self.position[0], self.position[1]), (self.size, 3*self.size))
            pygame.draw.rect(surface, BLUE ,r)

        elif self.pos%2==1:
            r = pygame.Rect((self.position[0], self.position[1]), (3*self.size, self.size))
            pygame.draw.rect(surface, BLUE ,r)

    def move(self):


        '''moves'''
        if self.pos%2==0 and self.position[1]+3*self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in vertical position '''
            game_on = False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]

            last_position = [p_1, p_2, p_3]


        elif self.pos%2==0 and [self.position[0],self.position[1]+3*self.size] in self.covered_area:
            ''' Instance where the vertical rectangle reaches a place where other rectangles have previously fallen. '''

            game_on = False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]

            last_position = [p_1, p_2, p_3]


        elif self.pos%2==1 and self.position[1]+self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in horizontal position '''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]

            last_position = [p_1, p_2, p_3]


        elif self.pos%2==1 and (
                [self.position[0],self.position[1]+self.size] in self.covered_area or
                [self.position[0]+self.size, self.position[1]+self.size] in self.covered_area or
                [self.position[0]+2*self.size, self.position[1]+self.size] in self.covered_area
                ):
            ''' Instance where the horizontal rectangle reaches a place where other rectangles have previously fallen. '''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]

            last_position = [p_1, p_2, p_3]


        else:
            ''' Instance where the rectangle is still moving down'''
            self.position[1] += GRID_SIZE/5
            game_on = True
            last_position = False

        return game_on, last_position

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    if self.pos%2==0 and (self.position[0]>=SCREEN_WIDTH-2*self.size):#case when rectangle is in vert. position and is to be flipped as to move out of the screen:
                        pass
                    else:
                        self.pos +=1
                elif event.key == pygame.K_LEFT:
                    if self.position[0] - self.size <0:
                        pass
                    else:
                        self.position[0] -= self.size

                elif event.key == pygame.K_RIGHT:

                    if self.pos%2==1 and (self.position[0]+ 3*self.size >= SCREEN_WIDTH):
                            pass

                    elif self.pos%2==0 and (self.position[0] + self.size >= SCREEN_WIDTH):
                            pass
                    else:
                        self.position[0] += self.size
                return event.key


class Half_Cross():
    def __init__(self, covered_area):
        self.size = 10
        self.position = [SCREEN_WIDTH-3*GRID_SIZE, self.size]
        self.pos = 0 #values of 0, 1, 2 and 3 possible for all four positions
        self.covered_area = covered_area


    def draw(self, surface):
        '''Draws half cross onto the surface'''

        if self.pos==0: #vertical position, nipple to the left
            r = pygame.Rect((self.position[0], self.position[1]), (self.size, self.size*3))
            pygame.draw.rect(surface, BLUE ,r)
            s = pygame.Rect((self.position[0]-self.size, self.position[1]+self.size), (self.size, self.size))
            pygame.draw.rect(surface, BLUE ,s)

        elif self.pos==1:#horizontal position, nipple down
            r = pygame.Rect((self.position[0], self.position[1]), (self.size*3, self.size))
            pygame.draw.rect(surface, BLUE ,r)
            s = pygame.Rect((self.position[0]+self.size, self.position[1]+self.size), (self.size, self.size))
            pygame.draw.rect(surface, BLUE ,s)

        elif self.pos==2:#vertical position, nipple right
            r = pygame.Rect((self.position[0], self.position[1]), (self.size, self.size*3))
            pygame.draw.rect(surface, BLUE ,r)
            s = pygame.Rect((self.position[0]+self.size, self.position[1]+self.size), (self.size, self.size))
            pygame.draw.rect(surface, BLUE ,s)

        else:#horizontal position, nipple up
            r = pygame.Rect((self.position[0], self.position[1]), (self.size*3, self.size))
            pygame.draw.rect(surface, BLUE ,r)
            s = pygame.Rect((self.position[0]+self.size, self.position[1]-self.size), (self.size, self.size))
            pygame.draw.rect(surface, BLUE ,s)

    def move(self):

        '''Creates a list of covered areas that are shifted vertically one grid_size up'''
        y_parameters = []
        for i in self.covered_area:
            y_parameters.append([i[0],i[1]-self.size])


        '''moves to the bottom'''
        if self.pos==0 and self.position[1]+3*self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in vertical position with nipple to the left'''
            game_on = False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]
            p_4 = [pos[0]-self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]

        elif self.pos==2 and self.position[1]+3*self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in vertical position with nipple to the right'''

            game_on = False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]
            p_4 = [pos[0]+self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==1 and self.position[1]+2*self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in horizontal position, nipple down'''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]
            p_4 = [pos[0]+self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==3 and self.position[1]+1*self.size >= SCREEN_HEIGHT:
            ''' Instance where the rectangle reaches the bottom in horizontal position, nipple up'''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]
            p_4 = [pos[0]+self.size, pos[1]-self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==0 and ((self.position in self.covered_area) or
            ([self.position[0],self.position[1]+self.size] in self.covered_area) or
            ([self.position[0],self.position[1]+2*self.size] in self.covered_area) or
            ([self.position[0],self.position[1]+3*self.size] in self.covered_area) or
            ([self.position[0]-self.size,self.position[1]+2*self.size] in self.covered_area)):

            ''' Instance where the rectangle reaches the covered area in vertical position with nipple to the left '''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]
            p_4 = [pos[0]-self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==2 and ((self.position in self.covered_area) or
            ([self.position[0],self.position[1]+self.size] in self.covered_area) or
            ([self.position[0],self.position[1]+2*self.size] in self.covered_area) or
            ([self.position[0],self.position[1]+3*self.size] in self.covered_area) or
            ([self.position[0]+self.size,self.position[1]+2*self.size] in self.covered_area)):

            ''' Instance where the rectangle reaches the covered area in vertical position with nipple to the right '''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0], pos[1]+self.size]
            p_3 = [pos[0], pos[1]+2*self.size]
            p_4 = [pos[0]+self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==1 and ((self.position in y_parameters) or
            ([self.position[0]+self.size,self.position[1]] in y_parameters) or
            ([self.position[0]+2*self.size,self.position[1]] in y_parameters) or
            ([self.position[0]+1*self.size,self.position[1]+self.size] in y_parameters)):

            ''' Instance where the rectangle reaches the covered area in horizontal position, nipple down '''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]
            p_4 = [pos[0]+self.size, pos[1]+self.size]

            last_position = [p_1, p_2, p_3, p_4]


        elif self.pos==3 and (([self.position[0],self.position[1]] in y_parameters) or
            ([self.position[0]+self.size,self.position[1]] in y_parameters) or
            ([self.position[0]+2*self.size,self.position[1]] in y_parameters)):

            ''' Instance where the rectangle reaches the covered area in horizontal position, nipple up.'''
            game_on= False

            pos = self.position
            p_1 = [pos[0], pos[1]]
            p_2 = [pos[0]+self.size, pos[1]]
            p_3 = [pos[0]+2*self.size, pos[1]]
            p_4 = [pos[0]+self.size, pos[1]-self.size]

            last_position = [p_1, p_2, p_3, p_4]


        else:
            ''' Instance where the rectangle is still moving down'''
            self.position[1] += GRID_SIZE/5
            game_on = True
            last_position = False

        return game_on, last_position

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:


                if event.key == pygame.K_UP: #Flipping

                    if self.pos==0 and (self.position[0]>=SCREEN_WIDTH-2*self.size):#case when rectangle is in vert. position and is to be flipped as to move out of the screen:
                        pass
                    elif self.pos<4:
                        self.pos +=1
                        print(self.pos)
                    else:
                        self.pos = 0


                elif event.key == pygame.K_LEFT:
                    if self.position[0] - self.size <0:
                        pass
                    else:
                        self.position[0] -= self.size


                elif event.key == pygame.K_RIGHT:

                    if self.pos%2==1 and (self.position[0]+ 3*self.size >= SCREEN_WIDTH):
                            pass

                    elif self.pos%2==0 and (self.position[0] + self.size >= SCREEN_WIDTH):
                            pass
                    else:
                        self.position[0] += self.size


                return event.key

'''Global Variables'''

SCREEN_HEIGHT = 200
SCREEN_WIDTH = 140
GRID_SIZE = 10

#Colors
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,255,0)
ORANGE = (255,165,0)




def main():

    pygame.init() #instantiate the game
    clock = pygame.time.Clock() #set up clock
    myFont = pygame.font.SysFont('monospace', 15) #define the font

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set up the screen
    surface = pygame.Surface(screen.get_size()) #set up the surface
    surface = surface.convert()



    covered_area = [] # create a variable that holds all areas where previous rectangles fell onto.
    SCORE = 0

    fallen_blocks = Fallen_Blocks(covered_area) #instantiate fallen blocks class


    while True:

        random_no = random.random()
        if random_no < 0.5:
            klasa = Rectangle(covered_area) #instantiate the rectangle class
        else:
            klasa = Half_Cross(covered_area)

        game_on = True #Flag


        while game_on:
            clock.tick(15)


            surface.fill(BLACK) #Fills the surface black so that the shape does not trail

            '''Draw the items'''


            klasa.draw(surface)
            # rectangle.draw(surface)

            fallen_blocks.draw(surface)

            game_on, l_position = klasa.move() #moves the rectangle down, returns information whether the game is still on, provides the last position of the fallen block

            '''Create a mark of where the block landed'''
            if l_position == False:
                pass
            else:
                for i in l_position:
                    covered_area.append(i)
            # print(covered_area)
            '''______________'''


            klasa.handle_keys()



            '''This part takes care of a completed layer'''
            #creates a dictionary for all heights for the screen
            full_layer_dic = {}
            for height in range(0,SCREEN_HEIGHT,GRID_SIZE):
                full_layer_dic[height]=0


            #counts grid squares covered by fallen blocks for each height:
            for height in range(0,SCREEN_HEIGHT,GRID_SIZE):
                for coordinate in covered_area:
                    if coordinate[1] == height:
                        full_layer_dic[height] += 1


            for key,value in full_layer_dic.items():
                if value == SCREEN_WIDTH/GRID_SIZE:

                    SCORE += 1 #Increment the score for a completed layer
                    print(SCORE)

                    for idx, val in enumerate(covered_area): #removes the completed layer
                        if val[1]==key:
                            covered_area[idx] = [200,200]

                    for item in covered_area: #moves layers above the removed layer one grid size down
                        if item[1]>value:
                            item[1] += GRID_SIZE

                    print(covered_area)
            '''________________________________'''




            '''Labels'''
            text_score = "Score: "+ str(SCORE)
            score_label = myFont.render(text_score, 1, YELLOW)
            '''Labels'''

            screen.blit(surface, (0,0)) #blit the surface onto the screen
            screen.blit(score_label, (0.1*SCREEN_WIDTH, SCREEN_HEIGHT*0.1)) #label needs to be blit on top of the surface
            pygame.display.update()



main()


