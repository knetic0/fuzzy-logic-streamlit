# Hava Durumu Tahmini Uygulaması

Bu uygulama, hava durumu tahminleri yapmak için **Streamlit** ve **scikit-fuzzy** kütüphanelerini kullanır. Uygulama, bulanık mantık tabanlı bir model ile hava durumu koşullarını sınıflandırır ve kullanıcı dostu bir web arayüzü sağlar.

## Gereksinimler

Aşağıdaki bağımlılıkların sisteminizde yüklü olması gereklidir:
- Python 3.8 veya üstü
- `streamlit`
- `scikit-fuzzy`

Bağımlılıkları kolayca yüklemek için aşağıdaki adımları takip edebilirsiniz.

## Kurulum

1. **Proje Bağımlılıklarını yükleme**
   ```bash
   pip install -r requirements.txt

   # Eğer MacOS ya da Linux ortamında çalışıyorsanız.
   pip3 install -r requirements.txt

2. **Uygulamayı çalıştırma**
    ```bash
    streamlit run main.py

    # Komutu ile uygulamayı çalıştırabilirsiniz.