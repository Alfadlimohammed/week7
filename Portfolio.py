def unique_letters_sorted(input_string):
    unique_letters_set = set(input_string)
    unique_letters_sorted_list = sorted(char for char in unique_letters_set if char.isalpha())
    return unique_letters_sorted_list
input_string = "cheese"
result = unique_letters_sorted(input_string)
print(result)
if __name__ == '__main__':
    def letters_in_either(word1, word2):
        return sorted(list(set(word1) | set(word2)))
def letters_in_both(word1, word2):
    return sorted([char for char in word1 if char in word2])
def letters_in_either_but_not_both(word1, word2):
    return sorted(list(set(word1) ^ set(word2)))
word1 = "hello"
word2 = "world"
result1 = letters_in_either(word1, word2)
result2 = letters_in_both(word1, word2)
result3 = letters_in_either_but_not_both(word1, word2)
print("Letters in either word:", result1)
print("Letters in both words:", result2)
print("Letters in either but not both:", result3)
if __name__ == '__main__':
    country_capitals = {}
    while True:
        country = input("Enter a country name (or 'exit' to terminate): ").strip().capitalize()
        if country == 'Exit':
            break
        capital = country_capitals.get(country)
        if capital:
            print(f"The capital of {country} is {capital}")
        else:
            capital = input(f"Enter the capital city of {country}: ").strip().capitalize()
            country_capitals[country] = capital
            print(f"Added {country} with capital {capital} to the list.")
    print("Program terminated.")
if __name__ == '__main__':
    from collections import Counter
    def frequency_analysis(message):
        cleaned_message = ''.join(filter(str.isalpha, message.lower()))
        letter_freq = Counter(cleaned_message)
        most_common = letter_freq.most_common(6)
        print("Six most common letters and their frequencies:")
        for letter, count in most_common:
            print(f"{letter}: {count}")
    message = "This is a sample message for frequency analysis."
    frequency_analysis(message)