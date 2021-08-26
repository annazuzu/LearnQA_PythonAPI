class TestEx10CatchPhrase:
    def test_catch_phrase(self):
        phrase = input("Set a phrase: ")

        assert len(phrase) <= 15, "More than 15 symbols in that phrase"
