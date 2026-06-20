import json

def load_json_file(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
    
    except FileNotFoundError:
        print("file not exist")
        return None

    except json.JSONDecodeError:
        print("Json format error")
        return None



def save_json_file(filename: str, data) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        data = json.dump(data, file, indent=2, ensure_ascii=False)