import math as ma
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# First we can calculate the angular momentum wind (per unit mass)
# at the equator.
u = -8.0                   # Speed at equator
omega = 7.27*(10**(-5))    # Rotation of earth in 1/s
r = 6371*(10**(3))         # Radius of earth

m = (u + omega*r)*r

# Function to calculate the speed per unit mass of the wind
# at a certain latitude by using the conservation of
# angular momtenum.
def speed(theta):
    u = -8.0                   # Speed at equator
    omega = 7.27*(10**(-5))    # Rotation of earth in 1/s
    r = 6371*(10**(3))         # Radius of earth
    m = (u + omega*r)*r        # Angular Momentun at equator

    tmp1 = r*np.cos(theta)
    
    return ( m/tmp1 ) - omega*r*np.cos(theta) 



# So we want to generate data for a "contor plot"
# First an array from -pi/2 to pi/2
# i.e every lattitude of the earth
N = 1000
err = 0.5
uppbd = ma.pi/2.0 - err
lat = np.linspace(-uppbd, uppbd, N)

# And then calculate the subsequent speeds
latspeed = speed(lat)

# Now we want to apply this lat to the world map so we will create
# a "matrix" with each column as latspeed
Nlat = 1000
AllLat = np.zeros((N, Nlat))

for i in range(0, Nlat):
    AllLat[:, i] = latspeed
            

cmap =  mcolors.ListedColormap(['purple', 'blue', 'green', 'yellow', 'red', 'grey'])
bounds= [-20, -5, 10, 25, 40, 55, 1000]
norm =  mcolors.BoundaryNorm(bounds, cmap.N)

img = plt.imshow(AllLat, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm, alpha=0.6)

plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds)
plt.savefig('WindSpeed.png')
plt.show()


from PIL import Image

background = Image.open("OutLine_of_Earth.png")
foreground = Image.open("WindSpeed.png")

background.paste(foreground, (0, 0), foreground)
background.show()



    
