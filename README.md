Título do projeto: Corona Run
Membros do grupo: Luca Coutinho Melão, Thiago de Donato Youssef e Vitor Fortes Giuliano Riccetti
Endereço do vídeo do jogo: (adicionar futuramente)

Descrição do projeto: o projeto consiste no desenvolvimento de um jogo interativo de computador em Python 3 utilizando os recursos da biblioteca PyGame e os conteúdos aprendidos ao longo do primeiro semestre de 2020 por nós, alunos do Insper, no curso "Design de Software". Nosso grupo optou pelo desenvolvimento de um programa que permite a interação com um usuário (jogador), inspirado no "T-Rex Game" do Google Chrome, porém, acrescentando funcionalidades extras e novos elementos no jogo. 

As referências utilizadas por nós para a elaboração do projeto podem ser encontradas no arquivo "referencias.txt" deste repositório.

Como instalar as dependências: para a elaboração do jogo foram utilizads os recursos da biblioteca "PyGame", sendo assim, se você ainda não possuí-la em seu computador, é necessária a instalação para que seja possível a execução do código, as instruções são descritas abaixo:

Para instalação em Windows e Linux:
Abra o seu terminal (Linux) ou Anaconda Prompt (Windows) e digite:
pip install pygame

Para instalação em Mac OSX:
Se você não tiver o Homebrew instalado, instale-o seguindo as instruções disponíveis neste link: https://brew.sh/
Abra o terminal e digite:
brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf
brew install Caskroom/cask/xquartz
git clone -b 1.9.6 --single-branch https://github.com/pygame/pygame.git
cd pygame
python setup.py -config -auto -sdl2
python setup.py install
cd ..
rm -rf pygame

Documentação com mais detalhes e opções de instalação no Mac para consulta: https://www.pygame.org/wiki/MacCompile

Como executar o programa: após realizar a instalação da biblioteca adicinal necessária, é necessário que este repositório do GitHub seja clonado em seu computador. Depois disso, abra-o o com o interpretador que desejar, como o Visual Studio Code por exemplo, e execute ocódigo a partir do arquivo "main.py".

Divirta-se!