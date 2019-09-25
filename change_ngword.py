class WordFilter():
    def __init__(self, ngword):
        self.ngword = ngword

    def detect(self, text):
        result = self.ngword in text
        return result


def main():
    # flagで入力を続けるかどうかの判断
    flag = "Y"
    while flag == "Y":
        ngword = input("NGワードを入力してください > ")

        my_filter = WordFilter(ngword)

        text = input("NGワードフィルタをかける文章を入力 >")
        if my_filter.detect(text) == True:
            print("NGワードは含まれます")
        else:
            print("NGワードは含まれません")

        flag = input("続けますか？(Y/N)")


if __name__ == "__main__":
    main()
