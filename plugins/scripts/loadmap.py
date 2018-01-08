from qgis.utils import iface
from qgis.gui import QgsMessageBar
import datetime
c = iface.mapCanvas()
t = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
img_path = '/tmp/map{}.png'
c.saveAsImage(img_path.format(t), None, 'PNG')
iface.messageBar().pushMessage("Header","MessageBody", QgsMessageBar.WARNING, 2)
