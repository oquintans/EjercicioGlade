__author__ = 'oquintansocampo'

from gi.repository import Gtk


class ExemploGridGTK3(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo de Grid")

        # LayoutGrid
        grid = Gtk.Grid()
        self.add(grid)

        # Botones
        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")

        grid.add(boton1)
        # attach(control,nCol,nFil,ancho,alto)
        grid.attach(boton2, 1, 0, 2, 1)
        grid.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(boton5, 1, 2, 1, 1)
        grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)


# Instanciar
fiestra = ExemploGridGTK3()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# Activar atencion de eventos
Gtk.main()
