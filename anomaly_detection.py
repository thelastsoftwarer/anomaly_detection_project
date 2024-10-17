import numpy as np
import time


# Veri akışını simüle eden fonksiyon
def veri_akisi_simulasyonu(steps=100):
    trend = 0  #first trend value
    period = 30  # The period for sinus wave
    noise_scale = 0.5  # moss amount

    for i in range(steps):
        # growing trend
        trend += 0.05

        seasonal = np.sin(2 * np.pi * i / period)

        # adding noice
        noise = np.random.normal(0, noise_scale)

        # Symlation data
        veri = trend + seasonal + noise

        # print datas
        print(f"Adım {i}: Veri {veri}")

        # waiting periodd
        time.sleep(0.1)  # we generate a data per 0.1 second


# Start smylation
veri_akisi_simulasyonu(steps=50)  # generate datas for 50 steps
from collections import deque

pencere_boyutu = 20
z_threshold = 2  # threshold value


# data flow and anomaly detect
def veri_akisi_anomali_tespiti(steps=100):
    trend = 0
    period = 30
    noise_scale = 0.5
    pencere = deque(maxlen=pencere_boyutu)
    anomali_listesi = []

    for i in range(steps):

        trend += 0.05
        seasonal = np.sin(2 * np.pi * i / period)
        noise = np.random.normal(0, noise_scale)
        veri = trend + seasonal + noise

        pencere.append(veri)


        if len(pencere) == pencere_boyutu:
            ortalama = np.mean(pencere)
            std_sapma = np.std(pencere)

            z_score = (veri - ortalama) / std_sapma if std_sapma != 0 else 0

            if abs(z_score) > z_threshold:
                print(f"Anomali tespit edildi! Adım {i}, Veri: {veri}, Z-score: {z_score}")
                anomali_listesi.append((i, veri))
            else:
                print(f"Adım {i}: Veri {veri} - Normal")
        else:
            print(f"Adım {i}: Veri {veri} - Yeterli veri yok (Pencere dolmadı)")

        # siumatling data flow time for real time
        time.sleep(0.1)

    return anomali_listesi


# Anomaly detect and start simulation
anomaliler = veri_akisi_anomali_tespiti(steps=50)
print(f"Toplam anomali sayısı: {len(anomaliler)}")
import matplotlib.pyplot as plt

#
pencere_boyutu = 20  # how many data will be used moving avarege
z_threshold = 2  # Z-score threshold value


# data flow and anomaly detection
def veri_akisi_anomali_tespiti_grafikli(steps=100):
    trend = 0
    period = 30
    noise_scale = 0.5
    pencere = deque(maxlen=pencere_boyutu)  # moving window
    veri_listesi = []
    anomali_listesi = []

    for i in range(steps):
        # simulated data generation
        trend += 0.05
        seasonal = np.sin(2 * np.pi * i / period)
        noise = np.random.normal(0, noise_scale)
        veri = trend + seasonal + noise

        # data add window
        pencere.append(veri)
        veri_listesi.append(veri)  # add all datas

        # calculating moving average and standard deviation
        if len(pencere) == pencere_boyutu:
            ortalama = np.mean(pencere)
            std_sapma = np.std(pencere)

            # Z-score calculate
            z_score = (veri - ortalama) / std_sapma if std_sapma != 0 else 0

            # if detect to threshold mark it as anomaly
            if abs(z_score) > z_threshold:
                print(f"Anomali tespit edildi! Adım {i}, Veri: {veri}, Z-score: {z_score}")
                anomali_listesi.append((i, veri))  # add anonamie to list
            else:
                print(f"Adım {i}: Veri {veri} - Normal")
        else:
            print(f"Adım {i}: Veri {veri} - Yeterli veri yok (Pencere dolmadı)")

        # Waiting time to simulate a real-time data stream
        time.sleep(0.1)

    # drawing graph
    plt.plot(range(steps), veri_listesi, label="Veri Akışı", color='blue')

    #mark anomalies in red
    if anomali_listesi:
        anomali_indexleri, anomali_verileri = zip(
            *anomali_listesi)  # Anomali noktalarının indeks ve veri değerlerini al
        plt.scatter(anomali_indexleri, anomali_verileri, color='red', label="Anomaliler")

    plt.title("Veri Akışı ve Anomaliler")
    plt.xlabel("Adımlar")
    plt.ylabel("Veri Değeri")
    plt.legend()
    plt.show()


# detect anomal and start simulation
veri_akisi_anomali_tespiti_grafikli(steps=100)

