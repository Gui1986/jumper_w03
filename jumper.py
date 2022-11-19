import random

def main():

    name = input("What is your name? ")

    print("Are you ready? Good Luck!", name)

    # list of word used in the game
    words_list = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 
    'condition', 'reverse', 'water', 'board', 'geeks', 'government', 'people', 'history', 
    'way', 'money' , 'world', 'information', 'map', 'family', 'government', 'health', 'system', 'computer',
    'meat', 'year', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding', 'theory', 'law', 'bird', 
    'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 'economics', 'byu','love',
    'internet', 'television', 'science', 'library', 'nature', 'fact', 'product', 'idea', 'temperature', 'country',
    'investment', 'area', 'society', 'activity', 'story', 'industry',  'marcos', 'media', 'thing', 'oven', 'python',
    'community', 'safety', 'quality', 'development', 'language', 'management', 'player', 'variety', 'video', 
    'week', 'security', 'country', 'movie', 'organization', 'equipment', 'physics', 'analys', 'policy', 'series', 
    'thought', 'basis', 'strategy', 'technology', 'army', 'camera', 'freedom', 'paper', 'environment', 'child', 
    'instance', 'month', 'marketing', 'university', 'article,' 'department,' 'difference', 'goal', 'news', 'audience', 
    'fishing', 'growth', 'income', 'marriage', 'user', 'combination', 'brazil', 'failure',' meaning', 'medicine', 
    'philosophy', 'teacher', 'communication', 'night', 'chemistry', 'disease', 'disk', 'energy', 'nation', 'road', 
    'role', 'soup', 'advertising', 'location', 'success', 'addition', 'apartment', 'education', 'math', 'moment', 
    'painting', 'politics', 'attention', 'decision', 'event', 'property', 'shopping', 'student', 'wood', 'competition', 
    'distribution', 'entertainment', 'office', 'population', 'president', 'unit', 'category', 'context', 'introduction', 
    'opportunity', 'performance', 'driver', 'flight', 'length', 'magazine', 'newspaper', 'relationship', 'teaching', 
    'cell', 'dealer', 'debate', 'lake','member', 'message', 'phone', 'scene', 'appearance', 'association', 'concept', 
    'customer', 'death', 'discussion', 'inflation', 'insurance', 'woman', 'advice', 'blood', 'effort', 'expression', 
    'importance', 'opinion', 'payment', 'responsibility', 'computer', 'accounting']

    # Function will choose one random, word from this list of words
    word = random.choice(words_list)

    print("Guess the letter [a-z]")

    guesses = ''

    # any number of turns can be used here
    turns = 15

    while turns > 0:

        # counts the number of times a user fails
        failed = 0

        # all characters from the input, word taking one at a time
        for char in word:

            # comparing that character with, the character in guesses
            if char in guesses:
                print(char, end=" ")

            else:
                print("_")

                # for every failure 1 will be, incremented in failure
                failed += 1

        if failed == 0:
            # user will win the game if failure is 0 and 'You won' will be given as output
            print(" You won")

            # this print the correct word
            print("The word is: ", word)
            break

        # if user has input the wrong alphabet then
        # it will ask user to enter another letter of the alphabet
        print()
        guess = input("guess a letter [a-z]:")

        # every input character will be stored in guesses
        guesses += guess

        # check input with the character in word
        if guess not in word:

            turns -= 1

            # if the character doesn’t match the word, then “Wrong” will be given as output
            print("Wrong")

            # this will print the number of
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")

if __name__ == "__main__":
    main()