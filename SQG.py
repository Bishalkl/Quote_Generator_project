# first put random library
import random

# collect and store quotes
quotes_set= set([
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron",
    "Life is what happens when you're busy making other plans. - John Lennon"
])

# make set as a list
quotes_list = list(quotes_set) # we conver the set to list because random function doesn't support a set 

# create the quote generator function
def get_random_quote(quotes):
    return random.choice(quotes_list) #random.choice function

# display a random quotes
if __name__ == "__main__":
    print("Here is a random quote for you:")
    print(get_random_quote(quotes_list))


