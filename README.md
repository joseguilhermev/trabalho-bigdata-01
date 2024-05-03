# Análise de Sentimento 🧐😮

Este repositório contém uma aplicação simples para realizar análise de sentimento em textos escritos em português. A aplicação utiliza a biblioteca Gradio para criar uma interface fácil de usar, permitindo que os usuários insiram texto em português e vejam o sentimento associado a ele.

## Funcionalidades

- **Análise de Sentimento**: A aplicação utiliza um modelo pré-treinado para realizar a análise de sentimento em textos. O modelo é capaz de determinar se o sentimento associado ao texto é positivo, negativo ou neutro, e também fornece um valor de confiança para a classificação.

- **Tradução Automática**: Antes de realizar a análise de sentimento, o texto inserido pelo usuário é automaticamente traduzido para o inglês utilizando a API do Google Translate. Isso garante que o modelo de análise de sentimento seja capaz de entender o texto independentemente do idioma original.

- **Caching de Resultados**: Para otimizar o desempenho e reduzir o tempo de processamento, os resultados da análise de sentimento são armazenados em um banco de dados Redis. Isso permite que resultados anteriores sejam recuperados rapidamente se o mesmo texto for inserido novamente.

### Instalação e Uso

Para testar esta solução, siga os passos abaixo:

1. Faça o clone do repositório:
    ```
    git clone https://github.com/joseguilhermev/trabalho-bigdata-01.git
    cd trabalho-bigdata-01
    ```

2. Instale as bibliotecas necessárias""
    ```
    pip install -r requirements.txt
    ```

3. Inicialize o servidor redis com docker
    ```
    docker compose up -d
    ```

2. Inicie a aplicação executando o seguinte código:
    ```
    python app.py
    ```

3. A aplicação estará disponível no navegador em: [http://localhost:7860](http://localhost:7860)

4. Insira um texto na caixa de texto fornecida e pressione o botão "Submit" para realizar uma análise de sentimento.

## Como Usar

Para iniciar a aplicação, execute o arquivo `app.py`. Isso iniciará a interface da aplicação no seu navegador padrão. Você pode então digitar o texto em português na caixa de texto fornecida e pressionar Enter para ver o resultado da análise de sentimento.

## Dependências

As seguintes bibliotecas são utilizadas neste projeto:

- [Gradio](https://gradio.app/): Biblioteca para criar interfaces de usuário simples para modelos de machine learning.
- [Transformers](https://huggingface.co/transformers/): Biblioteca para modelos de processamento de linguagem natural (NLP).
- [Redis](https://redis.io/): Banco de dados em memória utilizado para armazenar resultados em cache.
- [Deep Translator](https://github.com/nidhaloff/deep-translator): API de tradução automática para traduzir texto entre diferentes idiomas.
- [Torch](https://pytorch.org/): Biblioteca para aprendizado de máquina.

## Contribuição

Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request para este repositório.

Divirta-se analisando sentimentos! 🚀
