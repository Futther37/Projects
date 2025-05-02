import streamlit as st
from password import RandomPasswordGenerator, PinCodeGenerator, MemorablePasswordGenerator

st.set_page_config(page_title="Password Generator Dashboard", page_icon="🔐")
st.title("🔐 Password Generator Dashboard")
st.write("Vítejte! Vyberte typ hesla, který chcete vygenerovat a přizpůsobte si jeho parametry.")

# Výběr typu generátoru
generator_type = st.sidebar.radio("Vyber typ generátoru:", 
                                   ["Náhodné heslo", "Zapamatovatelné heslo", "PIN kód"])

if generator_type == "Náhodné heslo":
    st.header("🔑 Náhodné heslo")
    length = st.slider("Délka hesla", min_value=4, max_value=32, value=12)
    include_numbers = st.checkbox("Zahrnout čísla", value=True)
    include_symbols = st.checkbox("Zahrnout symboly", value=True)
    
    if st.button("Generovat heslo"):
        generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
        password = generator.generate()
        st.success(f"Vygenerované heslo: `{password}`")

elif generator_type == "Zapamatovatelné heslo":
    st.header("🧠 Zapamatovatelné heslo")
    num_words = st.slider("Počet slov", min_value=2, max_value=10, value=4)
    separator = st.text_input("Oddělovač mezi slovy", value="-")
    capitalize = st.checkbox("První písmeno velké", value=True)

    if st.button("Generovat heslo"):
        generator = MemorablePasswordGenerator(num_words, separator, capitalize)
        password = generator.generate()
        st.success(f"Vygenerované heslo: `{password}`")

elif generator_type == "PIN kód":
    st.header("🔢 PIN kód")
    length = st.slider("Délka PINu", min_value=4, max_value=12, value=4)
    
    if st.button("Generovat PIN"):
        generator = PinCodeGenerator(length)
        pin = generator.generate()
        st.success(f"Vygenerovaný PIN: `{pin}`")