def run(self):
        print("\n----spell Checke-----")

        while True:
            text = input("Enter the word: ")

            if text.lower() == "exit":
                print("closing..")
                break

            corrected_text = self.correct_text(text)
            print("corrected text:",corrected_text)
