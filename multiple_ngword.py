class WordFilter():
    def __init__(self, ngword):
        self.ngword = ngword

    def detect(self, text):
        for i in self.ngword:
            result = i in text
            if result == True:
                break
        return result


def main():
    ngword = input("NGワード入力（複数ある場合はスペース区切り） > ").split()
    my_filter = WordFilter(ngword)

    text = input("NGワードフィルタをかける文章を入力 > ")
    if my_filter.detect(text) == True:
        print("NGワードが含まれます")
    else:
        print("NGワードは含まれません")


if __name__ == "__main__":
    main()
