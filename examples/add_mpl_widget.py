import napari
from napari_matplotlib_base import NapariMPLWidget

viewer = napari.Viewer()
widget = NapariMPLWidget(viewer)

viewer.window.add_dock_widget(widget)

if __name__ == "__main__":
    napari.run()
