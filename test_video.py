"""
Exemplo completo de uso do AnimatePlot
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from animateplot import AnimatePlot
from noawclg import get_noaa_data as gnd
from IPython.display import display

data_noaa = gnd(date='17/10/2025')
wind = data_noaa['tmpmwl'].to_numpy() # Supondo que wind_speed é uma lista de arrays 2D
# ============================================================
# Exemplo 1: Animação simples de gráfico
# ============================================================

def plot_sine_wave(i,plt):
    """Plota uma onda senoidal animada"""
    x = np.linspace(0, 4*np.pi, 200)
    y = np.sin(x - i/10)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.grid(True, alpha=0.3)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Onda Senoidal - Frame {i}')
    return plt

# Cria a animação
frames = list(range(100))
animator = AnimatePlot(space=frames, callplot=plot_sine_wave, dpi=100)

# Renderiza os frames
animator.render_cache(show_progress=True, clear_previous=True)

# Gera GIF
animator.render_gif('sine_wave.gif', fps=20)

# Gera MP4 (rápido com OpenCV)
animator.render_mp4('sine_wave.mp4', fps=20, use_opencv=True)

# Informações do cache
print(animator)


# ============================================================
# Exemplo 2: Seu caso com dados de vento
# ============================================================

def plot_wind(i,plt):
    """
    Plota dados de vento para o frame i
    Assume que 'wind', 'lons', 'lats' estão definidos globalmente
    """
    data = wind[i]
    
    plt.figure(figsize=(14, 8))
    
    # Cria o mapa
    m = Basemap(
        projection='cyl',
        resolution='l',
        llcrnrlat=-90, urcrnrlat=90,
        llcrnrlon=0, urcrnrlon=360
    )
    
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.3)
    m.fillcontinents(color='lightgray', lake_color='white')
    m.drawmapboundary(fill_color='white')
    
    
    lats = np.linspace(90, -90, 721)       # latitude decrescendo
    lons = np.linspace(0, 360, 1440)       # longitude de 0 a 360
    
    lon2d, lat2d = np.meshgrid(lons, lats)
    # Plota os dados
    x, y = m(lon2d, lat2d)
    cs = m.contourf(x, y, data, levels=20, cmap='RdYlBu_r', extend='both')
    
    # Adiciona colorbar
    cbar = plt.colorbar(cs, orientation='horizontal', pad=0.05, shrink=0.8)
    cbar.set_label('Velocidade do Vento (m/s)', fontsize=10)
    
    # Título com informações
    plt.title(f'Vento - Frame {i}/{len(wind)}', fontsize=14, fontweight='bold')
    
    return plt


# Uso do AnimatePlot
num_frames = len(wind)
animator = AnimatePlot(
    space=list(range(num_frames)),
    callplot=plot_wind,
    dpi=150  # Alta resolução
)

# Renderiza frames (mostra progresso)
animator.render_cache(show_progress=True)

# Opção 1: GIF (menor tamanho, pode perder qualidade)
animator.render_gif('wind_animation.gif', fps=10)

# Opção 2: MP4 com OpenCV (rápido, boa qualidade)
animator.render_mp4('wind_animation.mp4', fps=10, use_opencv=True)

# Opção 3: MP4 com MoviePy (lento, melhor qualidade)
animator.render_mp4('wind_animation_hq.mp4', fps=10, use_opencv=False)

# Verifica informações do cache
cache_info = animator.get_cache_info()
print(f"\nCache: {cache_info['count']} imagens, {cache_info['size_mb']:.2f} MB")


# ============================================================
# Exemplo 3: Workflow completo com limpeza
# ============================================================

# 1. Configuração inicial
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
video_widget = animator.render_mp4('output.mp4', fps=15)

# 5. Se estiver no Jupyter, o vídeo será exibido automaticamente
if video_widget:
    display(video_widget)

# 6. Limpa cache após gerar outputs (opcional)
# animator.delete_cache()


# ============================================================
# Exemplo 4: Tratamento de erros
# ============================================================

try:
    animator = AnimatePlot(
        space=list(range(100)),
        callplot=plot_wind,
        dpi=100
    )
    
    # Renderiza com tratamento de erros
    animator.render_cache(show_progress=True, clear_previous=False)
    
    # Tenta gerar os outputs
    animator.render_gif('animation.gif', fps=10)
    animator.render_mp4('animation.mp4', fps=10, use_opencv=True)
    
    print("\n✓ Animação criada com sucesso!")
    
except ValueError as e:
    print(f"Erro de valor: {e}")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    # Limpeza opcional
    # animator.delete_cache()
    pass


# ============================================================
# Dicas de otimização
# ============================================================

"""
Performance Tips:

1. DPI: Use 100-150 para boa qualidade. 300+ é muito pesado.

2. Formato de saída:
   - GIF: Bom para web, tamanho menor, menos qualidade
   - MP4 OpenCV: Rápido, boa qualidade, tamanho médio (RECOMENDADO)
   - MP4 MoviePy: Lento, melhor qualidade, tamanho otimizado

3. Cache:
   - Use clear_previous=False para reusar frames
   - Limpe o cache regularmente para economizar espaço

4. FPS:
   - 10-15 fps: Bom para visualizações científicas
   - 20-30 fps: Suave para apresentações
   - 60+ fps: Desnecessário para plots estáticos

5. Resolução da figura:
   - figsize=(10, 6) para web
   - figsize=(14, 8) para apresentações
   - figsize=(20, 12) para posters
"""