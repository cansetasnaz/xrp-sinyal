import streamlit as st
import requests

def get_xrp_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["ripple"]["usd"]

st.title("XRP Alım/Satım Sinyali")

price = get_xrp_price()
st.write(f"Anlık XRP fiyatı: ${price:.4f}")

if price < 0.5:
    st.success("Sinyal: AL")
elif price > 1.5:
    st.error("Sinyal: SAT")
else:
    st.info("Sinyal: BEKLE")

st.write("Bu sinyal sadece örnek amaçlıdır, yatırım tavsiyesi değildir.")
