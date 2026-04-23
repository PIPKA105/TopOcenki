from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window

class RomashkaVPN(App):
    def build(self):
        # Черный фон в стиле Studio 26
        Window.clearcolor = (0, 0, 0, 1)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        # Логотип (твоя пуля-ромашка)
        # Убедись, что файл romashka.png лежит в папке с кодом
        self.logo = Image(source='romashka.png', allow_stretch=True)
        layout.add_widget(self.logo)
        
        # Единственная кнопка
        self.main_btn = Button(
            text="ПОДКЛЮЧИТЬСЯ",
            font_size='22sp',
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1), # Серый металл
            size_hint=(1, 0.3)
        )
        self.main_btn.bind(on_press=self.action)
        layout.add_widget(self.main_btn)
        
        return layout

    def action(self, instance):
        if self.main_btn.text == "ПОДКЛЮЧИТЬСЯ":
            # Тут мы запускаем твой DNS-скрипт для ботов
            success = True # Ставим False, если сервак упал
            
            if success:
                self.main_btn.text = "ПОДКЛЮЧЕНО"
                self.main_btn.background_color = (0, 0.7, 0, 1) # Зеленый
            else:
                self.main_btn.text = "НЕ УДАЛОСЬ ПОДКЛЮЧИТЬСЯ"
                self.main_btn.background_color = (0.7, 0, 0, 1) # Красный
        
        elif self.main_btn.text == "ПОДКЛЮЧЕНО" or self.main_btn.text == "НЕ УДАЛОСЬ ПОДКЛЮЧИТЬСЯ":
            # Сброс в исходное состояние
            self.main_btn.text = "ПОДКЛЮЧИТЬСЯ"
            self.main_btn.background_color = (0.2, 0.2, 0.2, 1)

if __name__ == '__main__':
    RomashkaVPN().run()
