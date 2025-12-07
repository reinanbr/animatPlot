
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from animateplot import AnimatePlot
from noawclg import get_noaa_data as gnd
from IPython.display import display




data_noaa = gnd(date='17/10/2025')
wind = data_noaa['ugrdmwl'].to_numpy()

def plot_wind(i,plt):

    data = wind[i]
    
    plt.figure(figsize=(14, 8))
    
    # Cria o mapa
    m = Basemap(
        projection='cyl',
        resolution='l',
        llcrnrlat=-90, urcrnrlat=90,
        llcrnrlon=-180, urcrnrlon=180
    )
    
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.3)
    m.fillcontinents(color='lightgray', lake_color='white')
    m.drawmapboundary(fill_color='white')
    m.drawmeridians(np.arange(-180, 181, 60), labels=[0,0,0,1], fontsize=8)
    # Linhas de latitude importantes
    # Equador
    m.drawparallels([0], labels=[1,0,0,0], fontsize=8, color='red', linewidth=1, dashes=[1,0])

    # Trópicos
    m.drawparallels([23.5, -23.5], labels=[1,0,0,0], fontsize=8, color='orange', linewidth=.5, dashes=[5,3])

    # Círculos Polares
    m.drawparallels([66.5, -66.5], labels=[1,0,0,0], fontsize=8, color='blue', linewidth=.5, dashes=[5,3])
    # fazer os tropicos de capricornio e cancer na cor verde
    #m.drawparallels(np.arange(-90, 91, 30), labels=[1,0,0,0], fontsize=8, color='green')

    lats = np.linspace(90, -90, 721)       # latitude decrescendo
    lons = np.linspace(-180, 180, 1440)       # longitude de -180 a 180
    
    lon2d, lat2d = np.meshgrid(lons, lats)
    # Plota os dados
    x, y = m(lon2d, lat2d)
    cs = m.contourf(x, y, data, levels=20, cmap='magma', extend='both')
    
    # Adiciona colorbar
    cbar = plt.colorbar(cs, orientation='horizontal', pad=0.05, shrink=0.8)
    cbar.set_label('Velocidade do Vento (m/s)', fontsize=10)
    
    # Título com informações
    plt.title(f'Vento - Frame {i}/{len(wind)}', fontsize=14, fontweight='bold')
    
    return plt







animator = AnimatePlot(
    space=list(range(128)),
    callplot=plot_wind,
    dpi=120
)

# 2. Verifica se há cache
cache_info = animator.get_cache_info()
if cache_info['exists']:
    print(f"Cache encontrado: {cache_info['count']} imagens")
    # Limpa cache antigo
    animator.delete_cache()

# 3. Renderiza novos frames
animator.render_cache(show_progress=True)

# 4. Gera outputs
animator.render_gif('output.gif', fps=15)
video_widget = animator.render_mp4('output.mp4', fps=15, use_opencv=False)

# 5. Se estiver no Jupyter, o vídeo será exibido automaticamente
if video_widget:
    display(video_widget)