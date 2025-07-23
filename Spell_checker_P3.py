from spellchecker import SpellChecker
class SpellchekerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self,text):
        words = text.split()
        correct_words = []

        for word in words:
            correct_word = self.spell.correction(word)
            if correct_word != word.lower():
                print(f"correcting {word} to {correct_word}")
                correct_words.append(correct_word)

        return " ".join(correct_words)
    

    def run(self):
        print("\n----spell Checke-----")

        while True:
            text = input("Enter the word: ")

            if text.lower() == "exit":
                print("closing..")
                break

            corrected_text = self.correct_text(text)
            print("corrected text:",corrected_text)

#if __name__ == "__main__":
SpellchekerApp().run()