from extract_info import ExtractInfo
from image_classification import ImageClassification
from img2text import OCR, Captioning
from text_preprocessing import TextPreprocessing
from text2vector import Text2Vector


class Doc2Vector:
    def __init__(self) -> None:
        pass

    def run(self, path: str) -> dict:
        """_summary_

        Args:
            path (str): 문서 경로

        Returns:
            dict: 문서 벡터화
        """
        # (2) 문서 내 텍스트 및 이미지 추출
        extractinfo = ExtractInfo()
        infoDict = extractinfo.run(path)

        # infoDict = {1: {'text': [],  # 1번 페이지에서 추출한 텍스트
        #                 'img': []}}  # 1번 페이지에서 추출한 이미지 경로

        # (3) 이미지 유형 분류
        imgclsfc = ImageClassification()
        ocr = OCR()
        captioning = Captioning()

        for _, typedata in infoDict.items():
            typedata['img2text'] = []
            for img_path in typedata['img']:
                img_type = imgclsfc.run(img_path=img_path)

                if img_type == 1:   # 1: 표 및 프로세스 (ocr)
                    text = ocr.run(img_path=img_path)
                elif img_type == 2:  # 2: 그림 (ImageCaptioning)
                    text = captioning.run(img_path=img_path)
                typedata['img2text'].append(text)

        # (4) 텍스트 합치기
        # infoDict = {1: {'text': [],  # 1번 페이지에서 추출한 텍스트
        #                 'img': []},  # 1번 페이지에서 추출한 텍스트
        #                 'img2text': []}}    # 이미지에서 텍스트로 변환한 데이터
        # docInfo = {'path': path,
        #            'text': text,
        #            'page': {1: text, 2: text}}

        docInfo = {'path': path,
                   'text': '',
                   'page': {}}

        for page_num, typedata in infoDict.items():
            page_text = ' '.join(typedata['text']) + \
                ' '.join(typedata['img2text'])
            docInfo['page'][page_num] = page_text

        for _, text in docInfo['page'].items():
            docInfo['text'] += text

        # (5) 텍스트 전처리
        textprepro = TextPreprocessing()
        docInfo = textprepro.run(docInfo=docInfo)

        # (6) BERT 문서 벡터화
        t2v = Text2Vector()
        docInfo = t2v.run(docInfo=docInfo)

        return docInfo


if __name__ == '__main__':
    process = Doc2Vector()

    path = ""

    process.run(path)
