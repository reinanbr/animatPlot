







### Examples 

coding:
```py
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

anime = AnimatePlot(sig,x,callback_plot=call_plt)
anime.render_cache()
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