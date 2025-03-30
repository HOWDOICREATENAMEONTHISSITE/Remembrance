import { App, Button, BoxLayout, Label, ScreenManager, Screen, TextInput, Clock } from 'kivy';

class MenuScreen extends Screen {
    constructor(kwargs) {
        super(kwargs);
        const layout = new BoxLayout({ orientation: 'vertical', padding: 20, spacing: 20 });

        const label = new Label({ text: "Игра на память", font_size: '40sp', size_hint: [1, 0.3] });
        layout.add_widget(label);

        const easyButton = new Button({ text: "Легкий", size_hint: [1, 0.2] });
        easyButton.bind(on_release: () => this.start_game('easy'));
        layout.add_widget(easyButton);

        const mediumButton = new Button({ text: "Средний", size_hint: [1, 0.2] });
        mediumButton.bind(on_release: () => this.start_game('medium'));
        layout.add_widget(mediumButton);

        const hardButton = new Button({ text: "Сложный", size_hint: [1, 0.2] });
        hardButton.bind(on_release: () => this.start_game('hard'));
        layout.add_widget(hardButton);

        this.add_widget(layout);
    }

    start_game(difficulty) {
        this.manager.current = 'game';
        this.manager.get_screen('game').start_game(difficulty);
    }
}

class GameScreen extends Screen {
    constructor(kwargs) {
        super(kwargs);
        this.layout = new BoxLayout({ orientation: 'vertical', padding: 20, spacing: 20 });
        this.add_widget(this.layout);
        
        this.words = ["дом", "книга", "стол", "стул", "окно", "дверь", "стена", "пол", "потолок", "лампа",
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
            "красота", "доброта", "правда", "ложь", "счастье", "горе", "любовь", "дружба", "жизнь", "смерть"];
        this.displayed_words = [];
        this.current_word_index = 0;
        this.difficulty = null;
        this.input_field = null;
    }

    start_game(difficulty) {
        this.layout.clear_widgets();
        this.difficulty = difficulty;
        this.displayed_words = this.shuffle(this.words).slice(0, 5);
        this.current_word_index = 0;
        this.show_next_word();
    }

    show_next_word(dt = 0) {
        if (this.current_word_index < this.displayed_words.length) {
            const word_label = new Label({ text: this.displayed_words[this.current_word_index], font_size: '30sp' });
            this.layout.clear_widgets();
            this.layout.add_widget(word_label);
            this.current_word_index += 1;
            const delay = { easy: 2, medium: 1.5, hard: 1 }[this.difficulty];
            Clock.schedule_once(() => this.show_next_word(), delay);
        } else {
            this.show_input_field();
        }
    }

    show_input_field() {
        this.layout.clear_widgets();
        this.input_field = new TextInput({ hint_text: "Введите слова через запятую с пробелом", multiline: false, font_size: '17.5sp' });
    }

    shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }
                      }
