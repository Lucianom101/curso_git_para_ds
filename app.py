import pandas as pd
import streamlit as st

def load_data():
    return pd.read_csv('Inicialização/3_Git_para_DS/7_Projeto/data/processed/bikes_completed.csv')

def main():
    df = load_data()

    st.dataframe(df)

if __name__ == '__main__':
    main()