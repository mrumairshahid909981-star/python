#find frequency of each word in a list using dictionary
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {
    "apple": words.count("apple"),
    "banana": words.count("banana"),
    "orange": words.count("orange")
}

print(frequency)
#soluton two
words = ["apple", "banana", "apple", "orange", "banana", "apple"]


print( "apple", words.count("apple"))
print("banana", words.count("banana"))
print("orange", words.count("orange"))
