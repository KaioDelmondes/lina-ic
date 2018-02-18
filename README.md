# Aplicativo para Rotulação de Clusters #

### O que o software faz? ###

Software que, dado um certo número de grupos oriundos de algoritmos de aprendizagem de máquina não supervisionados, aplicar outros algoritmos baseados em aprendizagem supervisionada em cada grupo formado para detectar quais atributos – e seus respectivos valores ou faixas de valores – podem ser utilizados para defini-los. Em outras palavras, o método proposto busca apresentar um rótulo, capaz de definir um determinado grupo com base em suas características.

### Configuração do Ambiente de Desenvolvimento ###

Requisitos:

* Python 3.5
* pip
* virtualenv
* Flask

#### Instalar Python 3 ####

> apt install python3

#### Instalar pip ####

> apt install python3-pip

#### Instalar virtualenv ####

> pip3 install virtualenv

#### Criar o ambiente ####

Crie um diretório em um local de seu desejo para armazenar ambientes virtuais. Nele você irá criar uma ambiente virtual para este projeto:

> virtualenv lina-ic --python=python3

**lina-ic** será o nome do ambiente. Esse nome fica a sua escolha.

Você terá a seguinte estrutura de diretórios:

  ambientes-virtuais/
  |̣----lina-ic/
  |    |----bin/
  |    |----include/
  |    |----lib/
  |    |----share/

#### Ativar e Desativar o ambiente ####

Ativar:

> source ambientes-virtuais/lina-ic/bin/activate

Desativar:

> deactivate

#### Configuração no Windows ####

[Tutorial de Instalação do Python, pip e virtualenv](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/)