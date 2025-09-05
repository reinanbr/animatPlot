<div align='center'>

<img height='200'  width='200' src='https://raw.githubusercontent.com/reinanbr/animatPlot/main/imgs/logo.png'>
<h2>AnimatePlot</h2>

<p> Making video from plot's</p>
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/reinanbr/animatPlot?logo=codefactor">
<!-- </a><img alt="CircleCI" src="https://img.shields.io/circleci/build/github/reinanbr/animatPlot"> -->
<img alt="Code Climate maintainability" src="https://img.shields.io/codeclimate/maintainability-percentage/reinanbr/animatPlot">

<br/>
<a href='https://pypi.org/project/animateplot/'><img src='https://img.shields.io/pypi/v/animateplot'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/animateplot"></a>
<br/>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/animateplot?color=orange">



</div>



### Examples 


#### sigmoid function

```py
import matplotlib.pyplot as plt
from animateplot import AnimatePlot as Ap
import numpy as np
plt.style.use('seaborn')


def sig(x):
  return 1/(1+np.exp(-x))


x = np.linspace(-10,10,100)
y = sig(x)


def call_plt(it,plt):
  plt.plot(x[:it],y[:it])
  plt.title('sigmoid function')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.xlim(-10,10)
  plt.ylim(0,1)
  return plt



anime = Ap(x,callback_plot=callback_plot)

anime.render_cache()
anime.render_mp4('sigmoid.mp4',fps=15)

```

results:

<br/>

<img src='https://github.com/reinanbr/animatPlot/blob/main/imgs/plot%20(9).gif?raw=true'>

<br>

### Example 2

```py
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

```
<video src='test_2.mp4'></video>