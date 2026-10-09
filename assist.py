import os


def replicate_directory_structure(source_dir, target_dir):
    """Проходит по всем папкам в source_dir и создает такую же структуру в target_dir."""
    # Превращаем пути в абсолютные для избежания ошибок
    source_dir = os.path.abspath(source_dir)
    target_dir = os.path.abspath(target_dir)

    # os.walk последовательно обходит все вложенные каталоги
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Получаем относительный путь текущей папки относительно исходной
        rel_path = os.path.relpath(dirpath, source_dir)

        # Формируем новый путь в целевой папке
        new_dir_path = os.path.join(target_dir, rel_path)

        # Создаем папку, если она еще не существует
        os.makedirs(new_dir_path, exist_ok=True)
        print(f"Создана папка: {new_dir_path}")


# Пример использования:
if __name__ == "__main__":
    # Замените эти пути на нужные вам
    SOURCE = "/Users/mac/Desktop/Project_NZ/nz_sdet/week01"
    TARGET = "/Users/mac/Desktop/Project_NZ/nz_sdet/week03"

    replicate_directory_structure(SOURCE, TARGET)
