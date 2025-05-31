import sqlite3
import pandas as pd

csv_file = "Air_Quality.csv"  # Dosya adını kendi dosyanla değiştir
df = pd.read_csv(csv_file)

conn = sqlite3.connect("Air_Quality.db") # Aynı dosya adını .db uzantılı şekilde yaz

df.to_sql("a1_tablo", conn, if_exists="replace", index=False) #tablo_adi kısmı değiştirilebilir

conn.close()

