# mypy: disable-error-code="valid-type, name-defined, no-redef, assignment, misc, override"

from ..port_v2.as_string import as_string as as_string
from ..port_v2.proxy_base import ProxyBase as ProxyBase
from .indenter import write_code as write_code
from .misc import Literal as Literal, moduleMember as moduleMember
from _typeshed import Incomplete

i18n_strings: Incomplete
i18n_context: str

def i18n_print(string) -> None: ...
def i18n_void_func(name): ...
def i18n_func(name): ...
def strict_getattr(module, clsname): ...

class i18n_string:
    string: Incomplete
    disambig: Incomplete
    def __init__(self, string, disambig) -> None: ...
    def __str__(self) -> str: ...

AS_ARGUMENT: int
AS_SIGNAL: int

class ProxyClassMember:
    proxy: Incomplete
    function_name: Incomplete
    flags: Incomplete
    def __init__(self, proxy, function_name, flags) -> None: ...
    def __str__(self) -> str: ...
    def __call__(self, *args): ...
    def __getattribute__(self, attribute): ...
    def __getitem__(self, idx): ...

class ProxySignalWithArguments:
    _sender: Incomplete
    _signal_name: Incomplete
    _signal_index: Incomplete
    def __init__(self, sender, signal_name, signal_index) -> None: ...
    def connect(self, slot) -> None: ...

class ProxyClass(ProxyBase):
    flags: int
    _uic_name: Incomplete
    def __init__(self, objectname, is_attribute, args=(), noInstantiation: bool = False) -> None: ...
    def __str__(self) -> str: ...
    def __getattribute__(self, attribute): ...

class LiteralProxyClass(ProxyClass):
    flags = AS_ARGUMENT
    _uic_name: Incomplete
    def __init__(self, *args) -> None: ...

class ProxyNamespace(ProxyBase): ...

class QtCore(ProxyNamespace):
    class Qt(ProxyNamespace): ...
    class QMetaObject(ProxyClass):
        @classmethod
        def connectSlotsByName(cls, *args) -> None: ...
    class QObject(ProxyClass):
        flags = AS_SIGNAL
        def metaObject(self): ...
        def objectName(self): ...

class QtGui(ProxyNamespace):
    class QIcon(ProxyClass):
        class fromTheme(ProxyClass): ...
    class QConicalGradient(ProxyClass): ...
    class QLinearGradient(ProxyClass): ...
    class QRadialGradient(ProxyClass): ...
    class QBrush(ProxyClass): ...
    class QPainter(ProxyClass): ...
    class QPalette(ProxyClass): ...
    class QFont(ProxyClass): ...
    class QFontDatabase(ProxyClass): ...

_qwidgets: Incomplete

class QtWidgets(ProxyNamespace):
    class QApplication(QtCore.QObject):
        @staticmethod
        def translate(uiname, text, disambig): ...
    class QSpacerItem(ProxyClass): ...
    class QSizePolicy(ProxyClass): ...
    class QAction(QtCore.QObject): ...
    class QActionGroup(QtCore.QObject): ...
    class QButtonGroup(QtCore.QObject): ...
    class QLayout(QtCore.QObject): ...
    class QGridLayout(QLayout): ...
    class QBoxLayout(QLayout): ...
    class QHBoxLayout(QBoxLayout): ...
    class QVBoxLayout(QBoxLayout): ...
    class QFormLayout(QLayout): ...
    class QWidget(QtCore.QObject):
        def font(self): ...
        def minimumSizeHint(self): ...
        def sizePolicy(self): ...
    class QDialog(QWidget): ...
    class QColorDialog(QDialog): ...
    class QFileDialog(QDialog): ...
    class QFontDialog(QDialog): ...
    class QInputDialog(QDialog): ...
    class QMessageBox(QDialog): ...
    class QWizard(QDialog): ...
    class QAbstractSlider(QWidget): ...
    class QDial(QAbstractSlider): ...
    class QScrollBar(QAbstractSlider): ...
    class QSlider(QAbstractSlider): ...
    class QMenu(QWidget):
        def menuAction(self): ...
    class QTabWidget(QWidget):
        def addTab(self, *args) -> None: ...
        def indexOf(self, page): ...
    class QComboBox(QWidget): ...
    class QFontComboBox(QComboBox): ...
    class QAbstractSpinBox(QWidget): ...
    class QDoubleSpinBox(QAbstractSpinBox): ...
    class QSpinBox(QAbstractSpinBox): ...
    class QDateTimeEdit(QAbstractSpinBox): ...
    class QDateEdit(QDateTimeEdit): ...
    class QTimeEdit(QDateTimeEdit): ...
    class QFrame(QWidget): ...
    class QLabel(QFrame): ...
    class QLCDNumber(QFrame): ...
    class QSplitter(QFrame): ...
    class QStackedWidget(QFrame): ...
    class QToolBox(QFrame):
        def addItem(self, *args) -> None: ...
        def indexOf(self, page): ...
        def layout(self): ...
    class QAbstractScrollArea(QFrame):
        def viewport(self): ...
    class QGraphicsView(QAbstractScrollArea): ...
    class QMdiArea(QAbstractScrollArea): ...
    class QPlainTextEdit(QAbstractScrollArea): ...
    class QScrollArea(QAbstractScrollArea): ...
    class QTextEdit(QAbstractScrollArea): ...
    class QTextBrowser(QTextEdit): ...
    class QAbstractItemView(QAbstractScrollArea): ...
    class QColumnView(QAbstractItemView): ...
    class QHeaderView(QAbstractItemView): ...
    class QListView(QAbstractItemView): ...
    class QTableView(QAbstractItemView):
        def horizontalHeader(self): ...
        def verticalHeader(self): ...
    class QTreeView(QAbstractItemView):
        def header(self): ...
    class QUndoView(QListView): ...
    class QListWidgetItem(ProxyClass): ...
    class QListWidget(QListView):
        setSortingEnabled: Incomplete
        isSortingEnabled: Incomplete
        item: Incomplete
    class QTableWidgetItem(ProxyClass): ...
    class QTableWidget(QTableView):
        setSortingEnabled: Incomplete
        isSortingEnabled: Incomplete
        item: Incomplete
        horizontalHeaderItem: Incomplete
        verticalHeaderItem: Incomplete
    class QTreeWidgetItem(ProxyClass):
        def child(self, index): ...
    class QTreeWidget(QTreeView):
        setSortingEnabled: Incomplete
        isSortingEnabled: Incomplete
        def headerItem(self): ...
        def topLevelItem(self, index): ...
    class QAbstractButton(QWidget): ...
    class QCheckBox(QAbstractButton): ...
    class QRadioButton(QAbstractButton): ...
    class QToolButton(QAbstractButton): ...
    class QPushButton(QAbstractButton): ...
    class QCommandLinkButton(QPushButton): ...
    class QKeySequenceEdit(QWidget): ...
