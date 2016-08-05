import sys

from PySide.QtCore import *
from PySide.QtGui import *

sys.path.insert(0, './dataFill/')

from fill_table_class import FillTable

sys.path.insert(0, './test/model/mongodbtest2/')

from DaoMaster import DaoMaster
from DaoSession import DaoSession
from CatalogComplexType import CatalogComplexType
from CatalogComplexTypeDao import CatalogComplexTypeDao

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    catalog_complex_dao = dao_session.getCatalogComplexTypeDao()

    fill_table = FillTable()
    # fill_table.addField('Id', 'Id')
    fill_table.addField('ComplexType', 'Tipo de Complejidad')
    asdf = []
    asdf.append(catalog_complex_dao.readFirst())
    fill_table.setData(asdf)

    app = QApplication(sys.argv)
    table = QTableWidget()
    tableItem = QTableWidgetItem()

    # initiate table
    # table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.resize(400, 250)
    # table.setRowCount(4)
    # table.setColumnCount(2)

    ## set data
    # table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
    # table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
    # table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
    # table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
    # table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
    # table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
    # table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
    # table.setItem(3,1, QTableWidgetItem("Item (4,2)"))

    fill_table.setTable(table)
    fill_table.fill()

    # show table
    table.show()
    app.exec_()
