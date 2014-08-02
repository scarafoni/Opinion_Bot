import unittest
class sentence_completion_test(unittest.TestCase):
    def test_complete_one(self):
        sentence = "green eggs and";
        correct_guess = "ham" 
        sentence_completer  = Sentence_Completer("green eggs and ham",3)
        guess = sentence_completer.guess(sentence)
        self.asserEqual(guess,correct_guess,"didn't guess 'green eggs and ham'")




if __name__ == "__main__":
    unittest.main()