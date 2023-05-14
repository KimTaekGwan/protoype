class TextPreprocessing:
    def __init__(self) -> None:
        pass

    def preprocssing(self, text: str) -> str:
        """_summary_

        Args:
            text (str): 전처리 전 텍스트

        Returns:
            str: 전처리 후 텍스트
        """
        return res

    def run(self, docInfo: dict) -> dict:
        """_summary_

        Args:
            docInfo (dict): _description_
        #  docInfo = {'path': path,
        #            'text': text,
        #            'page': {1: text, 2: text}}

        Returns:
            dict: _description_
        #  resInfo = {'path': path,
        #            'text': text,
        #            'page': {1: text, 2: text}}
        """
        resInfo = {'path': docInfo['path'],
                   'text': '',
                   'page': {}}

        for page_num, text in docInfo['page'].items():
            resInfo['page'][page_num] = self.preprocssing(text=text)

        resInfo['text'] = self.preprocssing(text=docInfo['text'])

        return resInfo


if __name__ == '__main__':
    textprepro = TextPreprocessing()

    docInfo = {}

    docInfo = textprepro.run(docInfo=docInfo)
