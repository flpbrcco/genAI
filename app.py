"""docstring"""

import streamlit as st
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError


def main() -> None:
    """docstring"""
    st.title("Sistema de CRM e Vendas da ZapFlow - FrontEnd Simples")
    email = st.text_input("E-mail do vendedor:")
    data = st.date_input("Data da venda:", datetime.now())
    # Valor padrão: data de agora.
    hora = st.time_input("Hora da venda:", value=time(9, 0))
    # Valor padrão: 9h
    valor = st.number_input("Valor da venda:", min_value=0.0, format="%.2f")
    quantidade = st.number_input(
        "Quantidade de produtos vendidos:", min_value=1, step=1
    )
    produto = st.selectbox(
        "Favor selecionar o produto:",
        ["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"],
    )

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto,
            )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")


if __name__ == "__main__":
    main()
