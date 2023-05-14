import matplotlib.pyplot as plt
from animateplot import AnimatePlot as Ap
from scipy import special
import numpy as np
plt.style.use('seaborn')

erf = special.erf
x = np.linspace(-2,2,200)



def callback_plot(plt,y,x):

	plt.plot(x,y)
	plt.xlim(-2,2)
	plt.ylim(-1,1)
	plt.xlabel(r'x')
	plt.ylabel(r'erf(x)')
	plt.title('função erro de Gauss')
	return plt



anime = Ap(erf,x,callback_plot=callback_plot)

anime.render_cache()

anime.render_mp4('erf.mp4',fps=10)
