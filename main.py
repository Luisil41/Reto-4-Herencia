class Serie():
    titulo = ''
    __numero_temporadas = 3
    prestado = False
    genero = ''
    creador = ''

    series = ['naruto', 'one piece', 'son goku', 'los simpsons', 'pokemon']

    def __init__(self, titulo, genero, creador):
        self.titulo = titulo
        self.genero = genero
        self.creador = creador

    def get_titulo(self):
        return self.titulo

    def get_numero_temporadas(self):
        return self.numero_temporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    def entregar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False


class Videojuego():
    titulo = ''
    horas_estimadas = 10
    entregado = False
    genero = ''
    compañia = ''

    videojuegos = ['nba 2k20', 'FIFA 2020', 'Spyro', 'Kingdom Hearts', 'GTA Vice City']

    def __init__(self, titulo, genero, compañia):
        self.titulo = titulo
        self.genero = genero
        self.creador = compañia

    def get_titulo(self):
        return self.titulo

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def get_genero(self):
        return self.genero

    def get_compañia(self):
        return self.compañia

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_genero(self, genero):
        self.genero = genero

    def set_compañia(self, compañia):
        self.compañia = compañia

    def entregar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False


serie1 = Serie('naruto', 'Anime', 'nakamoto')
juego1 = Videojuego('Final Fantasy IV', 'Open World', 'Nintendo')


print(serie1.get_creador())
serie1.set_creador('Manolo Escobar')
print(serie1.get_creador())
print(serie1.entregar())
print(juego1.get_titulo())

