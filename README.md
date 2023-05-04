<div align='center'>

<img height='200'  width='200' src='imgs/logo.png'>
<h2>AnimatePlot</h2>

</div>



### Examples 


#### Gif 

```py
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


def test_render_gif():
    anime = AnimatPlot(sig,x,callback_plot=call_plt)
    anime.delete_cache()
    anime.render_cache()
    anime.render_gif('tests/gifs/sigmoid.gif')



test_render_gif()
```
```sh
logs:
ended saved cache images! 
[200 images saved in 30.9s | speed: 6.5/img/s | ping: 15.5ms]
[Figure size 576x396 with 0 Axes]
```
saving the files from cache:
```py
anime.render_gif(path='plot.gif',fps=8.7)
```
```sh
logs: plot.gif saved in 6.8s
```
<img src='https://github.com/reinanbr/animatPlot/blob/main/imgs/plot%20(9).gif?raw=true'>


