import json 

def get_UK_text():
    with open('jawiki-country.json', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']

def main():
    text = get_UK_text()
    print(text)

if __name__ == '__main__':
    main()