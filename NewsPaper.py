
def getDateTimeNewsPaper(newsPaper : str, news_papers_dictionary : dict):
    try:
        print(news_papers_dictionary[newsPaper])
    except:
        print('Данная газета не найдена в списке')


def main():
    row = ""
    news_papers_dictionary = {'The Moscow Times': '',
                            'The Guardian': '',
                            'Daily News': ''}

    while row != '@':
        row = input("Введите название газеты: ")

        getDateTimeNewsPaper(row, news_papers_dictionary)

main()