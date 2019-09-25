class WordFilter():
    def __init__(self, ngword):
        self.ngword = ngword

    def censor(self, text):
        inputtext = input("アーセナルと置き換えるワードを入力して下さい > ")
        return text.replace(self.ngword, inputtext)


def main():
    my_filter = WordFilter("アーセナル")

    print("昨日のアーセナルの試合アツかったを置き換えます")
    print(my_filter.censor("昨日のアーセナルの試合アツかった"))


if __name__ == "__main__":
    main()
