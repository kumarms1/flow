"""
@author: Sadman Ahmed Shanto
"""
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
import seaborn as sns

#bounds for s0,v0,T
s0_bounds = np.linspace(0,5,20)
v0_bounds = np.linspace(0.1,30,20)
T_bounds = np.linspace(1,3,20)

#values of v_array
v = np.linspace(0.1,30,20)
#constants
L = 5

#function definitions
def s_equilibrium(s0,v0,T,v_array):
    numerator = s0 + v_array*T
    denominator = (1 - (v_array/v0)**4)**0.5
    return numerator / denominator

def Q(s0,v0,T,v_array):
    se = s_equilibrium(s0,v0,T,v_array)
    numerator = v_array
    denominator = se + L
    return numerator / denominator

""" dqds0 """
def dqds0(s0,v0,T,v_array):
    numerator = v_array*(1-(v_array/v0)**4)**0.5
    denominator = (s0 + T*v_array + L*(1 - (v_array/v0)**4)**0.5)**2
    return numerator / denominator

def plot_s0_derivative_T(s0,v0,T,v_array):
    for t in T:
        vals = dqds0(s0,v0,t,v_array)
        plt.plot(v_array, vals, label="T = "+str(round(t,3)))
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to s0")
        plt.legend()
        plt.title("Variation of T with s0 = " + str(s0) + " and v0 = " +str(v0))
    plt.show()

def plot_s0_derivative_s0(s0,v0,T,v_array):
    for t in s0:
        vals = dqds0(t,v0,T,v_array)
        plots = plt.plot(v_array, vals, label="s0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
    return plots

def plot_dqds0_varied_v0_T(s0,v0,T,v_array):
    for t in v0:
        vals = dqds0(s0,t,T,v_array)
        plots = plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
    return plots

def plotS0derivative_varied_v0_T():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        plot_dqds0_varied_v0_T(2,v0_bounds,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to s0")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqds0_fixed_s0.gif', writer = 'imagemagick')

def plot_s0_derivative_v0(s0,v0,T,v_array):
    for t in v0:
        vals = dqds0(s0,t,T,v_array)
        plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to s0")
        plt.legend()
        plt.title("Variation of v0 with T = " + str(T) + " and s0 = " +str(s0))
    plt.show()

def plotS0derivative_varied_s0_T():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        t = plot_s0_derivative_s0(s0_bounds,30,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to s0")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqds0_fixed_v0.gif', writer = 'imagemagick')

""" dqdv0 """
def dqdv0(s0,v0,T,v_array):
    numerator = 2*np.power(v_array,L)*(s0 +T*v_array)
    denominator = ((s0 + T*v_array + L*(1 - (v_array/v0)**4)**0.5)**2)*(((1 - (v_array/v0)**4)**0.5)*v0**L)
    return numerator / denominator

def plot_v0_derivative_T(s0,v0,T,v_array):
    for t in T:
        vals = dqdv0(s0,v0,t,v_array)
        plt.plot(v_array, vals, label="T = "+str(round(t,3)))
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to v0")
        plt.legend()
        plt.title("Variation of T with s0 = " + str(s0) + " and v0 = " +str(v0))
    plt.show()

def plot_v0_derivative_s0(s0,v0,T,v_array):
    for t in s0:
        vals = dqdv0(t,v0,T,v_array)
        plots = plt.plot(v_array, vals, label="s0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
        #ax.set_title("T value: "+str(i))
    return plots

def plot_v0_derivative_v0(s0,v0,T,v_array):
    for t in v0:
        vals = dqdv0(s0,t,T,v_array)
        plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to v0")
        plt.legend()
        plt.title("Variation of v0 with T = " + str(T) + " and s0 = " +str(s0))
    plt.show()

def plotV0derivative():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        t = plot_v0_derivative_s0(s0_bounds,30,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to v0")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqdv0_fixed_v0.gif', writer = 'imagemagick')

def plot_dqdv0_varied_v0_T(s0,v0,T,v_array):
    for t in v0:
        vals = dqdv0(s0,t,T,v_array)
        plots = plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
    return plots

def plotV0derivative_varied_v0_T():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        plot_dqdv0_varied_v0_T(2,v0_bounds,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to v0")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqdv0_fixed_s0.gif', writer = 'imagemagick')

""" dqdT"""

def dqdT(s0,v0,T,v_array):
    numerator = (v_array**2)*( (1 - (v_array/v0)**4)**0.5 )
    denominator = (s0 + T*v_array + L*(1 - (v_array/v0)**4)**0.5)**2
    return numerator / denominator

def plot_T_derivative_s0(s0,v0,T,v_array):
    for t in s0:
        vals = dqdT(t,v0,T,v_array)
        plots = plt.plot(v_array, vals, label="s0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
        #ax.set_title("T value: "+str(i))
    return plots

def plot_T_derivative_v0(s0,v0,T,v_array):
    for t in v0:
        vals = dqdT(s0,t,T,v_array)
        plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to v0")
        plt.legend()
        plt.title("Variation of v0 with T = " + str(T) + " and s0 = " +str(s0))
    plt.show()

def plotTderivative_varied_s0_T():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        t = plot_T_derivative_s0(s0_bounds,30,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to T")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqdT_fixed_v0.gif', writer = 'imagemagick')

def plot_dqdT_varied_v0_T(s0,v0,T,v_array):
    for t in v0:
        vals = dqdT(s0,t,T,v_array)
        plots = plt.plot(v_array, vals, label="v0 = "+str(round(t,3)))
        if T == 1:
            plt.legend()
    return plots

def plotTderivative_varied_v0_T():
    sns.set_palette(sns.color_palette("hls", 20))
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111)
    camera = Camera(fig)
    for i in T_bounds:
        plot_dqdT_varied_v0_T(2,v0_bounds,i,v)
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Partial Derivative of Q wrt to T")
        ax.text(0.5, 1.01, "T: " + str(i), transform=ax.transAxes)
        camera.snap()
    animation = camera.animate()
    animation.save('dqdT_fixed_s0.gif', writer = 'imagemagick')


def plotQV_v0(s0=0.5,v0=30,T=1.67,v_array=v):
    for t in v0:
        q = Q(s0,t,T,v_array)
        sns.set_palette(sns.color_palette("hls", 20))
        plt.plot(v_array, q, label="v0 = "+str(round(t,3)))
        plt.legend()
        plt.title("Different v0 parameters")
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Q")
    plt.show()

def plotQV_s0(s0=0.5,v0=30,T=1.67,v_array=v):
    for t in s0:
        q = Q(t,v0,T,v_array)
        sns.set_palette(sns.color_palette("hls", 20))
        plt.plot(v_array, q, label="s0 = "+str(round(t,3)))
        plt.legend()
        plt.title("Different s0 parameters")
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Q")
    plt.show()

def plotQV_T(s0=0.5,v0=30,T=1.67,v_array=v):
    for t in T:
        q = Q(s0,v0,t,v_array)
        sns.set_palette(sns.color_palette("hls", 20))
        plt.plot(v_array, q, label="T = "+str(round(t,3)))
        plt.legend()
        plt.title("Different T parameters")
        plt.xlabel("Veloctiy (m/s)")
        plt.ylabel("Q")
    plt.show()


if __name__ == "__main__":
#   plotV0derivative()
 #  plotS0derivative_varied_v0_T()
 #  plotV0derivative_varied_v0_T()
#   plotTderivative_varied_v0_T()
 #  plotTderivative()
   plotQV_v0(v0=v0_bounds)
   plotQV_s0(s0=s0_bounds)
   plotQV_T(T=T_bounds)
  # plot_T_derivative_v0(3,v0_bounds,2,v)

#find how min and max of each derivative looks like and whether the param vector set at these values are sensible or not
#min values -> most sensitive and max values-> least sensitive
