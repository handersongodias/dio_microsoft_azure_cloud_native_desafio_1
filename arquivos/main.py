import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv

load_dotenv()
BlobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
BlobContainerName = os.getenv("BLOB_CONTAINER_NAME")
BlobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQLServer = os.getenv("SQL_SERVER")
SQLDatabase = os.getenv("SQL_DATABASE")
SQLUser = os.getenv("SQL_USER")
SQLPassword = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_description = st.text_area("Descrição do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_image = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

#save image to blob storage
def save_image_to_blob(image_file):
    blob_service_client = BlobServiceClient.from_connection_string(BlobConnectionString)
    container_client = blob_service_client.get_container_client(BlobContainerName)
    blob_name = str(uuid.uuid4()) + image_file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(image_file.read(), overwrite=True)
    image_url = f"https://{BlobAccountName}.blob.core.windows.net/{BlobContainerName}/{blob_name}"
    return image_url

def insert_product_to_db(name, description, price, image_url):
    try:
        image_url = save_image_to_blob(product_image)
        connection = pymssql.connect(
            server=SQLServer,
            user=SQLUser,
            password=SQLPassword,
            database=SQLDatabase
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)",
            (name, description, price, image_url)
        )
        connection.commit()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
    finally:
        cursor.close()
        connection.close()
        
def get_list_of_products():
    try:
        connection = pymssql.connect(
            server=SQLServer,
            user=SQLUser,
            password=SQLPassword,
            database=SQLDatabase
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Produtos")
        products = cursor.fetchall()
        return products
    except Exception as e:
        st.error(f"Erro ao buscar produtos: {e}")
    finally:
        cursor.close()
        connection.close()  
def get_list_products_screen():
    products = get_list_of_products()
    if products:
        for product in products:
            st.markdown(f"Codigo do produto: {product[0]}")
            st.write(f"Nome do produto: {product[1]}")
            st.write(f"Descrição: {product[2]}")            
            st.image(product[4], width=150)
            st.write(f"Preço: {product[3]}")            
            st.markdown("---")
    else:
        st.write("Nenhum produto cadastrado.")

if st.button("Cadastrar"):
    insert_product_to_db(product_name, product_description, product_price, product_image)
    get_list_products_screen()
    

st.header("Produtos Cadastrados!")

if st.button("Listar Produtos"):
    get_list_products_screen()
