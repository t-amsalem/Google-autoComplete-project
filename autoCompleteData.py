
class AutoCompleteData:
    def __init__(self, sentence, source_text, offset):
        self.completed_sentence = sentence
        self.source_text = source_text
        self.offset = offset
        self.score = 0

    def get_completed_sentence(self):
        return self.completed_sentence

    def get_source_text(self):
        return self.source_text

    def get_offset(self):
        return self.offset

    def get_score(self):
        return self.score











