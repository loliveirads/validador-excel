from src.contrato import Vendas
import pytest
from datetime import datetime
from pydantic import ValidationError  # Certifique-se de que ValidationError está sendo usado corretamente

def test_vendas_com_dados_validos():
    dados_validos = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria3",
    }

    # Criar uma instância de Vendas com dados válidos
    venda = Vendas(**dados_validos)

    # Verificar se os atributos da instância correspondem aos valores fornecidos
    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]

def test_vendas_com_dados_invalidos():
    # Exemplo de dados inválidos
    dados_invalidos = {
        "email": "email_invalido",  # Exemplo de e-mail inválido
        "data": "data_invalida",   # Exemplo de data inválida
        "valor": -10.00,           # Valor inválido
        "produto": "",             # Produto vazio
        "quantidade": -1,          # Quantidade inválida
        "categoria": None          # Categoria nula
    }

    # Verificar se a criação de uma instância com dados inválidos levanta um ValidationError
    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)


# Teste de validação de categoria
def test_validacao_categoria():
    dados = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria inexistente",
    }
