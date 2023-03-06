import numpy as np
import matplotlib.pyplot as ply
from animateplot import AnimatPlot # import AnimatPlot


x = np.linspace(-10,10,200)
np.seterr(all="ignore")

def sig(x):
  return 1/(1+np.exp(-x))

def call_plt(plt,y,x):
  plt.style.use('seaborn')
  plt.plot(x,y)
  plt.title('sigmoid function')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.xlim(-10,10)
  plt.ylim(0,1)
  return plt


def test_render():
    anime = AnimatPlot(sig,x,callback_plot=call_plt)
    #anime.delete_cache()
    anime.render_cache()
    #anime.render_gif('tests/gifs/sigmoid.gif')
    anime.render_mp4('tests/videos/sigmoid.mp4',fps=10)
    
