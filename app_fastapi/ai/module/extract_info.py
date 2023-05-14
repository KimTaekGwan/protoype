class ExtractInfo:
    def __init__(self) -> None:
        pass

    def run(self, path: str) -> dict:
        """_summary_

        Args:
            path (str): 문서 경로

        Returns:
            dict:
                page_num (int):
                    text (str): list
                    img (str): list
        """
        res = {1: {'text': [],  # 1번 페이지에서 추출한 텍스트
                   'img': []}}  # 1번 페이지에서 추출한 이미지 경로
        return res


if __name__ == '__main__':
    extractinfo = ExtractInfo()

    path = ""

    res = extractinfo.run(path)
