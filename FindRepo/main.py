from argpars.parser import parser
from reader.reader import read_file
from search.search import find
from split.split import Split

def main():
    args = parser.parse_args()
    
    if args.file is None:
        print('Не указан файл')
        return

    text, ftype = read_file(args.file)
    
    is_code = ftype in ['py']

    split_class = Split()

    if is_code:
        splited_text = split_class.split_code(text, code_lang=ftype)
        print('Поиск по коду')
    else:
        splited_text = split_class.split_text(text)
        print('Поиск по тексту')

    print(f'Текст разделен на {len(splited_text)} частей')
    dict_link = dict()

    for i in range(len(splited_text)):
        print(f'Поиск по {i} части')
        result = find(splited_text[i][0], is_code=is_code)
        
        for key in result:
            dict_link[key] = dict_link.get(key, 0) + 1
    
    for link in dict(sorted(dict_link.items(), key=lambda item: -item[1])):
        print(f'Результат: {link}. Количество совпадений: {dict_link[link]}')
    

if __name__ == "__main__":
    main()
