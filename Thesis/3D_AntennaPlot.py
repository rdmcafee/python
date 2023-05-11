'''
Created on Apr 29, 2023

@author: Mcrye
'''
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')

class emitter():

    def __init__(self, x, y, z, c, f, phi, color = 'blue'):

        self.r, self.c, self.f = np.array([x, y, z]), c, f

        self.color = color

        self.setup()

        self.mag()

        self.phi = phi

    def setup(self):
        self.lambda0 = self.c/self.f
        self.T = 1/self.f
        self.k = 2*np.pi/self.lambda0
        self.w = 2*np.pi*self.f

    def mag(self):
        self.m = (self.r[0]**2 + self.r[1]**2 + self.r[2]**2)**1/2
    

class P():
    def __init__(self, rho, theta, phi):
        self.rho, self.theta, self.phi = rho, theta, phi
        x = rho*np.cos(theta)*np.sin(phi)
        y = rho*np.sin(theta)*np.sin(phi)
        z = rho*np.sin(phi)

        self.r = np.array([x, y, z])

        self.mag()

    def mag(self):
        self.m = (self.r[0]**2 + self.r[1]**2 + self.r[2]**2)**(1/2)


class phasedArray():

    def __init__(self, size, c, f, spacing):
        self.size, self.c, self.f, self.spacing = size, c, f, spacing

        self.Setup()

    def Setup(self):
        self.phase = []
        for i in range(self.size):
            self.phase.append(0)

        self.wl = self.c/self.f

        self.phaser = []

        for i in range(self.size):
            self.phaser.append(emitter(self.wl*(i)*self.spacing-(self.size*self.wl/4),
                                       0, 0, self.c, self.f, self.phase[i]))


def m(a, b):
    r = np.subtract(b, a)
    m = (r[0]**2 + r[1]**2 + r[2]**2)**(1/2)
    return m

def eq(emitters, point):
    '''
       seems messy; I could probably make this an object representing the
       the desired equation. I could put the incoming equations into an array
       this way, I will be able to pass an array of any length into the method
       and loop through it.
    '''

    t = np.linspace(0, emitters[0].T, 1000)
    r = np.zeros_like(emitters)
    eq = np.zeros_like(emitters)

    for i in range(len(emitters)):
        r[i] = m(point, emitters[i].r)

    for i in range(len(r)):
        eq[i] = np.sin(emitters[i].k*r[i] - emitters[i].w*t + emitters[i].phi)

    eq_t = max(np.sum(eq))

    return eq_t

'''
    create a loop to calculate intensity at point P_0 which rotates at a given
    distance, rho, around a complete circle. The increment of i represents the
    desired resolution
'''

phaser_1 = phasedArray(10, 340, 40000, 1/2).phaser

theta = np.linspace(0, 2*np.pi, 50)
phi = np.linspace(-np.pi/2, np.pi/2, 50)
#T, P = np.meshgrid(theta, phi)

r = 0
t = 0
u, v, w = 0, 0, 0
p = -np.pi/2
eq_1 = []

while r < 2:
    w = r
    eq_1.append(eq(phaser_1, [w, u, v])*np.cos(theta)*np.sin(phi))

    while t < 2*np.pi:
        u = r*np.sin(t)
        eq_1.append(eq(phaser_1, [w, u, v])*np.sin(theta)*np.sin(phi))
        t += 0.1
        while p < 2:
            v = p
            eq_1.append(eq(phaser_1, [w, u, v])*np.cos(phi))
            p += 0.1
    r += 0.01
    t = 0
    p = 0

#theta = np.linspace(0, 2*np.pi,len(eq_1))

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


plt.title("Normalized Radiation Pattern [5-Element Phased Array]", fontsize = 12)
plt.polar(theta, eq_1)
plt.tight_layout()
plt.grid(color = 'k', alpha = 0.4)
plt.show()
