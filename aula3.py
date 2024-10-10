import streamlit as st
import random

# 1. Criar um número secreto e inicializar tentativas
if 'número_secreto' not in st.session_state:
    st.session_state.número_secreto = random.randint(1, 100)
    st.session_state.tentativas = 0  # Inicializa o contador de tentativas
    st.session_state.chances = 4  # Define o número de chances
    st.session_state.acertou = False  # Flag para verificar se o usuário acertou
st.write(st.session_state.número_secreto)
# 2. Título na aplicação
st.title("=== Jogo: Descubra o Número Secreto ===")

# 3. Dar uma mensagem de boas-vindas
st.write("Bem-vindo ao jogo! Tente adivinhar o número secreto entre 1 e 100.")
st.write(f"Você tem {st.session_state.chances} chances para adivinhar.")

# 4. Receber o chute do usuário
chute = st.number_input("Digite seu palpite:", min_value=1, max_value=100)

if st.button("Enviar"):
    # Aumenta o contador de tentativas
    st.session_state.tentativas += 1
    st.session_state.chances -= 1  # Decrementa o número de chances

    # 6. Verificar o chute com o número secreto
    if chute < st.session_state.número_secreto:
        st.write("Muito baixo! Tente novamente.")
    elif chute > st.session_state.número_secreto:
        st.write("Muito alto! Tente novamente.")
    else:
        # 7. Mostrar uma mensagem personalizada e indicar que acertou
        st.write(f"Parabéns! Você acertou o número secreto: {st.session_state.número_secreto}")
        st.session_state.acertou = True  # Marca que o usuário acertou

    # Verifica se o número de chances atingiu o limite
    if st.session_state.chances <= 0:
        st.write("Você atingiu o limite de tentativas. A sessão será encerrada.")
        st.session_state.clear()  # Limpa todas as variáveis do estado da sessão
    else:
        st.write(f"Você ainda tem {st.session_state.chances} chances restantes.")

    # Opção para reiniciar o jogo
    if st.button("Reiniciar o jogo"):
        st.session_state.número_secreto = random.randint(1, 100)
        st.session_state.tentativas = 0  # Reinicia o contador de tentativas
        st.session_state.chances = 4  # Reinicia o número de chances
        st.session_state.acertou = False  # Reinicia a flag
        st.write("O jogo foi reiniciado. Tente adivinhar novamente!")

# Botão para reiniciar após acerto
if st.session_state.acertou:
    if st.button("Jogar Novamente"):
        st.session_state.número_secreto = random.randint(1, 100)
        st.session_state.tentativas = 0  # Reinicia o contador de tentativas
        st.session_state.chances = 4  # Reinicia o número de chances
        st.session_state.acertou = False  # Reinicia a flag
        st.write("O jogo foi reiniciado. Tente adivinhar novamente!")

# Opção para encerrar a sessão
if st.button("Encerrar Sessão"):
    st.session_state.clear()  # Limpa todas as variáveis do estado da sessão
    st.write("A sessão foi encerrada. Você pode recarregar a página para jogar novamente.")
