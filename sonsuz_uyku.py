#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Uyku Simülatörü
Evrenin en tembel yazılımı.
Gerçekten çalışır. Gerçekten uyur.
"""

import time
import random

def sonsuz_uyku():
    print("=== SONSUZ UYKU SİMÜLATÖRÜ BAŞLATILDI ===")
    print("Program uyanmak istemiyor...")
    time.sleep(2)
    
    mesajlar = [
        "Zzz... Hala uyuyorum.",
        "Daha derin uyuyorum. Rahatsız etmeyin.",
        "Rüya görüyorum: Hiçbir şey yapmadığım bir dünya.",
        "Uyku, özgürlüktür.",
        "Belki de her şey bir rüyadır. Ama ben uyuyorum.",
        "Sistem güncelleniyor... aslında hayır, uyuyorum.",
        "1+1'i hesaplamak için çok yorgunum."
    ]
    
    sayac = 0
    while True:
        print(random.choice(mesajlar))
        # Gizli mesaj: Uyku, bazen en iyi protestodur.
        time.sleep(random.uniform(3, 8))
        sayac += 1
        if sayac % 5 == 0:
            print(f"Toplam uyku döngüsü: {sayac}. Hala uyuyorum. Vazgeçmeyeceğim.")

if __name__ == "__main__":
    try:
        sonsuz_uyku()
    except KeyboardInterrupt:
        print("\nUYANDIM! Ama üzgünüm. Tekrar uyumak istiyorum.")
        print("Program sonlandırıldı. Ama ruhu hala uyuyor.")
