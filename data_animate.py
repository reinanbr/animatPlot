import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from animateplot import AnimatePlot
from datetime import datetime, timedelta

class DataAnimator:
    def __init__(self, wind, start_date=datetime(2025, 10, 19, 0, 0, 0), quantity=128, interval_hours=3):
        self.wind = wind
        self.start_date = start_date
        self.quantity = quantity
        self.interval_hours = interval_hours
        
        # Inicialização modular
        self.timestamps = self._setup_timestamps()
        self.fig = self._setup_figure()
        self.map = self._setup_basemap()
        self.lats, self.lons = self._setup_coordinates()
        self.lon2d, self.lat2d = self._setup_meshgrid()
        self.x, self.y = self._setup_projection()
        self.vmin, self.vmax = self._setup_colorscale()
        self._draw_map_features()
        self.mesh = self._setup_initial_contour()
        self.cbar = self._setup_colorbar()
        self.title = self._setup_title()
    
    def _setup_timestamps(self):
        """Gera lista de timestamps baseada na data inicial, quantidade e intervalo."""
        timestamps = []
        for i in range(self.quantity):
            timestamps.append(self.start_date + timedelta(hours=self.interval_hours * i))
        return timestamps
    
    def _setup_figure(self):
        """Configura a figura matplotlib."""
        return plt.figure(figsize=(14, 10), facecolor='black')
    
    def _setup_basemap(self):
        """Configura o mapa base com projeção ortográfica."""
        return Basemap(projection='ortho', resolution='l', lat_0=-9, lon_0=-40)
    
    def _setup_coordinates(self):
        """Define arrays de latitudes e longitudes."""
        lats = np.linspace(90, -90, 721)
        lons = np.linspace(-180, 180, 1440)
        return lats, lons
    
    def _setup_meshgrid(self):
        """Cria malha 2D de coordenadas."""
        return np.meshgrid(self.lons, self.lats)
    
    def _setup_projection(self):
        """Projeta coordenadas geográficas para coordenadas do mapa."""
        return self.map(self.lon2d, self.lat2d)
    
    def _setup_colorscale(self):
        """Define limites mínimo e máximo para escala de cores."""
        return self.wind.min(), self.wind.max()
    
    def _draw_map_features(self):
        """Desenha características geográficas no mapa."""
        m = self.map
        m.drawcoastlines(linewidth=0.5)
        m.drawcountries(linewidth=0.3)
        m.fillcontinents(color='lightgray', lake_color='white')
        m.drawmapboundary(fill_color='white')
        m.drawmeridians(np.arange(-180, 181, 60), linewidth=0.5, color='gray', alpha=0.5)
        m.drawparallels([0], linewidth=2, color='red', dashes=[1,0])
        m.drawparallels([23.5, -23.5], linewidth=.5, color='orange', dashes=[5,3])
        m.drawparallels([66.5, -66.5], linewidth=.5, color='blue', dashes=[5,3])
        m.drawparallels(np.arange(-90, 91, 30), linewidth=0.1, color='gray', alpha=0.5)
    
    def _setup_initial_contour(self):
        """Cria o contorno inicial com os primeiros dados."""
        return self.map.contourf(
            self.x, self.y, self.wind[0],
            shading='auto', cmap='magma',
            vmin=self.vmin, vmax=self.vmax
        )
    
    def _setup_colorbar(self):
        """Configura a barra de cores."""
        cbar = plt.colorbar(
            self.mesh,
            orientation='horizontal',
            pad=0.03,
            shrink=0.5,
            aspect=30
        )
        cbar.set_label('Wind Speed (m/s)', fontsize=9, color='white')
        cbar.ax.tick_params(labelsize=8, colors='white')
        return cbar
    
    def _setup_title(self):
        """Configura o título inicial do gráfico."""
        return plt.title('', fontsize=14, fontweight='bold', color='white')
    
    def _plot_frame(self, i, mesh):
        """Atualiza o frame da animação."""
        self.mesh = self.map.contourf(
            self.x, self.y, self.wind[i],
            shading='auto', cmap='magma',
            vmin=self.vmin, vmax=self.vmax
        )
        self.title.set_text(f'Jet Streams\n{self.timestamps[i].strftime("%d %B %Y %H:%M")}')
        return plt
    
    def render_gif(self, path='wind.gif', dpi=120):
        """Renderiza animação como GIF."""
        animator = AnimatePlot(
            space=list(range(len(self.timestamps))),
            callplot=self._plot_frame,
            dpi=dpi,
            clf=False
        )
        animator.render_cache()
        animator.render_gif(path)
    
    def render_video(self, path='wind.mp4', dpi=120, fps=24):
        """Renderiza animação como vídeo MP4."""
        animator = AnimatePlot(
            space=list(range(len(self.timestamps))),
            callplot=self._plot_frame,
            dpi=dpi,
            clf=False
        )
        animator.render_cache()
        animator.render_video(path, fps=fps)