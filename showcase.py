import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta



ticker_dict = {
    'ANTM.JK': "PT Aneka Tambang Tbk",
    'BMRI.JK': "PT Bank Mandiri (Persero) Tbk",
    'BBNI.JK': "PT Bank Negara Indonesia (Persero) Tbk",
    'PNBN.JK': "PT Bank Pan Indonesia Tbk",
    'ISAT.JK': "PT Indosat Tbk",
    'JSMR.JK': "PT Jasa Marga (Persero) Tbk",
    'LPGI.JK': "PT Lippo General Insurance Tbk",
    'FREN.JK': "PT Smartfren Telecom Tbk",
    'TLKM.JK': "PT Telekomunikasi Indonesia Tbk",
    'EXCL.JK': "PT XL Axiata Tbk",
    'GOOGL': "Google",
    'MSFT': "Microsoft",
    'AAPL': "Apple",
    'META' : "Facebook Meta"
    'META' : "Facebook Meta",
    'ANTM.JK': "PT Aneka Tambang Tbk"
    'ANTM.JK': "PT Aneka Tambang Tbk", 
    'MCD': "McDonald's Corporation"
}

st.write("""
# Aplikasi Yahoo Finance

## Data Saham Beberapa Perusahaan

""")

tickerSymbols = sorted(ticker_dict.keys())

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = tickerSymbols
)

st.write(f'Ticker Perusahaan: **{ticker_dict[ticker]}**')

tickerData = yf.Ticker(ticker)

hari_mundur = st.selectbox(
    "Pilihan Rentang Hari",
    options = [7, 10, 20, 30, 60, 90, 365] 
)

jumlah_hari = timedelta(days = -int(hari_mundur))

tgl_mulai = date.today() + jumlah_hari

tgl_akhir = st.date_input(
    "Hingga",
    value=date.today()
)

tickerDF = tickerData.history(
    period='1d',
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

attributes = st.multiselect(
    "Informasi yang ditampilkan:",
    options=['Open', 'High', 'Low', 'Close', 'Volume'],
    default=['Volume', 'Open']
)

st.markdown(f"Lima data pertama:")
st.write(tickerDF.head())

judul_chart = f'Harga Saham {ticker_dict[ticker]} ({ticker})'

st.plotly_chart(
    px.line(
        tickerDF,
        title=judul_chart,
        y = attributes
    )
)
