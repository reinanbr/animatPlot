
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from animateplot import AnimatePlot
from noawclg import get_noaa_data as gnd
from IPython.display import display
from time_ import generate_timestamps
from datetime import datetime

timestamps = generate_timestamps(quantity=128, interval_hours=3, start_date=datetime(2025, 10, 19, 0, 0, 0))

data_noaa = gnd(date='19/10/2025')
wind = data_noaa['ugrdmwl'].to_numpy()

def plot_wind(i, plt):
    data = wind[i]

    plt.figure(figsize=(14, 10), facecolor='black')

    # Cria o mapa
    m = Basemap(
        projection='ortho',
        resolution='l',
        lat_0=-9, lon_0=-40
    )
    
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.3)
    m.fillcontinents(color='lightgray', lake_color='white')
    m.drawmapboundary(fill_color='white')
    
    # Meridianos sem labels
    m.drawmeridians(np.arange(-180, 181, 60), linewidth=0.5, color='gray', alpha=0.5)
    
    

    # Linhas importantes SEM labels
    # Equador
    m.drawparallels([0], linewidth=2, color='red', dashes=[1,0])
    
    # Trópicos
    m.drawparallels([23.5, -23.5], linewidth=.5, color='orange', dashes=[5,3])
    
    # Círculos Polares
    m.drawparallels([66.5, -66.5], linewidth=.5, color='blue', dashes=[5,3])
    
    # Paralelos adicionais
    m.drawparallels(np.arange(-90, 91, 30), linewidth=0.1, color='gray', alpha=0.5)
    
    lats = np.linspace(90, -90, 721)
    lons = np.linspace(-180, 180, 1440)
    
    lon2d, lat2d = np.meshgrid(lons, lats)
    x, y = m(lon2d, lat2d)
    
    # Define os limites fixos baseados em todos os dados
    vmin = wind.min()
    vmax = wind.max()

    

    cs_ = m.contourf(x, y, wind[0], levels=20, cmap='magma', extend='both', 
                    vmin=vmin, vmax=vmax)
    cs = m.contourf(x, y, data, levels=20, cmap='magma', extend='both', 
                    vmin=vmin, vmax=vmax)
    # Colorbar menor e mais compacta
    cbar = plt.colorbar(cs_, orientation='horizontal', pad=0.03, shrink=0.5, aspect=30)
    cbar.set_label('Velocidade do Vento (m/s)', fontsize=9, color='white')
    cbar.ax.tick_params(labelsize=8, colors='white')

    plt.title(f'Jatos de Vento \n {timestamps[i].strftime("%d %B %Y %H:%M")}', fontsize=14, fontweight='bold', color='white')

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
animator.render_gif('output_ortho.gif', fps=15)
video_widget = animator.render_mp4('output_ortho.mp4', fps=15, use_opencv=False)

# 5. Se estiver no Jupyter, o vídeo será exibido automaticamente
if video_widget:
    display(video_widget)