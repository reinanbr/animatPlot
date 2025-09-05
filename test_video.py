from animateplot import AnimatePlot as ap
import numpy as np

x = np.linspace(0,10,100)

def call(i,plt):
    s = x[:i]
    
    plt.xlim(x[0],x[-1])
    plt.ylim(x[0]**2,x[-1]**2)
    plt.plot(s,s**2)
    return plt


animat = ap(x,call)
animat.render_cache()
animat.render_mp4(path_video="test_2.mp4",fps=15)