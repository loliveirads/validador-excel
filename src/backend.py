import pandas as pd
from contrato import Vendas
import os

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        erros = []
        # Verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            erros.append(f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}")

        # Validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha {index + 2}: {e}")

        # Se houver erros, retorne-os, caso contrário, sucesso
        if erros:
            return None, erros
        return "Validação bem-sucedida", None

    except Exception as e:
        # Em caso de exceção, retorne o erro
        return None, [f"Erro inesperado: {str(e)}"]


