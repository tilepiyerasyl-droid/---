import json

class Portfolio:
    def __init__(self, data_filepath):
        self.data_filepath = data_filepath
        with open(self.data_filepath, "r", encoding="utf-8") as file:
            self.info_blocks = json.load(file)

    def show_menu(self):
        while True:
            print("\n=== МОЁ ПОРТФОЛИО ===")
            print("1. О себе")
            print("2. Моя цель")
            print("3. Как я пришел в IT")
            print("4. Мой ментор")
            print("5. Точка А → Точка Б (Мой прогресс)")
            print("6. Хобби и интересы")
            print("7. Мои лучшие работы")
            print("8. Ссылка на GitHub")
            print("0. Выход из программы")
            print("=====================")
            
            choice = input("Выберите нужный пункт (0-8): ")

            if choice == "1":
                block = self.info_blocks.get("about_me")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "2":
                block = self.info_blocks.get("my_goal")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "3":
                block = self.info_blocks.get("path_to_it")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "4":
                block = self.info_blocks.get("mentor")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "5":
                block = self.info_blocks.get("progress")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "6":
                block = self.info_blocks.get("hobbies")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "7":
                block = self.info_blocks.get("best_works")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "8":
                block = self.info_blocks.get("github")
                print(f"\n--- {block['title']} ---\n{block['content']}")
            elif choice == "0":
                print("\nВыход из программы.")
                break
            else:
                print("\nНеправильный ввод! Введи цифру от 0 до 8.")

if __name__ == "__main__":
    my_portfolio = Portfolio("data.json")
    my_portfolio.show_menu()