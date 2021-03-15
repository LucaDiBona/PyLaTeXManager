class latexFile():

    def __init__(self, fileName: str) -> None:
        self.fileName=fileName
        self.__f=open(fileName, "a+")
        self.__f.seek(0)
        self.__fContentsI=self.__f.read()
        print(self.__fContentsI)
        self.fContents=self.__fContentsI