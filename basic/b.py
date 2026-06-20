#1
def normalize_tool_name(tool_name: str) -> str:
    clean_data = tool_name.strip().lower()

    return clean_data

print(normalize_tool_name("   SeaRCH    "))


#2
def is_json_file(filename: str) -> bool:
    clean_data = filename.lower()
    if clean_data.endswith(".json"):
        return True
    
    return False

#3
text = "  Hello, WORLD.  "

text = text.lower().replace(',','').replace('.','').strip()

print(text)

#4
def count_words(text: str) -> dict:
    texts = text.lower().replace(',',' ').replace('.',' ').strip().split()
    word_counts = {}
    for word in texts:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

text = "Apple, banana apple. Orange banana apple"
print(count_words(text))

#5
errors = "timeout database timeout validation timeout database"

errors = errors.split()
error_counts = {}
for error in errors:
    if error in error_counts:
        error_counts[error] += 1
    else:
        error_counts[error] = 1

print(error_counts)
