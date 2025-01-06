# ETL de Múltiplos Arquivos com Saída em Parquet ou CSV

Este projeto é um exemplo de um pipeline ETL para processar múltiplos arquivos `*.json`. O pipeline utiliza as bibliotecas **Pandas** para processamento de dados e **Pandera** para validação e garantia de qualidade dos dados. Ao final do processamento, o usuário pode escolher o formato de saída: **Parquet** ou **CSV**.

## Estrutura do Projeto

```
.
├── data/                # Diretório para armazenar os arquivos de entrada
├── output/              # Diretório para armazenar os arquivos de saída
├── etl.py               # Script principal do pipeline ETL
├── pipeline.py          # Arquivo execução da etl
├── README.md            # Documentação do projeto
```

## Requisitos

- Python 3.11 ou superior
- Poetry para gerenciar pacotes

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/jonhnatta/exemplo-etl-multiplos-arquivos.git
   cd exemplo-etl-multiplos-arquivos
   ```

2. Instale as dependências:
   ```bash
   poetry shell
   poetry install
   ```

## Configuração do Ambiente

Coloque os arquivos de entrada no diretório `data/`. Certifique-se de que os arquivos estejam em um formato `JSON`.

## Uso

Atualize a variável output_format do arquivo `pipeline.py` para definir os formatos de saída desejados. Por exemplo:
```bash
output_format: list = ["parquet", "csv"]  #Saída parquet e csv
output_format: list = ["parquet"]  #Saída parquet
output_format: list = ["csv"]  #Saída csv
```

Execute o script principal:
```bash
poetry run python pipeline.py
```

O script:
1. Lê os arquivos do diretório `data/`.
2. Processa e valida os dados usando **Pandas** e **Pandera**.
3. Salva os dados processados no formato escolhido pelo usuário: **Parquet** ou **CSV**.


## Tecnologias Utilizadas

- **Pandas**: Utilizado para processamento de dados, incluindo limpeza, transformação e agregação.
- **Pandera**: Utilizado para validação de schemas e garantia de qualidade dos dados.

