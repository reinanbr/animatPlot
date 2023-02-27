import matplotlib.pyplot as plt
import imageio
import numpy as np
import time



class AnimatePlot:
  pattern_savefig = 'fig_%(i)s.png'
  images = None
  
  def __init__(self,f,x,callback_plot:plt,plt=plt,args=None):
    self.f = f
    self.plot = callback_plot
    self.args = args
    self.x = x
    self.size = len(self.x)
    self.plt = plt



  def render_cache(self):
    self.images = []
    time_init = time.time()
    for i,x in enumerate(self.x):
      #print(f'[{i}/{self._size}]')
      f = self.f(self.x[:i],*self.args)[:i] if self.args else self.f(self.x[:i])[:i]
      plot = self.plot(self.plt,f[:i],self.x[:i])
      img_plot = self.pattern_savefig%{'i':str(i)}
      plot.savefig(img_plot)
      plot.cla()
      plot.clf()
      self.images.append(img_plot)
    ping_total = time.time()-time_init
    ping = 1000*ping_total/self.size
    speed = self.size/ping_total
    print(f'ended saved cache images! \n[{self.size} images saved in {ping_total:.1f}s | speed: {speed:.1f}/img/s | ping: {ping:.1f}ms]')
  

  def render_gif(self,path,fps=8.9):
    if self.images:
      imgs_imread = []
      time_init = time.time()
      for i,img in enumerate(self.images):
        imgs_imread.append(imageio.imread(img))
      imageio.mimsave(path,imgs_imread,fps=fps)
      ping_total = time.time() - time_init
    print(f'{path} saved in {ping_total:.1f}s')

  





