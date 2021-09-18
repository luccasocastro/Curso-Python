class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def getEstado(self) -> bool:
        return self.__estado

    def setEstado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor

