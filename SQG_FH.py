import random 

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return quotes

# function for get_random_quotes
def get_random_quote(quotes):
    return random.choice(quotes).strip()

# function main
def main():
    quotes = load_quotes('quotes.txt')
    print("Here's a random quotes for you:\n")
    print(get_random_quote(quotes))


# main constructor
if __name__ == '__main__':
    main()