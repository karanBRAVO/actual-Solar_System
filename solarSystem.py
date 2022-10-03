import pygame
from pygame.locals import *
import math

pygame.init()

clock = pygame.time.Clock()


class Constants:
    def __init__(self):
        self.winWidth = 600
        self.winHeight = 600
        self.fps = 60
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.grey = (192, 192, 192)
        self.font1 = pygame.font.SysFont('monospace', 10, True, False)
        self.window = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("Solar System")

        self.AU = 1.495978707 * 1E+11
        self.M = 1.9891 * 1E+30
        self.G = 6.6743 * 1E-11
        self.Earth_mass = 5.972 * 1E+24

        """ Actual Measurements """
        self.sun_radius = 696340 * 1000

        self.mercury_radius = 2439.7 * 1000
        self.mercury_sun_radius_ratio = self.mercury_radius / self.sun_radius
        self.mercury_semi_major_axis = 0.38709893 * self.AU
        self.mercury_eccentricity = 0.20563069
        self.mercury_foci = self.mercury_eccentricity * self.mercury_semi_major_axis
        self.mercury_semi_minor_axis = ((self.mercury_semi_major_axis ** 2) - (self.mercury_foci ** 2)) ** 0.5

        self.venus_radius = 6051.8 * 1000
        self.venus_sun_radius_ratio = self.venus_radius / self.sun_radius
        self.venus_semi_major_axis = 0.72333199 * self.AU
        self.venus_eccentricity = 0.00677323
        self.venus_foci = self.venus_eccentricity * self.venus_semi_major_axis
        self.venus_semi_minor_axis = ((self.venus_semi_major_axis ** 2) - (self.venus_foci ** 2)) ** 0.5

        self.earth_radius = 6371 * 1000
        self.earth_sun_radius_ratio = self.earth_radius / self.sun_radius
        self.earth_semi_major_axis = 1.00000011 * self.AU
        self.earth_eccentricity = 0.01671022
        self.earth_foci = self.earth_eccentricity * self.earth_semi_major_axis
        self.earth_semi_minor_axis = ((self.earth_semi_major_axis ** 2) - (self.earth_foci ** 2)) ** 0.5

        self.mars_radius = 3389.5 * 1000
        self.mars_sun_radius_ratio = self.mars_radius / self.sun_radius
        self.mars_semi_major_axis = 1.52366231 * self.AU
        self.mars_eccentricity = 0.09341233
        self.mars_foci = self.mars_eccentricity * self.mars_semi_major_axis
        self.mars_semi_minor_axis = ((self.mars_semi_major_axis ** 2) - (self.mars_foci ** 2)) ** 0.5

        self.jupiter_radius = 69911 * 1000
        self.jupiter_sun_radius_ratio = self.jupiter_radius / self.sun_radius
        self.jupiter_semi_major_axis = 5.20336301 * self.AU
        self.jupiter_eccentricity = 0.04839266
        self.jupiter_foci = self.jupiter_eccentricity * self.jupiter_semi_major_axis
        self.jupiter_semi_minor_axis = ((self.jupiter_semi_major_axis ** 2) - (self.jupiter_foci ** 2)) ** 0.5

        """ Scaled Measurements"""
        self.sun_scaled_radius = 10
        
        self.scaled_mercury_radius = (self.mercury_sun_radius_ratio * self.sun_scaled_radius) * 50
        self.scaled_mercury_semi_major_axis = self.mercury_semi_major_axis / 1E+9
        self.scaled_mercury_foci = self.mercury_foci / 1E+9
        self.scaled_mercury_semi_minor_axis = self.mercury_semi_minor_axis / 1E+9
        
        self.scaled_venus_radius = (self.venus_sun_radius_ratio * self.sun_scaled_radius) * 50
        self.scaled_venus_semi_major_axis = self.venus_semi_major_axis / 1E+9
        self.scaled_venus_foci = self.venus_foci / 1E+9
        self.scaled_venus_semi_minor_axis = self.venus_semi_minor_axis / 1E+9

        self.scaled_earth_radius = (self.earth_sun_radius_ratio * self.sun_scaled_radius) * 50
        self.scaled_earth_semi_major_axis = self.earth_semi_major_axis / 1E+9
        self.scaled_earth_foci = self.earth_foci / 1E+9
        self.scaled_earth_semi_minor_axis = self.earth_semi_minor_axis / 1E+9

        self.scaled_mars_radius = (self.mars_sun_radius_ratio * self.sun_scaled_radius) * 50
        self.scaled_mars_semi_major_axis = self.mars_semi_major_axis / 1E+9
        self.scaled_mars_foci = self.mars_foci / 1E+9
        self.scaled_mars_semi_minor_axis = self.mars_semi_minor_axis / 1E+9

        self.scaled_jupiter_radius = (self.jupiter_sun_radius_ratio * self.sun_scaled_radius) * 10
        self.scaled_jupiter_semi_major_axis = self.jupiter_semi_major_axis / 1E+9
        self.scaled_jupiter_foci = self.jupiter_foci / 1E+9
        self.scaled_jupiter_semi_minor_axis = self.jupiter_semi_minor_axis / 1E+9

        """ Positions """
        self.sun_pos = (299.9999903894465, 300)
        self.xCor_sun_pos = self.sun_pos[0]
        self.yCor_sun_pos = self.sun_pos[1]
        
        self.mercury_pos = (self.winWidth // 2 + self.scaled_mercury_semi_major_axis, self.winHeight // 2)
        self.xCor_mercury_pos = self.mercury_pos[0]
        self.yCor_mercury_pos = self.mercury_pos[1]
        
        self.venus_pos = (self.winWidth // 2 + self.scaled_venus_semi_major_axis, self.winHeight // 2)
        self.xCor_venus_pos = self.venus_pos[0]
        self.yCor_venus_pos = self.venus_pos[1]

        self.earth_pos = (self.winWidth // 2 + self.scaled_earth_semi_major_axis, self.winHeight // 2)
        self.xCor_earth_pos = self.earth_pos[0]
        self.yCor_earth_pos = self.earth_pos[1]

        self.mars_pos = (self.winWidth // 2 + self.scaled_mars_semi_major_axis, self.winHeight // 2)
        self.xCor_mars_pos = self.mars_pos[0]
        self.yCor_mars_pos = self.mars_pos[1]

        self.jupiter_pos = (self.winWidth // 2 + self.scaled_jupiter_semi_major_axis, self.winHeight // 2)
        self.xCor_jupiter_pos = self.jupiter_pos[0]
        self.yCor_jupiter_pos = self.jupiter_pos[1]

    def blitText(self):
        message1 = self.font1.render('Sun', True, self.blue)
        message1Rect = message1.get_rect()
        message1Rect.center = (self.xCor_sun_pos, self.yCor_sun_pos)
        self.window.blit(message1, message1Rect)

        message2 = self.font1.render(f"{self.xCor_sun_pos}, {self.yCor_sun_pos}", True, self.white)
        self.window.blit(message2, (message1Rect.x - 50, message1Rect.y + 15))

    def drawAxis(self):
        pygame.draw.line(self.window, self.red, (self.winWidth // 2, 0), (self.winWidth // 2, self.winHeight), 1)  # y-axis
        pygame.draw.line(self.window, self.red, (0, self.winHeight // 2), (self.winWidth, self.winHeight // 2), 1)  # x-axis


class Main(Constants):
    def __init__(self):
        super().__init__()
        self.font2 = pygame.font.SysFont('monospace', 12, True, False)

        self.sin_neg = 1
        self.cos_neg = 1

        self.mercury_turn = 1
        self.mercury_pos_lst = []

        self.venus_turn = 1
        self.venus_pos_lst = []

        self.earth_turn = 1
        self.earth_pos_lst = []

        self.mars_turn = 1
        self.mars_pos_lst = []

        self.jupiter_turn = 1
        self.jupiter_pos_lst = []

    def mercuryMove(self):
        x_mercury = 0
        y_mercury = 0
        phi_mercury = 0

        if self.xCor_mercury_pos - self.xCor_sun_pos > 0:
            x_mercury = self.xCor_mercury_pos - self.xCor_sun_pos
        elif self.xCor_mercury_pos - self.xCor_sun_pos < 0:
            x_mercury = self.xCor_sun_pos - self.xCor_mercury_pos
        if self.yCor_sun_pos - self.yCor_mercury_pos > 0:
            y_mercury = self.yCor_sun_pos - self.yCor_mercury_pos
        elif self.yCor_sun_pos - self.yCor_mercury_pos < 0:
            y_mercury = self.yCor_mercury_pos - self.yCor_sun_pos

        d_mercury = ((x_mercury ** 2) + (y_mercury ** 2)) ** 0.5
        message3 = self.font2.render(f"d(m)= {d_mercury * 1E+9}", True, self.white)
        self.window.blit(message3, (self.xCor_mercury_pos - 50, self.yCor_mercury_pos - 15))

        dx_mercury = self.xCor_mercury_pos - self.winWidth // 2
        dy_mercury = self.winHeight // 2 - self.yCor_mercury_pos

        mercury_planetVel = ((self.G * self.M) / (d_mercury * 1E+9)) ** 0.5
        mercury_scaled_planetVel = mercury_planetVel / 1E+4
        message4 = self.font2.render(f"v(m/s)= {mercury_planetVel}", True, self.white)
        self.window.blit(message4, (self.xCor_mercury_pos - 50, self.yCor_mercury_pos + 15))

        if dx_mercury != 0:
            phi_mercury = math.atan(dy_mercury / dx_mercury)
        elif dx_mercury == 0:
            phi_mercury = math.pi / 2

        if math.sin(phi_mercury) <= 0:
            self.sin_neg = -1
        elif math.sin(phi_mercury) > 0:
            self.sin_neg = 1
        if math.cos(phi_mercury) <= 0:
            self.cos_neg = -1
        elif math.cos(phi_mercury) > 0:
            self.cos_neg = 1

        mercury_planet_xVel = mercury_scaled_planetVel * math.sin(phi_mercury) * self.sin_neg
        mercury_planet_yVel = mercury_scaled_planetVel * math.cos(phi_mercury) * self.cos_neg

        pygame.draw.line(self.window, self.white, (self.xCor_sun_pos, self.yCor_sun_pos), (self.xCor_mercury_pos, self.yCor_mercury_pos), 1)

        if self.mercury_turn == 1:
            if self.winWidth // 2 < self.xCor_mercury_pos <= self.winWidth // 2 + self.scaled_mercury_semi_major_axis:
                self.xCor_mercury_pos -= mercury_planet_xVel
                if self.winHeight // 2 - self.scaled_mercury_semi_minor_axis < self.yCor_mercury_pos <= self.winHeight // 2:
                    self.yCor_mercury_pos -= mercury_planet_yVel

                if self.xCor_mercury_pos <= self.winWidth // 2:
                    self.xCor_mercury_pos = self.winWidth // 2
                if self.yCor_mercury_pos <= self.winHeight // 2 - self.scaled_mercury_semi_minor_axis:
                    self.yCor_mercury_pos = self.winHeight // 2 - self.scaled_mercury_semi_minor_axis

            elif self.winHeight // 2 - self.scaled_mercury_semi_major_axis <= self.xCor_mercury_pos <= self.winWidth // 2:
                self.xCor_mercury_pos -= mercury_planet_xVel
                if self.winHeight // 2 - self.scaled_mercury_semi_minor_axis <= self.yCor_mercury_pos <= self.winHeight // 2:
                    self.yCor_mercury_pos += mercury_planet_yVel

                if self.xCor_mercury_pos <= self.winWidth // 2 - self.scaled_mercury_semi_major_axis:
                    self.xCor_mercury_pos = self.winWidth // 2 - self.scaled_mercury_semi_major_axis
                if self.yCor_mercury_pos >= self.winHeight // 2:
                    self.yCor_mercury_pos = self.winHeight // 2

            if self.xCor_mercury_pos == self.winWidth // 2 - self.scaled_mercury_semi_major_axis and self.yCor_mercury_pos == self.winHeight // 2:
                self.mercury_turn = 2
        if self.mercury_turn == 2:
            if self.winWidth // 2 - self.scaled_mercury_semi_major_axis <= self.xCor_mercury_pos < self.winWidth // 2:
                self.xCor_mercury_pos += mercury_planet_xVel
                if self.winHeight // 2 <= self.yCor_mercury_pos < self.winHeight // 2 + self.scaled_mercury_semi_minor_axis:
                    self.yCor_mercury_pos += mercury_planet_yVel

                if self.xCor_mercury_pos >= self.winWidth // 2:
                    self.xCor_mercury_pos = self.winWidth // 2
                if self.yCor_mercury_pos >= self.winHeight // 2 + self.scaled_mercury_semi_minor_axis:
                    self.yCor_mercury_pos = self.winHeight // 2 + self.scaled_mercury_semi_minor_axis

            elif self.winWidth // 2 <= self.xCor_mercury_pos <= self.winWidth // 2 + self.scaled_mercury_semi_major_axis:
                self.xCor_mercury_pos += mercury_planet_xVel
                if self.winHeight // 2 <= self.yCor_mercury_pos <= self.winHeight // 2 + self.scaled_mercury_semi_minor_axis:
                    self.yCor_mercury_pos -= mercury_planet_yVel

                if self.xCor_mercury_pos >= self.winWidth // 2 + self.scaled_mercury_semi_major_axis:
                    self.xCor_mercury_pos = self.winWidth // 2 + self.scaled_mercury_semi_major_axis
                if self.yCor_mercury_pos <= self.winHeight // 2:
                    self.yCor_mercury_pos = self.winHeight // 2

            if self.xCor_mercury_pos == self.winWidth // 2 + self.scaled_mercury_semi_major_axis and self.yCor_mercury_pos == self.winHeight // 2:
                self.mercury_turn = 1

        self.mercury_pos_lst.append((self.xCor_mercury_pos, self.yCor_mercury_pos))
        for i in range(0, len(self.mercury_pos_lst)):
            pygame.draw.line(self.window, self.white, self.mercury_pos_lst[i], self.mercury_pos_lst[i], 1)

        message2 = self.font1.render('Mercury', True, self.white)
        self.window.blit(message2, (self.xCor_mercury_pos, self.yCor_mercury_pos))

    def venusMove(self):
        x_venus = 0
        y_venus = 0
        phi_venus = 0

        if self.xCor_venus_pos - self.xCor_sun_pos > 0:
            x_venus = self.xCor_venus_pos - self.xCor_sun_pos
        elif self.xCor_venus_pos - self.xCor_sun_pos < 0:
            x_venus = self.xCor_sun_pos - self.xCor_venus_pos
        if self.yCor_sun_pos - self.yCor_venus_pos > 0:
            y_venus = self.yCor_sun_pos - self.yCor_venus_pos
        elif self.yCor_sun_pos - self.yCor_venus_pos < 0:
            y_venus = self.yCor_venus_pos - self.yCor_sun_pos

        d_venus = ((x_venus ** 2) + (y_venus ** 2)) ** 0.5
        message3 = self.font2.render(f"d(m)= {d_venus * 1E+9}", True, self.white)
        self.window.blit(message3, (self.xCor_venus_pos - 50, self.yCor_venus_pos - 15))

        dx_venus = self.xCor_venus_pos - self.winWidth // 2
        dy_venus = self.winHeight // 2 - self.yCor_venus_pos

        planetVel = ((self.G * self.M) / (d_venus * 1E+9)) ** 0.5
        scaled_planetVel = planetVel / 1E+4
        message4 = self.font2.render(f"v(m/s)= {planetVel}", True, self.white)
        self.window.blit(message4, (self.xCor_venus_pos - 50, self.yCor_venus_pos + 15))

        if dx_venus != 0:
            phi_venus = math.atan(dy_venus / dx_venus)
        elif dx_venus == 0:
            phi_venus = math.pi / 2

        if math.sin(phi_venus) <= 0:
            self.sin_neg = -1
        elif math.sin(phi_venus) > 0:
            self.sin_neg = 1
        if math.cos(phi_venus) <= 0:
            self.cos_neg = -1
        elif math.cos(phi_venus) > 0:
            self.cos_neg = 1

        planet_xVel = scaled_planetVel * math.sin(phi_venus) * self.sin_neg
        planet_yVel = scaled_planetVel * math.cos(phi_venus) * self.cos_neg

        pygame.draw.line(self.window, self.white, (self.xCor_sun_pos, self.yCor_sun_pos), (self.xCor_venus_pos, self.yCor_venus_pos), 1)

        if self.venus_turn == 1:
            if self.winWidth // 2 < self.xCor_venus_pos <= self.winWidth // 2 + self.scaled_venus_semi_major_axis:
                self.xCor_venus_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_venus_semi_minor_axis < self.yCor_venus_pos <= self.winHeight // 2:
                    self.yCor_venus_pos -= planet_yVel

                if self.xCor_venus_pos <= self.winWidth // 2:
                    self.xCor_venus_pos = self.winWidth // 2
                if self.yCor_venus_pos <= self.winHeight // 2 - self.scaled_venus_semi_minor_axis:
                    self.yCor_venus_pos = self.winHeight // 2 - self.scaled_venus_semi_minor_axis

            elif self.winHeight // 2 - self.scaled_venus_semi_major_axis <= self.xCor_venus_pos <= self.winWidth // 2:
                self.xCor_venus_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_venus_semi_minor_axis <= self.yCor_venus_pos <= self.winHeight // 2:
                    self.yCor_venus_pos += planet_yVel

                if self.xCor_venus_pos <= self.winWidth // 2 - self.scaled_venus_semi_major_axis:
                    self.xCor_venus_pos = self.winWidth // 2 - self.scaled_venus_semi_major_axis
                if self.yCor_venus_pos >= self.winHeight // 2:
                    self.yCor_venus_pos = self.winHeight // 2

            if self.xCor_venus_pos == self.winWidth // 2 - self.scaled_venus_semi_major_axis and self.yCor_venus_pos == self.winHeight // 2:
                self.venus_turn = 2
        if self.venus_turn == 2:
            if self.winWidth // 2 - self.scaled_venus_semi_major_axis <= self.xCor_venus_pos < self.winWidth // 2:
                self.xCor_venus_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_venus_pos < self.winHeight // 2 + self.scaled_venus_semi_minor_axis:
                    self.yCor_venus_pos += planet_yVel

                if self.xCor_venus_pos >= self.winWidth // 2:
                    self.xCor_venus_pos = self.winWidth // 2
                if self.yCor_venus_pos >= self.winHeight // 2 + self.scaled_venus_semi_minor_axis:
                    self.yCor_venus_pos = self.winHeight // 2 + self.scaled_venus_semi_minor_axis

            elif self.winWidth // 2 <= self.xCor_venus_pos <= self.winWidth // 2 + self.scaled_venus_semi_major_axis:
                self.xCor_venus_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_venus_pos <= self.winHeight // 2 + self.scaled_venus_semi_minor_axis:
                    self.yCor_venus_pos -= planet_yVel

                if self.xCor_venus_pos >= self.winWidth // 2 + self.scaled_venus_semi_major_axis:
                    self.xCor_venus_pos = self.winWidth // 2 + self.scaled_venus_semi_major_axis
                if self.yCor_venus_pos <= self.winHeight // 2:
                    self.yCor_venus_pos = self.winHeight // 2

            if self.xCor_venus_pos == self.winWidth // 2 + self.scaled_venus_semi_major_axis and self.yCor_venus_pos == self.winHeight // 2:
                self.venus_turn = 1

        self.venus_pos_lst.append((self.xCor_venus_pos, self.yCor_venus_pos))
        for i in range(0, len(self.venus_pos_lst)):
            pygame.draw.line(self.window, self.white, self.venus_pos_lst[i], self.venus_pos_lst[i], 1)

        message2 = self.font1.render('Venus', True, self.white)
        self.window.blit(message2, (self.xCor_venus_pos, self.yCor_venus_pos))

    def earthMove(self):
        x_earth = 0
        y_earth = 0
        phi_earth = 0

        if self.xCor_earth_pos - self.xCor_sun_pos > 0:
            x_earth = self.xCor_earth_pos - self.xCor_sun_pos
        elif self.xCor_earth_pos - self.xCor_sun_pos < 0:
            x_earth = self.xCor_sun_pos - self.xCor_earth_pos
        if self.yCor_sun_pos - self.yCor_earth_pos > 0:
            y_earth = self.yCor_sun_pos - self.yCor_earth_pos
        elif self.yCor_sun_pos - self.yCor_earth_pos < 0:
            y_earth = self.yCor_earth_pos - self.yCor_sun_pos

        d_earth = ((x_earth ** 2) + (y_earth ** 2)) ** 0.5
        message3 = self.font2.render(f"d(m)= {d_earth * 1E+9}", True, self.white)
        self.window.blit(message3, (self.xCor_earth_pos - 50, self.yCor_earth_pos - 15))

        dx_earth = self.xCor_earth_pos - self.winWidth // 2
        dy_earth = self.winHeight // 2 - self.yCor_earth_pos

        planetVel = ((self.G * self.M) / (d_earth * 1E+9)) ** 0.5
        scaled_planetVel = planetVel / 1E+4
        message4 = self.font2.render(f"v(m/s)= {planetVel}", True, self.white)
        self.window.blit(message4, (self.xCor_earth_pos - 50, self.yCor_earth_pos + 15))

        if dx_earth != 0:
            phi_earth = math.atan(dy_earth / dx_earth)
        elif dx_earth == 0:
            phi_earth = math.pi / 2

        if math.sin(phi_earth) <= 0:
            self.sin_neg = -1
        elif math.sin(phi_earth) > 0:
            self.sin_neg = 1
        if math.cos(phi_earth) <= 0:
            self.cos_neg = -1
        elif math.cos(phi_earth) > 0:
            self.cos_neg = 1

        planet_xVel = scaled_planetVel * math.sin(phi_earth) * self.sin_neg
        planet_yVel = scaled_planetVel * math.cos(phi_earth) * self.cos_neg

        pygame.draw.line(self.window, self.white, (self.xCor_sun_pos, self.yCor_sun_pos), (self.xCor_earth_pos, self.yCor_earth_pos), 1)

        if self.earth_turn == 1:
            if self.winWidth // 2 < self.xCor_earth_pos <= self.winWidth // 2 + self.scaled_earth_semi_major_axis:
                self.xCor_earth_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_earth_semi_minor_axis < self.yCor_earth_pos <= self.winHeight // 2:
                    self.yCor_earth_pos -= planet_yVel

                if self.xCor_earth_pos <= self.winWidth // 2:
                    self.xCor_earth_pos = self.winWidth // 2
                if self.yCor_earth_pos <= self.winHeight // 2 - self.scaled_earth_semi_minor_axis:
                    self.yCor_earth_pos = self.winHeight // 2 - self.scaled_earth_semi_minor_axis

            elif self.winHeight // 2 - self.scaled_earth_semi_major_axis <= self.xCor_earth_pos <= self.winWidth // 2:
                self.xCor_earth_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_earth_semi_minor_axis <= self.yCor_earth_pos <= self.winHeight // 2:
                    self.yCor_earth_pos += planet_yVel

                if self.xCor_earth_pos <= self.winWidth // 2 - self.scaled_earth_semi_major_axis:
                    self.xCor_earth_pos = self.winWidth // 2 - self.scaled_earth_semi_major_axis
                if self.yCor_earth_pos >= self.winHeight // 2:
                    self.yCor_earth_pos = self.winHeight // 2

            if self.xCor_earth_pos == self.winWidth // 2 - self.scaled_earth_semi_major_axis and self.yCor_earth_pos == self.winHeight // 2:
                self.earth_turn = 2
        if self.earth_turn == 2:
            if self.winWidth // 2 - self.scaled_earth_semi_major_axis <= self.xCor_earth_pos < self.winWidth // 2:
                self.xCor_earth_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_earth_pos < self.winHeight // 2 + self.scaled_earth_semi_minor_axis:
                    self.yCor_earth_pos += planet_yVel

                if self.xCor_earth_pos >= self.winWidth // 2:
                    self.xCor_earth_pos = self.winWidth // 2
                if self.yCor_earth_pos >= self.winHeight // 2 + self.scaled_earth_semi_minor_axis:
                    self.yCor_earth_pos = self.winHeight // 2 + self.scaled_earth_semi_minor_axis

            elif self.winWidth // 2 <= self.xCor_earth_pos <= self.winWidth // 2 + self.scaled_earth_semi_major_axis:
                self.xCor_earth_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_earth_pos <= self.winHeight // 2 + self.scaled_earth_semi_minor_axis:
                    self.yCor_earth_pos -= planet_yVel

                if self.xCor_earth_pos >= self.winWidth // 2 + self.scaled_earth_semi_major_axis:
                    self.xCor_earth_pos = self.winWidth // 2 + self.scaled_earth_semi_major_axis
                if self.yCor_earth_pos <= self.winHeight // 2:
                    self.yCor_earth_pos = self.winHeight // 2

            if self.xCor_earth_pos == self.winWidth // 2 + self.scaled_earth_semi_major_axis and self.yCor_earth_pos == self.winHeight // 2:
                self.earth_turn = 1

        self.earth_pos_lst.append((self.xCor_earth_pos, self.yCor_earth_pos))
        for i in range(0, len(self.earth_pos_lst)):
            pygame.draw.line(self.window, self.white, self.earth_pos_lst[i], self.earth_pos_lst[i], 1)

        message2 = self.font1.render('Earth', True, self.white)
        self.window.blit(message2, (self.xCor_earth_pos, self.yCor_earth_pos))

    def marsMove(self):
        x_mars = 0
        y_mars = 0
        phi_mars = 0

        if self.xCor_mars_pos - self.xCor_sun_pos > 0:
            x_mars = self.xCor_mars_pos - self.xCor_sun_pos
        elif self.xCor_mars_pos - self.xCor_sun_pos < 0:
            x_mars = self.xCor_sun_pos - self.xCor_mars_pos
        if self.yCor_sun_pos - self.yCor_mars_pos > 0:
            y_mars = self.yCor_sun_pos - self.yCor_mars_pos
        elif self.yCor_sun_pos - self.yCor_mars_pos < 0:
            y_mars = self.yCor_mars_pos - self.yCor_sun_pos

        d_mars = ((x_mars ** 2) + (y_mars ** 2)) ** 0.5
        message3 = self.font2.render(f"d(m)= {d_mars * 1E+9}", True, self.white)
        self.window.blit(message3, (self.xCor_mars_pos - 50, self.yCor_mars_pos - 15))

        dx_mars = self.xCor_mars_pos - self.winWidth // 2
        dy_mars = self.winHeight // 2 - self.yCor_mars_pos

        planetVel = ((self.G * self.M) / (d_mars * 1E+9)) ** 0.5
        scaled_planetVel = planetVel / 1E+4
        message4 = self.font2.render(f"v(m/s)= {planetVel}", True, self.white)
        self.window.blit(message4, (self.xCor_mars_pos - 50, self.yCor_mars_pos + 15))

        if dx_mars != 0:
            phi_mars = math.atan(dy_mars / dx_mars)
        elif dx_mars == 0:
            phi_mars = math.pi / 2

        if math.sin(phi_mars) <= 0:
            self.sin_neg = -1
        elif math.sin(phi_mars) > 0:
            self.sin_neg = 1
        if math.cos(phi_mars) <= 0:
            self.cos_neg = -1
        elif math.cos(phi_mars) > 0:
            self.cos_neg = 1

        planet_xVel = scaled_planetVel * math.sin(phi_mars) * self.sin_neg
        planet_yVel = scaled_planetVel * math.cos(phi_mars) * self.cos_neg

        pygame.draw.line(self.window, self.white, (self.xCor_sun_pos, self.yCor_sun_pos), (self.xCor_mars_pos, self.yCor_mars_pos), 1)

        if self.mars_turn == 1:
            if self.winWidth // 2 < self.xCor_mars_pos <= self.winWidth // 2 + self.scaled_mars_semi_major_axis:
                self.xCor_mars_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_mars_semi_minor_axis < self.yCor_mars_pos <= self.winHeight // 2:
                    self.yCor_mars_pos -= planet_yVel

                if self.xCor_mars_pos <= self.winWidth // 2:
                    self.xCor_mars_pos = self.winWidth // 2
                if self.yCor_mars_pos <= self.winHeight // 2 - self.scaled_mars_semi_minor_axis:
                    self.yCor_mars_pos = self.winHeight // 2 - self.scaled_mars_semi_minor_axis

            elif self.winHeight // 2 - self.scaled_mars_semi_major_axis <= self.xCor_mars_pos <= self.winWidth // 2:
                self.xCor_mars_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_mars_semi_minor_axis <= self.yCor_mars_pos <= self.winHeight // 2:
                    self.yCor_mars_pos += planet_yVel

                if self.xCor_mars_pos <= self.winWidth // 2 - self.scaled_mars_semi_major_axis:
                    self.xCor_mars_pos = self.winWidth // 2 - self.scaled_mars_semi_major_axis
                if self.yCor_mars_pos >= self.winHeight // 2:
                    self.yCor_mars_pos = self.winHeight // 2

            if self.xCor_mars_pos == self.winWidth // 2 - self.scaled_mars_semi_major_axis and self.yCor_mars_pos == self.winHeight // 2:
                self.mars_turn = 2
        if self.mars_turn == 2:
            if self.winWidth // 2 - self.scaled_mars_semi_major_axis <= self.xCor_mars_pos < self.winWidth // 2:
                self.xCor_mars_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_mars_pos < self.winHeight // 2 + self.scaled_mars_semi_minor_axis:
                    self.yCor_mars_pos += planet_yVel

                if self.xCor_mars_pos >= self.winWidth // 2:
                    self.xCor_mars_pos = self.winWidth // 2
                if self.yCor_mars_pos >= self.winHeight // 2 + self.scaled_mars_semi_minor_axis:
                    self.yCor_mars_pos = self.winHeight // 2 + self.scaled_mars_semi_minor_axis

            elif self.winWidth // 2 <= self.xCor_mars_pos <= self.winWidth // 2 + self.scaled_mars_semi_major_axis:
                self.xCor_mars_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_mars_pos <= self.winHeight // 2 + self.scaled_mars_semi_minor_axis:
                    self.yCor_mars_pos -= planet_yVel

                if self.xCor_mars_pos >= self.winWidth // 2 + self.scaled_mars_semi_major_axis:
                    self.xCor_mars_pos = self.winWidth // 2 + self.scaled_mars_semi_major_axis
                if self.yCor_mars_pos <= self.winHeight // 2:
                    self.yCor_mars_pos = self.winHeight // 2

            if self.xCor_mars_pos == self.winWidth // 2 + self.scaled_mars_semi_major_axis and self.yCor_mars_pos == self.winHeight // 2:
                self.mars_turn = 1

        self.mars_pos_lst.append((self.xCor_mars_pos, self.yCor_mars_pos))
        for i in range(0, len(self.mars_pos_lst)):
            pygame.draw.line(self.window, self.white, self.mars_pos_lst[i], self.mars_pos_lst[i], 1)

        message2 = self.font1.render('Mars', True, self.white)
        self.window.blit(message2, (self.xCor_mars_pos, self.yCor_mars_pos))

    def jupiterMove(self):
        x_jupiter = 0
        y_jupiter = 0
        phi_jupiter = 0

        if self.xCor_jupiter_pos - self.xCor_sun_pos > 0:
            x_jupiter = self.xCor_jupiter_pos - self.xCor_sun_pos
        elif self.xCor_jupiter_pos - self.xCor_sun_pos < 0:
            x_jupiter = self.xCor_sun_pos - self.xCor_jupiter_pos
        if self.yCor_sun_pos - self.yCor_jupiter_pos > 0:
            y_jupiter = self.yCor_sun_pos - self.yCor_jupiter_pos
        elif self.yCor_sun_pos - self.yCor_jupiter_pos < 0:
            y_jupiter = self.yCor_jupiter_pos - self.yCor_sun_pos

        d_jupiter = ((x_jupiter ** 2) + (y_jupiter ** 2)) ** 0.5
        message3 = self.font2.render(f"d(m)= {d_jupiter * 1E+9}", True, self.white)

        dx_jupiter = self.xCor_jupiter_pos - self.winWidth // 2
        dy_jupiter = self.winHeight // 2 - self.yCor_jupiter_pos

        planetVel = ((self.G * self.M) / (d_jupiter * 1E+9)) ** 0.5
        scaled_planetVel = (planetVel / 1E+4)
        message4 = self.font2.render(f"v(m/s)= {planetVel}", True, self.white)

        message2 = self.font1.render('Jupiter', True, self.white)

        if dx_jupiter != 0:
            phi_jupiter = math.atan(dy_jupiter / dx_jupiter)
        elif dx_jupiter == 0:
            phi_jupiter = math.pi / 2

        if math.sin(phi_jupiter) <= 0:
            self.sin_neg = -1
        elif math.sin(phi_jupiter) > 0:
            self.sin_neg = 1
        if math.cos(phi_jupiter) <= 0:
            self.cos_neg = -1
        elif math.cos(phi_jupiter) > 0:
            self.cos_neg = 1

        planet_xVel = scaled_planetVel * math.sin(phi_jupiter) * self.sin_neg
        planet_yVel = scaled_planetVel * math.cos(phi_jupiter) * self.cos_neg

        pygame.draw.line(self.window, self.white, (self.xCor_sun_pos, self.yCor_sun_pos), (self.xCor_jupiter_pos, self.yCor_jupiter_pos), 1)

        if self.jupiter_turn == 1:
            if self.winWidth // 2 < self.xCor_jupiter_pos <= self.winWidth // 2 + self.scaled_jupiter_semi_major_axis:
                self.xCor_jupiter_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_jupiter_semi_minor_axis < self.yCor_jupiter_pos <= self.winHeight // 2:
                    self.yCor_jupiter_pos -= planet_yVel

                if self.xCor_jupiter_pos <= self.winWidth // 2:
                    self.xCor_jupiter_pos = self.winWidth // 2
                if self.yCor_jupiter_pos <= self.winHeight // 2 - self.scaled_jupiter_semi_minor_axis:
                    self.yCor_jupiter_pos = self.winHeight // 2 - self.scaled_jupiter_semi_minor_axis

                self.window.blit(message3, (400, 10))
                self.window.blit(message2, (400, 20))
                self.window.blit(message4, (400, 30))
            elif self.winHeight // 2 - self.scaled_jupiter_semi_major_axis <= self.xCor_jupiter_pos <= self.winWidth // 2:
                self.xCor_jupiter_pos -= planet_xVel
                if self.winHeight // 2 - self.scaled_jupiter_semi_minor_axis <= self.yCor_jupiter_pos <= self.winHeight // 2:
                    self.yCor_jupiter_pos += planet_yVel

                if self.xCor_jupiter_pos <= self.winWidth // 2 - self.scaled_jupiter_semi_major_axis:
                    self.xCor_jupiter_pos = self.winWidth // 2 - self.scaled_jupiter_semi_major_axis
                if self.yCor_jupiter_pos >= self.winHeight // 2:
                    self.yCor_jupiter_pos = self.winHeight // 2

                self.window.blit(message3, (20, 10))
                self.window.blit(message2, (20, 20))
                self.window.blit(message4, (20, 30))
            if self.xCor_jupiter_pos == self.winWidth // 2 - self.scaled_jupiter_semi_major_axis and self.yCor_jupiter_pos == self.winHeight // 2:
                self.jupiter_turn = 2
        if self.jupiter_turn == 2:
            if self.winWidth // 2 - self.scaled_jupiter_semi_major_axis <= self.xCor_jupiter_pos < self.winWidth // 2:
                self.xCor_jupiter_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_jupiter_pos < self.winHeight // 2 + self.scaled_jupiter_semi_minor_axis:
                    self.yCor_jupiter_pos += planet_yVel

                if self.xCor_jupiter_pos >= self.winWidth // 2:
                    self.xCor_jupiter_pos = self.winWidth // 2
                if self.yCor_jupiter_pos >= self.winHeight // 2 + self.scaled_jupiter_semi_minor_axis:
                    self.yCor_jupiter_pos = self.winHeight // 2 + self.scaled_jupiter_semi_minor_axis

                self.window.blit(message3, (20, 540))
                self.window.blit(message2, (20, 550))
                self.window.blit(message4, (20, 560))
            elif self.winWidth // 2 <= self.xCor_jupiter_pos <= self.winWidth // 2 + self.scaled_jupiter_semi_major_axis:
                self.xCor_jupiter_pos += planet_xVel
                if self.winHeight // 2 <= self.yCor_jupiter_pos <= self.winHeight // 2 + self.scaled_jupiter_semi_minor_axis:
                    self.yCor_jupiter_pos -= planet_yVel

                if self.xCor_jupiter_pos >= self.winWidth // 2 + self.scaled_jupiter_semi_major_axis:
                    self.xCor_jupiter_pos = self.winWidth // 2 + self.scaled_jupiter_semi_major_axis
                if self.yCor_jupiter_pos <= self.winHeight // 2:
                    self.yCor_jupiter_pos = self.winHeight // 2

                self.window.blit(message3, (410, 540))
                self.window.blit(message2, (410, 550))
                self.window.blit(message4, (410, 560))
            if self.xCor_jupiter_pos == self.winWidth // 2 + self.scaled_jupiter_semi_major_axis and self.yCor_jupiter_pos == self.winHeight // 2:
                self.jupiter_turn = 1

        self.jupiter_pos_lst.append((self.xCor_jupiter_pos, self.yCor_jupiter_pos))
        for i in range(0, len(self.jupiter_pos_lst)):
            pygame.draw.line(self.window, self.white, self.jupiter_pos_lst[i], self.jupiter_pos_lst[i], 1)

    def drawPlanet(self):
        pygame.draw.circle(self.window, self.yellow, (self.xCor_sun_pos, self.yCor_sun_pos), self.sun_scaled_radius)
        pygame.draw.circle(self.window, self.grey, (self.xCor_mercury_pos, self.yCor_mercury_pos), self.scaled_mercury_radius)
        pygame.draw.circle(self.window, self.white, (self.xCor_venus_pos, self.yCor_venus_pos), self.scaled_venus_radius)
        pygame.draw.circle(self.window, self.blue, (self.xCor_earth_pos, self.yCor_earth_pos), self.scaled_earth_radius)
        pygame.draw.circle(self.window, self.red, (self.xCor_mars_pos, self.yCor_mars_pos), self.scaled_mars_radius)
        pygame.draw.circle(self.window, self.grey, (self.xCor_jupiter_pos, self.yCor_jupiter_pos), self.scaled_jupiter_radius)


const = Constants()
mainClass = Main()
print("*** Solar System ***")


def drawGameWindow():
    const.window.fill(const.black)
    const.drawAxis()
    mainClass.drawPlanet()
    const.blitText()
    mainClass.mercuryMove()
    mainClass.venusMove()
    mainClass.earthMove()
    mainClass.marsMove()
    mainClass.jupiterMove()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == KEYDOWN and (event.key == K_ESCAPE):
            run = False

    drawGameWindow()

    pygame.display.update()
    clock.tick(const.fps)
pygame.quit()
