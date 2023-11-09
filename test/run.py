import subprocess
import os
import time
import pandas as pd

directory = "dane"
tim=[]
names=[]
val=[]
n=[]
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Pełna ścieżka do pliku .exe
        exe_path = "148240.exe"
        # Pełna ścieżka do aktualnego pliku .txt
        txt_path = filename
        txt_path = os.path.join(directory, filename)
        # Uruchomienie pliku .exe z plikiem .txt jako argumentem
        start_time = time.time()
        result = subprocess.run([exe_path, txt_path], capture_output=True, text=True)
        duration_ms = (time.time() - start_time) * 1000  # Konwersja czasu trwania na milisekundy
        rounded_duration_ms = round(duration_ms, 2)

        if result.returncode != 0:
            print(f"Error for {filename}:\n{result.stderr}")

        pom = txt_path.split('_')
        with open("out_"+pom[1]+"_148240_"+pom[2], 'r', encoding='utf-8') as plik:
            # Wczytanie pierwszej linijki z pliku
            linijka = plik.readline()
            # Wypisanie linijki
            print(pom[1] + pom[2].replace(".txt","") , linijka, duration_ms)
            tim.append(rounded_duration_ms)
            names.append(pom[1])
            n.append(pom[2].replace(".txt",""))
            val.append(linijka)
# Informacja o zakończeniu procesu
print("Done processing all .txt files.")
df = pd.DataFrame({'Czas wykonania (ms)': tim,
                   'Wartosc' :val,
                   'Indeks' :names,
                   'n':n})


# Zapisanie DataFrame do pliku Excel
nazwa_pliku = 'czas_wykonania_subprocesow.xlsx'
with pd.ExcelWriter(nazwa_pliku, engine='openpyxl', mode='w') as writer:
    df.to_excel(writer, index=False)

print(f'Czas wykonania subprocesów został zapisany do {nazwa_pliku}.')
