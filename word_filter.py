class WordFilter():
    def __init__(self, ngword):
        self.ngword = ngword

    def detect(self, text):
        result = self.ngword in text
        return result


def main():
    my_filter = WordFilter("アーセナル")
    my_filter.detect("昨日のアーセナルの試合アツかった！")

    my_filter.detect("昨日のリバプールの試合アツかった！")


if __name__ == "__main__":
    main()
