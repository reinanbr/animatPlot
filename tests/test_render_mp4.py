import numpy as np
import matplotlib.pyplot as plt
from animateplot import AnimatePlot # import AnimatPlot
plt.style.use('seaborn')

x = np.linspace(-10,10,50)
np.seterr(all="ignore")

def sig(x):
  return 1/(1+np.exp(-x))

def call_plt(plt,y,x):

  plt.plot(x,y)
  plt.title('sigmoid function')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.xlim(-10,10)
  plt.ylim(0,1)
  return plt


def test_render():
    anime = AnimatePlot(sig,x,callback_plot=call_plt)
    anime.render_cache()
    anime.render_mp4('tests/videos/sigmoid.mp4',fps=10)
    
