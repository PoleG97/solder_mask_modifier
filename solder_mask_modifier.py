import pcbnew
import wx
import os

class SolderMaskModifierPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Solder Mask Modifier"
        self.category = "Modify PCB"
        self.description = "Modifica la expansión de la máscara de soldadura de componentes seleccionados"
        self.icon_file_name = ""  # Opcional: puedes agregar un ícono si lo deseas

    def Run(self):
        # Mostrar la ventana del plugin
        app = wx.App(False)
        frame = SolderMaskModifierDialog(None, "Solder Mask Modifier")
        frame.Show()
        app.MainLoop()


class SolderMaskModifierDialog(wx.Frame):
    def __init__(self, parent, title):
        super(SolderMaskModifierDialog, self).__init__(parent, title=title, size=(400, 300))

        # Configurar la ventana principal
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Campo de texto para las referencias
        lbl_referencias = wx.StaticText(panel, label="Referencias de componentes (separadas por comas):")
        self.txt_referencias = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(350, 100))

        # Campo de texto para el valor de expansión
        lbl_expansion = wx.StaticText(panel, label="Nuevo valor de expansión de máscara (en mm):")
        self.txt_expansion = wx.TextCtrl(panel, size=(100, 25))

        # Botón para aplicar cambios
        btn_aplicar = wx.Button(panel, label="Aplicar Cambios")
        btn_aplicar.Bind(wx.EVT_BUTTON, self.on_apply_changes)

        # Agregar elementos al layout
        vbox.Add(lbl_referencias, flag=wx.ALL, border=10)
        vbox.Add(self.txt_referencias, flag=wx.ALL | wx.EXPAND, border=10)
        vbox.Add(lbl_expansion, flag=wx.ALL, border=10)
        vbox.Add(self.txt_expansion, flag=wx.ALL, border=10)
        vbox.Add(btn_aplicar, flag=wx.ALL | wx.ALIGN_CENTER, border=10)

        panel.SetSizer(vbox)

    def on_apply_changes(self, event):
        # Obtener las referencias y el valor de expansión
        referencias = self.txt_referencias.GetValue().split(",")
        referencias = [ref.strip() for ref in referencias if ref.strip()]  # Limpiar espacios
        try:
            nuevo_valor = float(self.txt_expansion.GetValue())
        except ValueError:
            wx.MessageBox("Por favor, ingresa un valor numérico válido para la expansión.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Aplicar los cambios al diseño
        if referencias:
            self.modify_solder_mask(referencias, nuevo_valor)
        else:
            wx.MessageBox("Por favor, ingresa al menos una referencia de componente.", "Error", wx.OK | wx.ICON_ERROR)

    def modify_solder_mask(self, referencias, nuevo_valor):
        # Convertir el valor de expansión a nanómetros
        nuevo_valor_nm = pcbnew.FromMM(nuevo_valor)

        # Cargar el diseño
        tablero = pcbnew.GetBoard()

        for ref in referencias:
            componente = tablero.FindFootprintByReference(ref)
            if componente is None:
                wx.MessageBox(f"Advertencia: No se encontró el componente '{ref}' en el diseño.", "Advertencia", wx.OK | wx.ICON_WARNING)
                continue

            # Modificar la expansión de los pines
            for pad in componente.Pads():
                pad.SetLocalSolderMaskMargin(nuevo_valor_nm)

        # Actualizar el diseño en la vista
        pcbnew.Refresh()
        wx.MessageBox("Cambios aplicados correctamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)


# Registrar el plugin
SolderMaskModifierPlugin().register()
