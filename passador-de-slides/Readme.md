# Passador de Slides com Mãos

Este projeto permite controlar uma apresentação de slides utilizando gestos das mãos, por meio de visão computacional. Ele utiliza ferramentas como **OpenCV** para processamento de imagem, **Cvzone** para facilitar a manipulação de gestos, **MediaPipe** para detecção e rastreamento das mãos, e **Pynput** para simular interações com o teclado ou mouse.

## Funcionalidades

- **Detecção de gestos** para navegação entre os slides.
- **Avançar e retroceder** slides com movimentos das mãos.
- **Interface interativa** utilizando visão computacional.

## Configuração do Ambiente

1. **Instalação do Python e PIP**:
   - Verifique se o Python está instalado em seu sistema.
   - Instale o PIP: `sudo apt-get install pip` (para Ubuntu).

2. **Instalação das dependências**:
   - **NumPy**: `pip install numpy`
   - **Matplotlib**: `pip install matplotlib`
   - **SciPy**: `pip install scipy`
   - **OpenCV**: `pip install opencv-python`
   - **Cvzone**: `pip install cvzone`
   - **MediaPipe**: `pip install mediapipe`
   - **Pynput**: `pip install pynput`

## Requisitos

- Python 3.x
- Sistema operacional compatível com os pacotes necessários (Linux, Windows, macOS).

## Como Executar

1. Após instalar as dependências, execute o script principal.
2. O sistema começará a rastrear os gestos das suas mãos e controlar os slides conforme o movimento.

---

Esse projeto oferece uma maneira interativa e moderna de controlar apresentações usando apenas gestos, aproveitando o poder da visão computacional.
