from dados import playing
from animateplot import AnimatePlot as ap
import numpy as np



max = 900_000
n = np.linspace(10,max,200)

#global iter = 1
def call(i,plt):
    N = n[i]
    fig = playing(N)
    plt.title(f"Sessão {i}º de Lançamentos:\nFrequências do Dado Sendo Lançado {int(N)} vezes em uma Sessão")
    return plt



animat = ap(n,call)
animat.render_cache()
animat.render_mp4(path_video=f"test_dados_max={max}.mp4",fps=4)
