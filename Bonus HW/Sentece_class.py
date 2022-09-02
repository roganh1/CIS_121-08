class Sentence:
    def __init__(self, string):
        self.Sentence = str(string)

    def get_sentence(self):
        return self.Sentence

    def get_words(self):
        return self.Sentence.split(" ")

    def get_length(self):
        return len(self.Sentence)

    def get_num_words(self):
        return len(self.get_words())

    def __str__(self):
        return self.Sentence


class Sentence1:
    def __init__(self, string):
        self.Sentence = string.split(" ")

    def get_sentence(self):
        return self.Sentence

    def get_words(self):
        return self.Sentence.split(" ")

    def get_length(self):
        return len(self.Sentence)

    def get_num_words(self):
        return len(self.get_words())

    def capitalize_words(self):
        return self.Sentence.upper()

    def __getitem__(self, item):
        pass

    def __len__(self):
        return len(self)

    def __contains__(self, item):
        pass
