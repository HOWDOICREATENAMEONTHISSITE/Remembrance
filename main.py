from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import random

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        label = Label(text="Игра на память", font_size='40sp', size_hint=(1, 0.3))
        layout.add_widget(label)

        easy_button = Button(text="Легкий", size_hint=(1, 0.2))
        easy_button.bind(on_release=lambda x: self.start_game('easy'))
        layout.add_widget(easy_button)

        medium_button = Button(text="Средний", size_hint=(1, 0.2))
        medium_button.bind(on_release=lambda x: self.start_game('medium'))
        layout.add_widget(medium_button)

        hard_button = Button(text="Сложный", size_hint=(1, 0.2))
        hard_button.bind(on_release=lambda x: self.start_game('hard'))
        layout.add_widget(hard_button)

        self.add_widget(layout)

    def start_game(self, difficulty):
        self.manager.current = 'game'
        self.manager.get_screen('game').start_game(difficulty)

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.add_widget(self.layout)
        
        self.words = ["дом", "книга", "стол", "стул", "окно", "дверь", "стена", "пол", "потолок", "лампа",
            "кровать", "шкаф", "зеркало", "картина", "диван", "кресло", "подушка", "одеяло", "плед", "ковёр",
            "телефон", "компьютер", "телевизор", "холодильник", "плита", "микроволновка", "чайник", "тарелка",
            "чашка", "ложка", "вилка", "нож", "тарелка", "кастрюля", "сковородка", "посуда", "еда", "вода",
            "соль", "сахар", "перец", "хлеб", "масло", "сыр", "молоко", "мясо", "рыба", "фрукты", "овощи",
            "яблоко", "груша", "банан", "апельсин", "помидор", "огурец", "картофель", "морковь", "лук", "чеснок",
            "цветы", "дерево", "трава", "куст", "солнце", "луна", "звёзды", "небо", "облако", "дождь", "снег",
            "ветер", "море", "река", "озеро", "лес", "гора", "дорога", "машина", "автобус", "поезд", "самолёт",
            "город", "деревня", "село", "улица", "площадь", "парк", "дом", "квартира", "комната", "человек",
            "женщина", "мужчина", "ребёнок", "собака", "кошка", "птица", "рыба", "песня", "музыка", "танец",
            "работа", "учёба", "отдых", "день", "ночь", "утро", "вечер", "час", "минута", "секунда", "год",
            "месяц", "неделя", "зима", "весна", "лето", "осень", "холод", "тепло", "жара", "свет", "тьма",
            "красота", "доброта", "правда", "ложь", "счастье", "горе", "любовь", "дружба", "жизнь", "смерть"]
        self.displayed_words = []
        self.current_word_index = 0
        self.difficulty = None
        self.input_field = None

    def start_game(self, difficulty):
        self.layout.clear_widgets()
        self.difficulty = difficulty
        self.displayed_words = random.sample(self.words, 5)
        self.current_word_index = 0
        self.show_next_word()

    def show_next_word(self, dt=0):
        if self.current_word_index < len(self.displayed_words):
            word_label = Label(text=self.displayed_words[self.current_word_index], font_size='30sp')
            self.layout.clear_widgets()
            self.layout.add_widget(word_label)
            self.current_word_index += 1
            delay = {'easy': 2, 'medium': 1.5, 'hard': 1}[self.difficulty]
            Clock.schedule_once(self.show_next_word, delay)
        else:
            self.show_input_field()

    def show_input_field(self):
        self.layout.clear_widgets()
        self.input_field = TextInput(hint_text="Введите слова через запятую и пробел", multiline=False, font_size='20sp')
        submit_button = Button(text="Проверить", on_release=self.check_answer)
        self.layout.add_widget(self.input_field)
        self.layout.add_widget(submit_button)

    def check_answer(self, instance):
        user_input = self.input_field.text.strip()
        correct_answer = ", ".join(self.displayed_words)
        if user_input == correct_answer:
            self.show_success()
        else:
            self.show_failure()

    def show_success(self):
        self.layout.clear_widgets()
        success_label = Label(text="Отлично!", font_size='30sp')
        menu_button = Button(text="Главное меню")
        menu_button.bind(on_release=self.goto_menu)
        self.layout.add_widget(success_label)
        self.layout.add_widget(menu_button)

    def show_failure(self):
        self.layout.clear_widgets()
        failure_label = Label(text="Неправильно.", font_size='30sp')
        restart_button = Button(text="Заново", on_release=lambda x: self.start_game(self.difficulty))
        menu_button = Button(text="Главное меню")
        menu_button.bind(on_release=self.goto_menu)
        self.layout.add_widget(failure_label)
        self.layout.add_widget(restart_button)
        self.layout.add_widget(menu_button)

    def goto_menu(self, instance):
        self.manager.current = 'menu'

class MemoryGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm

if __name__ == '__main__':
    MemoryGameApp().run()