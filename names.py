import unicodedata
import locale

def sort_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read().split(',')
    
    cleaned_names = []
    for name in names:
        name = name.strip()
        parts = name.split(' ')
        if len(parts) == 2:
            first, last = parts
            middle = ''
        else:
            first, *middle, last = parts
            middle = ' '.join(middle)
        cleaned_names.append((first, middle, last))
    
    has_polish_chars = any(
        'ą' in name or 'ć' in name or 'ę' in name or 'ł' in name or 'ń' in name or 'ó' in name or 'ś' in name or 'ź' in name or 'ż' in name
        for first, middle, last in cleaned_names
        for name in (first, middle, last)
    )
    
    if has_polish_chars:
        locale.setlocale(locale.LC_COLLATE, 'pl_PL.UTF-8')
        sorted_names = sorted(cleaned_names, key=lambda x: locale.strxfrm(x[2]))
    else:
        sorted_names = sorted(cleaned_names, key=lambda x: x[2])
    
    formatted_names = []
    for first, middle, last in sorted_names:
        if middle:
            formatted_name = f"{first} {middle} {last}"
        else:
            formatted_name = f"{first} {last}"
        formatted_names.append(formatted_name.title())
    
    result = ", ".join(formatted_names)
    
    return result

def save_sorted_names(sorted_names, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(sorted_names)
    print(f"Sorted names saved to {output_file}")

input_file = 'names.txt'
output_file = 'sorted_names.txt'

sorted_names = sort_names(input_file)
save_sorted_names(sorted_names, output_file)
print(sorted_names)