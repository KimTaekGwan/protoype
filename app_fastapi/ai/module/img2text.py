class OCR:
    def __init__(self) -> None:
        pass

    def run(self, img_path: str) -> str:
        """_summary_

        Args:
            img_path (str): 이미지 경로

        Returns:
            str: 이미지에서 추출한 텍스트
        """
        res = ""
        return res


class Captioning:
    def __init__(self) -> None:
        pass

    def run(self, img_path: str) -> str:
        """_summary_

        Args:
            img_path (str): 이미지 경로

        Returns:
            str: 이미지에서 텍스트로 변환 결과
        """
        res = ""
        return res


if __name__ == '__main__':
    ocr = OCR()
    captioning = Captioning()

    img_path = ""

    res = ocr.run(img_path=img_path)
    res = captioning.run(img_path=img_path)
