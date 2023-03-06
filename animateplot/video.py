import cv2
import os



class RenderVideo:
    __dir_pattern_imgs = '.data'
    
    
    def __init__(self,dir:str) -> None:
        if os.path.isdir(dir):
            self.__dir_pattern_imgs = dir
        else:
            Exception()
# Definir o caminho para a pasta de fotos
diretorio = 'caminho/para/sua/pasta/de/fotos'

# Definir a taxa de quadros do vídeo
fps = 30

# Obter a lista de nomes de arquivo PNG na pasta
arquivos_png = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.png')]

# Classificar a lista em ordem alfabética
arquivos_png.sort()

# Obter o primeiro arquivo PNG para obter a largura e altura da imagem
primeiro_arquivo = cv2.imread(os.path.join(diretorio, arquivos_png[0]))
altura, largura, _ = primeiro_arquivo.shape

# Criar um objeto VideoWriter para escrever o vídeo
video = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (largura, altura))

# Loop pelos arquivos PNG e adicionar cada quadro ao vídeo
for arquivo in arquivos_png:
    caminho_completo = os.path.join(diretorio, arquivo)
    imagem = cv2.imread(caminho_completo)
    video.write(imagem)

# Liberar o objeto VideoWriter e fechar o vídeo
video.release()
cv2.destroyAllWindows()