class WordFilter():
    def __init__(self, ngword):
        self.ngword = ngword

    def censor(self, text):
        return text.replace(self.ngword, "<censored>")


def main():
    my_filter = WordFilter("アーセナル")
    my_filter.censor("昨日のアーセナルの試合アツかった")

    my_filter.censor("昨日のリバプールの試合アツかった")


if __name__ == "__main__":
    main()
