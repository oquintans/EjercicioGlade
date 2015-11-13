__author__ = 'oquintansocampo'

from gi.repository import Gtk


class ExemploBoxGTK3(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo de Box")

        # LayoutBox1 (Vertical)
        self.caixa = Gtk.Box(spacing=6)
        self.caixa.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.caixa)

        # LayoutBox2 (Horizontal)
        self.caixa2 = Gtk.Box(spacing=6)
        self.caixa.pack_end(self.caixa2, True, True, 3)

        # Boton1
        self.boton1 = Gtk.Button(label="Ola")
        self.boton1.connect("clicked", self.on_boton1_clicked)
        self.caixa2.pack_start(self.boton1, True, True, 3)

        # Boton2
        self.boton2 = Gtk.Button(label="Adeus")
        self.boton2.connect("clicked", self.on_boton2_clicked)
        self.caixa2.pack_start(self.boton2, True, True, 3)

        # Label
        self.label1 = Gtk.Label(label="Texto")
        self.caixa.pack_start(self.label1, True, True, 3)

    def on_boton1_clicked(self, control):
        print("Ola")
        self.label1.set_text("Ola")

    def on_boton2_clicked(self, widget):
        print("Adeus")
        self.label1.set_text("Adeus")


# Instanciar
fiestra = ExemploBoxGTK3()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Maximizable Off
fiestra.set_resizable(False)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# Activar atencion de eventos
Gtk.main()
