import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st

class FuzzyWeatherApplication:
    def __init__(self):
        """
            FuzzyWeatherApplication sınıfı, bulanık mantık tabanlı bir hava durumu tahmin sistemi oluşturur.
            Bu sınıf, sıcaklık, nem, rüzgar hızı ve hava durumu gibi değişkenler arasındaki ilişkiyi modellemek için
            bulanık mantık kurallarını kullanır. Bu sınıf ayrıca Streamlit arayüzü oluşturur ve kullanıcıdan giriş
            verilerini alarak hava durumu tahminini gerçekleştirir.
        """

        # Üyelik fonksiyonlarını tanımlıyoruz
        self.temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
        self.humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
        self.wind_speed = ctrl.Antecedent(np.arange(0, 31, 1), 'wind_speed')
        self.weather_condition = ctrl.Consequent(np.arange(0, 101, 1), 'weather_condition')
        
        self.temperature['low'] = fuzz.trimf(self.temperature.universe, [0, 0, 20])
        self.temperature['medium'] = fuzz.trimf(self.temperature.universe, [10, 20, 30])
        self.temperature['high'] = fuzz.trimf(self.temperature.universe, [20, 40, 40])
        
        self.humidity['low'] = fuzz.trimf(self.humidity.universe, [0, 0, 50])
        self.humidity['medium'] = fuzz.trimf(self.humidity.universe, [30, 50, 70])
        self.humidity['high'] = fuzz.trimf(self.humidity.universe, [50, 100, 100])
        
        self.wind_speed['slow'] = fuzz.trimf(self.wind_speed.universe, [0, 0, 15])
        self.wind_speed['medium'] = fuzz.trimf(self.wind_speed.universe, [10, 15, 20])
        self.wind_speed['fast'] = fuzz.trimf(self.wind_speed.universe, [15, 30, 30])
        
        # Çıkış değişkenleri için üyelik fonksiyonları
        self.weather_condition['sunny'] = fuzz.trimf(self.weather_condition.universe, [0, 0, 25])
        self.weather_condition['cloudy'] = fuzz.trimf(self.weather_condition.universe, [20, 40, 60])
        self.weather_condition['rainy'] = fuzz.trimf(self.weather_condition.universe, [50, 75, 100])
        self.weather_condition['stormy'] = fuzz.trimf(self.weather_condition.universe, [70, 100, 100])

        # Güneşli Hava Kuralları
        rule1 = ctrl.Rule(self.temperature['high'] & self.humidity['low'] & self.wind_speed['slow'], self.weather_condition['sunny'])
        rule2 = ctrl.Rule(self.temperature['high'] & self.humidity['low'] & self.wind_speed['medium'], self.weather_condition['sunny'])
        rule3 = ctrl.Rule(self.temperature['medium'] & self.humidity['low'] & self.wind_speed['slow'], self.weather_condition['sunny'])
        rule4 = ctrl.Rule(self.temperature['medium'] & self.humidity['low'] & self.wind_speed['medium'], self.weather_condition['sunny'])
        rule5 = ctrl.Rule(self.temperature['low'] & self.humidity['low'] & self.wind_speed['slow'], self.weather_condition['sunny'])
        rule6 = ctrl.Rule(self.temperature['high'] & self.humidity['medium'] & self.wind_speed['slow'], self.weather_condition['sunny'])
        rule7 = ctrl.Rule(self.temperature['high'] & self.humidity['medium'] & self.wind_speed['medium'], self.weather_condition['sunny'])
        rule8 = ctrl.Rule(self.temperature['medium'] & self.humidity['medium'] & self.wind_speed['slow'], self.weather_condition['sunny'])
        rule9 = ctrl.Rule(self.temperature['medium'] & self.humidity['low'] & self.wind_speed['fast'], self.weather_condition['sunny'])

        # Bulutlu Hava Kuralları
        rule10 = ctrl.Rule(self.temperature['medium'] & self.humidity['medium'] & self.wind_speed['slow'], self.weather_condition['cloudy'])
        rule11 = ctrl.Rule(self.temperature['low'] & self.humidity['medium'] & self.wind_speed['slow'], self.weather_condition['cloudy'])
        rule12 = ctrl.Rule(self.temperature['medium'] & self.humidity['medium'] & self.wind_speed['medium'], self.weather_condition['cloudy'])
        rule13 = ctrl.Rule(self.temperature['low'] & self.humidity['medium'] & self.wind_speed['medium'], self.weather_condition['cloudy'])
        rule14 = ctrl.Rule(self.temperature['medium'] & self.humidity['high'] & self.wind_speed['slow'], self.weather_condition['cloudy'])
        rule15 = ctrl.Rule(self.temperature['high'] & self.humidity['medium'] & self.wind_speed['fast'], self.weather_condition['cloudy'])
        rule16 = ctrl.Rule(self.temperature['high'] & self.humidity['high'] & self.wind_speed['slow'], self.weather_condition['cloudy'])

        # Yağmurlu Hava Kuralları
        rule17 = ctrl.Rule(self.humidity['high'] & self.wind_speed['slow'], self.weather_condition['rainy'])
        rule18 = ctrl.Rule(self.temperature['medium'] & self.humidity['high'] & self.wind_speed['medium'], self.weather_condition['rainy'])
        rule19 = ctrl.Rule(self.temperature['low'] & self.humidity['high'] & self.wind_speed['medium'], self.weather_condition['rainy'])
        rule20 = ctrl.Rule(self.temperature['high'] & self.humidity['high'] & self.wind_speed['slow'], self.weather_condition['rainy'])
        rule21 = ctrl.Rule(self.temperature['medium'] & self.humidity['high'] & self.wind_speed['slow'], self.weather_condition['rainy'])
        rule22 = ctrl.Rule(self.temperature['high'] & self.humidity['high'] & self.wind_speed['medium'], self.weather_condition['rainy'])

        # Fırtınalı Hava Kuralları
        rule23 = ctrl.Rule(self.temperature['low'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule24 = ctrl.Rule(self.temperature['low'] & self.humidity['high'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule25 = ctrl.Rule(self.temperature['medium'] & self.humidity['high'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule26 = ctrl.Rule(self.temperature['high'] & self.humidity['high'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule27 = ctrl.Rule(self.temperature['low'] & self.humidity['medium'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule28 = ctrl.Rule(self.temperature['medium'] & self.humidity['medium'] & self.wind_speed['fast'], self.weather_condition['stormy'])
        rule29 = ctrl.Rule(self.temperature['high'] & self.humidity['low'] & self.wind_speed['fast'], self.weather_condition['stormy'])

        self.control_system = ctrl.ControlSystem([
            rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
            rule10, rule11, rule12, rule13, rule14, rule15, rule16,
            rule17, rule18, rule19, rule20, rule21, rule22,
            rule23, rule24, rule25, rule26, rule27, rule28, rule29
        ])
        
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)

    def run_simulation(self, temp, hum, wind):
        """Hava durumu tahminini gerçekleştirir.

        Args:
            temp (int): Hava sıcaklığı.
            hum (int): Nem oranı.
            wind (int): Rüzgar hızı.

        Returns:
            int: Elde edilen sonuç.
        """

        # Giriş verilerini ayarla
        self.simulation.input['temperature'] = temp
        self.simulation.input['humidity'] = hum
        self.simulation.input['wind_speed'] = wind

        self.simulation.compute()
        result = self.simulation.output['weather_condition']
        return result
       

    def render(self):
        """
            Streamlit arayüzünü oluşturur ve kullanıcıdan giriş verilerini alarak hava durumu tahminini gerçekleştirir.
        """

        # Streamlit arayüzü
        st.title("Bulanık Mantık Hava Durumu Tahmini")
        
        # Kullanıcıdan giriş verilerini al
        temp = st.slider("Sıcaklık (°C)", 0, 40, 20).as_integer_ratio()[0]
        hum = st.slider("Nem (%)", 0, 100, 50).as_integer_ratio()[0]
        wind = st.slider("Rüzgar Hızı (km/s)", 0, 30, 10).as_integer_ratio()[0]

        if st.button("Tahmin Et"):
            result = self.run_simulation(temp, hum, wind)
            
            st.subheader("Tahmin Edilen Hava Durumu")
            if result < 25:
                st.write("🌞 **Güneşli**")
            elif result < 50:
                st.write("☁️ **Bulutlu**")
            elif result < 75:
                st.write("🌧️ **Yağmurlu**")
            else:
                st.write("🌩️ **Fırtınalı**")
            
            st.write(f"Tahmin Skoru: {result:.2f}")
        else:
            st.write("Butona basarak tahmini başlatabilirsiniz.")