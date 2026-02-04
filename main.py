from pathlib import Path
import shutil


FOLDERS: dict[str, list[str]] = {
    'Изображения': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
    'Видео': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.webm'],
    'Аудио': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
    'Документы': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    'Архивы': ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
    'Программы': ['.exe', '.msi', '.dmg', '.apk', '.deb'],
    'Код': ['.py', '.java', '.js', '.html', '.css', '.json', '.xml'],
    'Книги': ['.epub', '.mobi', '.fb2', '.pdf'],
    'Остальное': []
}

def find_category(extension: str) -> str:
    for folder, extensions in FOLDERS.items():
        if extension in extensions:
            return folder
    return 'Остальное'
    
def create_category(source_path: Path) -> None:
    for category in FOLDERS.keys():
        category_folder: Path = source_path / category
        category_folder.mkdir(exist_ok=True)

def move_file(source_path: Path, category: str, file: Path) -> None:
    destination_folder: Path = source_path / category
    destination_path: Path = destination_folder / file.name
    shutil.move(str(file), str(destination_path))

def main(source_dir: str) -> None: 
    source_path: Path = Path(source_dir)
    
    create_category(source_path=source_path)
    
    for file in source_path.iterdir():
        if not file.is_file():
            continue

        category: str = find_category(extension=file.suffix)
        move_file(
            source_path=source_path,
            category=category,
            file=file
        )
    
if __name__ == '__main__':
    source_dir: str = input("Введите путь до папки: ")
    main(source_dir)
