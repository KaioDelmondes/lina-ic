inputs = {
  'discretizacao' : {
    'name' : 'alg_disc',
    'label' : 'Algoritmo de Discretização',
    'inputs' : [
      {
        'label' : 'Variação V (%)',
        'type' : 'range',
        'name' : 'varv',
        'value' : 10,
        'max' : 20,
        'min' : 1,
        'help' : 'A variação V expressa em porcentagem (%), é utilizada para eliminar a possível ambiguidade entre clusters selecionando todos os atributos que possuem até um diferença V em relação ao atributo com maior taxa de acerto e descartar os demais.',
      },
      {
        'label' : 'Nº de faixas',
        'type' : 'range',
        'name' : 'faixas',
        'value' : 3,
        'max' : 10,
        'min' : 1,
        'help' : 'Número de faixas de valores para discretização. Este valor representa a quantidade de valores discretos que um atributo pode assumir.',
      },
    ],
    'options' : [
      {
        'name' : 'EWD - Equals Width Discretization',
        'value' : 'EWD',
      },
      {
        'name' : 'EFD - Equals Frequency Discretization',
        'value' : 'EFD',
      },
    ],
  },
  'classificacao' : {
    'name' : 'alg_clas',
    'label' : 'Algoritmo de Classificação',
    'inputs' : [
      {
        'label' : '% de dados para treino',
        'type' : 'range',
        'name' : 'treino',
        'value' : 60,
        'max' : 80,
        'min' : 40,
        'help' : 'Percentagem de elementos da base de dados que servirão de entrada para a fase de treinamento do modelo proposto.',
      },
    ],
    'options' : [
      {
        'name' : 'MultiLayer Perceptron',
        'value' : 'MLP',
      },
      {
        'name' : 'Decision Tree',
        'value' : 'tree',
      },
    ],
  },
}