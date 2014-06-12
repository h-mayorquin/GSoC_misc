import numpy as np
import matplotlib.pyplot as plt 

def spatial_kernel(x,y, sigma_center, sigma_surround):
    'The spatial component of the kernel. A difference of gaussian'
    
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)  # Distance
    center = (17.0 / sigma_center**2) * np.exp(-(R / sigma_center)**2)
    surround = (16.0 / sigma_surround**2) * np.exp(-(R / sigma_surround)**2)
    return center - surround


def temporal_kernel(t, K1, K2, c1, c2, t1, t2, n1, n2):
    p1 = K1 * ((c1*(t - t1))**n1 * np.exp(-c1*(t - t1))) / ((n1**n1) * np.exp(-n1))
    p2 = K2 * ((c2*(t - t2))**n2 * np.exp(-c2*(t - t2))) / ((n2**n2) * np.exp(-n2))
    p3 = p1 - p2

    return p3

def create_kernel(dx, Lx, dy, Ly, sigma_surround, sigma_center, dt_kernel, kernel_size):
    '''
    Returns the kernel 
    '''
    ## Temporal parameters
    K1 = 1.05
    K2 = 0.7
    c1 = 0.14
    c2 = 0.12
    n1 = 7.0
    n2 = 8.0
    t1 = -6.0
    t2 = -6.0
    td = 6.0
    
    ## Spatial parameters 
    Nx = (Lx / dx)
    Ny = int(Ly / dy )
    # Create the positions 
    x = np.arange(-Lx/2, Lx/2, dx)
    y = np.arange(-Ly/2, Ly/2, dy)
    
    # Call the spatial kernel
    Z = spatial_kernel(x,y, sigma_center, sigma_surround)
    # Call the temporal kernel
    t = np.arange(0, kernel_size * dt_kernel, dt_kernel)
    f_t = temporal_kernel(t, K1, K2, c1, c2, t1, t2, n1, n2)

    # Initialize and fill the spatio-temporal kernel  
    kernel = np.zeros((kernel_size, Nx, Ny))
    for k, ft in enumerate(f_t):
        kernel[k,...] = ft * Z   
    
    return kernel