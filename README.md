# BRANCH TRAINING_BALL

Essa branch é utilizada para fazer o treinamento e validação do primeiro modelo do projeto.

---

## Estrutura do Projeto

├── data.yaml # Configuração do dataset para treinamento, validação e teste. 
├── dataset/ 
│ └── futevolei/ # Pasta com nome do projeto.
│   ├── images/ # Imagens do dataset 
│        ├── test/ # Imagens utilizadas para teste de 1 - 50
│        ├── train/ # Imagens utilizadas para treino de 1 - 200
│        ├── val/ # Imagens utilizadas para validação de 1 - 100
│   └── labels/ # Labels do dataset 
│        ├── test/ # Labels com as coordenadas do objeto nas imagens utilizadas no teste de 1 - 50
│        ├── train/ # Labels com as coordenadas do objeto nas imagens no treino de 1 - 200
│        ├── val/ # Labels com as coordenadas do objeto nas imagens na validação de 1 - 100
├── futvolei1n.pt # Melhor modelo do primeiro treinamento realizado com YOLO11n. (Sempre deve está na raiz do projeto para ser executado.)
├── run_model.py # Script principal para execução do modelo.
├── runs/ # Resultados de execuções
│ └── detect 
│   └── train
└── teste.mp4 # Vídeo de teste. (Não encontrado no repositório Github.)

---

## Executando treinamentos e testando modelos.

### Configurando Ambiente Virtual para execução de comandos (Dentro do Terminal).

1. Preparar ambiente virtual Python
```bash
python -m venv venv
```
2. Iniciando ambiente virtual
```bash
./venv/Scripts/activate
```
3. Instalar biblioteca Ultralytics
```bash
pip install ultralytics
```
4. Finalizando ambiente virtual
```bash
deactivate
```

### Executando treinamento de modelo (Dentro do Terminal).

```bash
yolo train model=futevolei1n.pt data=data.yaml imgsz=640 epochs=100 batch=2 device=cpu workers=2
```
2. Você pode saber mais sobre cada parametro dentro de "./data.yaml".

### Executando arquivo run_model.py

```bash
python './run_model.py'
```

---
