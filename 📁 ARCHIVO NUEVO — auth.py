import streamlit as st
import hashlib

# USUARIOS (usuario: password)
USERS = {
    "admin": "admin123",
    "usuario1": "clave123"
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

HASHED_USERS = {u: hash_password(p) for u, p in USERS.items()}

def login():
    st.title("🔐 Iniciar Sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if username in HASHED_USERS and hash_password(password) == HASHED_USERS[username]:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Acceso concedido")
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

def logout():
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.clear()
        st.rerun()
