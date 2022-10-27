class Voto:
    def __init__(self):
        self.__tipo_eleitor = None
        self.__candidato_reitor = None
        self.__candidato_proreitor_grad = None
        self.__candidato_proreitor_pes = None
        self.__candidato_proreitor_ext = None

    @property
    def candidato_reitor(self):
        return self.__candidato_reitor

    @candidato_reitor.setter
    def candidato_reitor(self, candidato):
        self.__candidato_reitor = candidato

    @property
    def candidato_proreitor_grad(self):
        return self.__candidato_proreitor_grad

    @candidato_proreitor_grad.setter
    def candidato_proreitor_grad(self, candidato):
        self.__candidato_proreitor_grad = candidato

    @property
    def candidato_proreitor_pes(self):
        return self.__candidato_proreitor_pes

    @candidato_proreitor_pes.setter
    def candidato_proreitor_pes(self, candidato):
        self.__candidato_proreitor_pes = candidato

    @property
    def candidato_proreitor_ext(self):
        return self.__candidato_proreitor_ext

    @candidato_proreitor_ext.setter
    def candidato_proreitor_ext(self, candidato):
        self.__candidato_proreitor_ext = candidato

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor
    
    
    
