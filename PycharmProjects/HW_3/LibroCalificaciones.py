
class LibroCalificaciones:

    def __init__(self, nombre):


        self.nombre_del_curso = nombre



    def establecer_nombre_del_curso(self, nombre):

        self.nombre_del_curso = nombre

    def obtener_nombre_del_curso(self):

        return self.nombre_del_curso


    def mostrar_mensaje(self):
        print("Bienvenido al Libro de calificaciones para", self.obtener_nombre_del_curso() + "!")


class PruebaLibroCalificaciones:
    @staticmethod
    def main():
        libro_calificaciones1 = LibroCalificaciones("CS101 Introduccion a la programacion en Java")


        libro_calificaciones2 = LibroCalificaciones("CS102 Estructuras de datos en Java")

        print("El nombre del curso de libroCalificaciones1 es:", libro_calificaciones1.obtener_nombre_del_curso())

        print("El nombre del curso de libroCalificaciones2 es:", libro_calificaciones2.obtener_nombre_del_curso())


PruebaLibroCalificaciones.main()