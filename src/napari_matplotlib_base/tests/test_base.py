from napari_matplotlib import NapariMPLWidget


def test_base_widget(make_napari_viewer):
    # Smoke test adding the base widget
    viewer = make_napari_viewer()
    widget = NapariMPLWidget()
    viewer.add_dock_widget(widget)
