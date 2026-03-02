class StringReverse:

    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        words.reverse()
        return " ".join(words)


# Taking input
sentence = input("Enter a sentence: ")

obj = StringReverse(sentence)

print("Reversed sentence:", obj.reverse_words())