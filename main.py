
import rdzen
from rdzen.szufladka import Szufladka
from rdzen.wstrzykiwacz_zaleznosci.kontener_wstrzykiwania import WstrzykiwaczZaleznosci


def main():
    wstrzykiwacz_zaleznosci = WstrzykiwaczZaleznosci()
    wstrzykiwacz_zaleznosci.wire(modules=[rdzen.szufladka])
    app = Szufladka()
    app.uruchom()


if __name__ == '__main__':
    main()
