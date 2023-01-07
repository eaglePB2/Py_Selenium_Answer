convert = [i.strip().split('|') for i in open('raw_data.txt', 'r', encoding='UTF-8')]
with open('dictionary.txt', 'w', encoding='UTF-8') as f:
    for num, chinese, english, sentence in convert:
        print(chinese + " = " + english)
        f.write(chinese + " = " + english + "\n")