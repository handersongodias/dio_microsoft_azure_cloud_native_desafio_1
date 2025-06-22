# Desafio DIO com Microsoft Azure Cloud Native
# Formulario de cadastro e listar produtos , utilizando o Python Streamlit + Azure Blob Storage + Azure SQL Server

Este projeto foi desenvolvido com **Streamlit**, que permite cadastrar produtos com **nome**, **preço**, **descrição** e **imagem**. Os dados são salvos em um banco de dado na Azure **SQL Server** e as imagens são armazenadas no **Azure Blob Storage**.

---

## 🚀 Funcionalidades

-  Cadastro dos dados com upload de imagem para o Azure Blob Storage e SQLServer

-  Exibição dos produtos cadastrados com codigo do produto , nome, descrição, preço e imagem
  

---

## 🧰 Tecnologias e Bibliotecas

- Visual Studio Code
- Python 3.12
- Streamlit
- Azure Storage Blob SDK
- Python Dotenv
- PyMSSQL
- UUID
- SQL Server

---

## 📦 Instalação

### 1. Crie uma pasta local que sera utilizada no visual code
### 2. Crie os arquivos .env, infos.txt, main.py, requirements.txt
    .env -> as variaveis de ambiente e configuração
    infos.txt -> o script de criação da Tabela
    main.py -> script python que cria o formulario e os comando de cadastro e listar
    requirements.txt -> script com as bibliotecas necessarias para execução do codigo python e scripts do banco de dados
    
### 3. Instale as bibliotecas
    no terminal, execute o seguinte comando:
      pip install -r requirements.txt
      
### 4. Execute o projeto
     streamlit run .\main.py 
     ou
     python -m streamlit run .\main.py



## 📸 Telas da aplicação e configuração do Azure 
      na pasta arquivos/imagens

