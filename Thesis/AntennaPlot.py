'''
Created on Apr 29, 2023

@author: Mcrye
'''
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')

class emitter():
    
    def __init__(self, x, y, c, f, phi, color = 'blue'):
        
        self.r, self.c, self.f = np.array([x, y]), c, f
        
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
        self.m = (self.r[0]**2 + self.r[1]**2)**1/2
    

class P():
    def __init__(self, r, theta):
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        self.r = np.array([x, y])
        
        self.mag()
        
    def mag(self):
        self.m = (self.r[0]**2 + self.r[1]**2)**(1/2)
'''       
e_1 = emitter(-0.0085, 0, 340, 40000, 0)
e_2 = emitter(-0.00425, 0, 340, 40000, 0)  
e_3 = emitter(-0.002125, 0, 340, 40000, 0)   
   
e_4 = emitter(0.002125, 0, 340, 40000, 0)
e_5 = emitter(0.00425, 0, 340, 40000, 0)
e_6 = emitter(0.0085, 0, 340, 40000, 0)
'''
        
'''
q = 0.0085/4
s = 5
ss = 1
e_1 = emitter(-q*(s+3), 0, 340, 40000, np.pi/(2**(ss-1)))
e_2 = emitter(-q*(s+1), 0, 340, 40000, np.pi/(2**(ss)))  
e_3 = emitter(-q*(s), 0, 340, 40000, 0)   
   
e_4 = emitter(q*(s), 0, 340, 40000, 0)
e_5 = emitter(q*(s+1), 0, 340, 40000, np.pi/(2**(ss)))
e_6 = emitter(q*(s+3), 0, 340, 40000, np.pi/(2**(ss-1)))
'''


q = 0.0113
s = 1
e_1 = emitter(-q*(s+1), 0, 340, 40000, 0)
e_2 = emitter(-q*(s), 0, 340, 40000, 0)  
e_3 = emitter(-q*(s*0), 0, 340, 40000, 0)   
   
e_4 = emitter(q*(s), 0, 340, 40000, 0)
e_5 = emitter(q*(s+1), 0, 340, 40000, 0)
#e_6 = emitter(q*(s+3), 0, 340, 40000, 0)

P_0 = P(2, 3*np.pi/2)


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
                                       0, self.c, self.f, self.phase[i]))
'''
    print('Class "ceiling" value = '  + str(e.N))

    lambda_1 = 340/40000
    print('Wavelength = ' + str(lambda_1 * 100) + ' cm')

    N = 1.5/lambda_1
    print('N value = ' + str(np.ceil(N)))
'''

#print(P_0.r)

def m(a, b):
    r = np.subtract(b, a) 
    m = (r[0]**2 + r[1]**2)**(1/2)
    return m

#magnitude of e_1 to P_0
m_1 = m(e_1.r, P_0.r)

#magnitude of e_2 to P_0
m_2 = (m(e_2.r, P_0.r))

def eq(emitters, point):
    '''
       seems messy; I could probably make this an object representing the
       the desired equation. I could put the incoming equations into an array
       this way, I will be able to pass an array of any length into the method
       and loop through it. 
    '''
    
    t = np.linspace(0, emitters[0].T, 1000)
    
    r_1 = m(point.r, emitters[0].r)
    r_2 = m(point.r, emitters[1].r)
    r_3 = m(point.r, emitters[2].r)
    r_4 = m(point.r, emitters[3].r)
    r_5 = m(point.r, emitters[4].r)
    #r_6 = m(point.r, emitters[5].r)
    
    #print(r_1,r_2)
    eq_1 = np.sin(emitters[0].k*r_1 - emitters[0].w * t + emitters[0].phi)
    eq_2 = np.sin(emitters[1].k*r_2 - emitters[1].w * t + emitters[1].phi)
    eq_3 = np.sin(emitters[2].k*r_3 - emitters[2].w * t + emitters[2].phi)
    eq_4 = np.sin(emitters[3].k*r_4 - emitters[3].w * t + emitters[3].phi)
    eq_5 = np.sin(emitters[4].k*r_5 - emitters[4].w * t + emitters[4].phi)
    #eq_6 = np.sin(emitters[5].k*r_6 - emitters[5].w * t + emitters[5].phi)
    
    #eq = max(eq_1+eq_2+eq_3+eq_4+eq_5+eq_6)
    eq = max(eq_1+eq_2+eq_3+eq_4+eq_5)
    '''
    eq = np.format_float_scientific((np.sin(a.k * r_1 + a.phi) + \
                                     np.sin(b.k * r_2 + b.phi)), 4)
    '''
    return eq

'''
    create a loop to calculate intensity at point P_0 which rotates at a given
    distance, rho, around a complete circle. The increment of i represents the 
    desired resolution
'''

vals = []
i = np.pi
while i <= 2*np.pi:
    P_0 = P(1, i)
    
    eq_1 = eq([e_1, e_2, e_3, e_4, e_5], P_0)
    vals.append(eq_1)
    i += 0.001

#eq_1 = eq(e_1, e_2, P_0)

phaser_1 = phasedArray(10, 340, 40000, 1/2)
for i in range(len(phaser_1.phaser)):

    print(phaser_1.phaser[i].r)

#print(vals)
theta = np.linspace(np.pi, 2*np.pi, len(vals))
theta_2 = np.linspace(0, np.pi, 1000)
blankRegion = theta_2*0 + 1
plt.polar(theta, vals/max(vals))
plt.polar(theta_2, blankRegion, color = 'darkred', )
plt.fill_between(theta_2, 0, blankRegion, color = 'darkred', alpha = 0.2)
#plt.polar(theta, vals)
plt.title("Normalized Radiation Pattern [5-Element Phased Array]", fontsize = 12)
plt.tight_layout()
plt.grid(color = 'k', alpha = 0.4)
plt.show()


