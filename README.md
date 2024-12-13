# Projeto-Segundo-Semestre-ECM514-Ciencia-dos-Dados

Este repositório contém arquivos do Projeto Semestral de ECM514 - Ciência dos Dados para o segundo semestre de 2024.


Alunos:

Marcel Marques Caceres - RA 17.00648-0

Kaique de Andrade Almeida - RA 17.01113-2

Filipe dos Santos Pugliesi - RA 18.02608-7

Johannes Mattheus Krouwel - RA 20.01248-9


Link para o vídeo da apresentação disponível no YouTube:  
https://youtu.be/oPtiWn8m9Jo


Observações sobre os arquivos desse repositório:

Os arquivos "Projeto_Semestral_Segundo_Semestre_ECM514_Ciência_dos_Dados_API_Wikipédia.ipynb" 
(arquivo Colab) e "projeto_semestral_segundo_semestre_ecm514_ciencia_dos_dados_api_wikipedia.py" 
possuem códigos completos para realizar a comunicação com o dropbox, extrair textos da Wikipédia
e realizar o aprendizado de máquina (treinar o modelo). Após esse processo é gerado o arquivo de
parâmetros "embeddings.pkl". E por fim, disponibilizam também o teste do programa.

Sendo assim, se um usuário deseja criar e treinar seu próprio modelo, ele usará o código todo.
Mas se o usuário deseja somente testar o modelo criado para este trabalho, basta fazer download
do arquivo "embeddings.pkl" para o computador e depois adicionar ao Colab conforme está explicado
no código dos dois primeiros arquivos citados no parágrafo anterior. Para esse teste é suficiente
a execução das três últimas células do arquivo Colab.

Os arquivos "rotulos.py" e "app.py" são a programação para o Streamlit App. Para o usuário executar, 
ele deve fazer download deles e do arquivo "embeddings.pkl" e digitar os comandos a seguir no terminal:

pip install torch transformers sklearn plotly streamlit (para download de bibliotecas)

streamlit run app.py (para execução).







