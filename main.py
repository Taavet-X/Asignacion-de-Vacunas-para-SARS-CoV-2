import model
from Views.Gui import Gui
# gui.create_gui(model.main())
#model.init_solver()
Gui(model.load_info("info.txt"), model.load_restric("restricciones.txt"))
