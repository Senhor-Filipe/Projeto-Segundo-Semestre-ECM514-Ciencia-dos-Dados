import streamlit as st
import plotly.express as px
from rotulos import calcular_similaridade

# Título do app
st.title("Sistema de Sugestão de Rótulos com Similaridade")

# Entrada para o nome da página
new_page_title = st.text_input("Digite o título da página da Wikipédia:")

# Botão para gerar resultado
if st.button("Obter Rótulo e Similaridade"):
    if new_page_title:
        suggested_label, suggested_similarity, top_data = calcular_similaridade(new_page_title)

        if suggested_label:
            # Exibir o rótulo e similaridade
            st.write(f"**Sugestão de rótulo:** {suggested_label}")
            st.write(f"**Similaridade com o rótulo sugerido:** {suggested_similarity:.2f}")

            # Gráfico de similaridade
            top_labels, top_similarities = top_data
            colors = ['#636EFA' if label != suggested_label else '#EF553B' for label in top_labels]

            fig = px.bar(
                x=top_labels,
                y=top_similarities,
                labels={'x': 'Rótulos', 'y': 'Similaridade'},
                title=f'Similaridade entre o Texto e os Rótulos (Texto: {new_page_title})',
                color_discrete_sequence=colors
            )
            fig.update_layout(
                xaxis=dict(title='Rótulos', tickangle=45),
                yaxis=dict(title='Similaridade'),
                showlegend=False
            )

            st.plotly_chart(fig)
        else:
            st.error("Não foi possível recuperar o conteúdo da página da Wikipédia.")
    else:
        st.error("Por favor, insira um título de página válido.")
