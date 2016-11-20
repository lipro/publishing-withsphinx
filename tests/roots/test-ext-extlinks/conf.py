# -*- coding: utf-8 -*-

needs_sphinx = '1.2'
needs_extensions = {'sphinx.ext.extlinks': '1.2'}
extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]

extlinks = {
    'dsarcidxf': (
        'http://datasheet.datasheetarchive.com/originals/scans/%s.pdf',
        'Datasheet Archive (IDXF): '
    ),
    'dsarcmain': (
        'http://datasheet.datasheetarchive.com/originals/distributors/%s.pdf',
        'Datasheet Archive (MAIN): '
    ),
    'hehaddrhl': (
        'https://www-user.tu-chemnitz.de/~heha/basteln/Konsumg%%C3%%BCter/DDR-Halbleiter/%s',
        'Henrik Haftmann, GDR-Semiconductor (DATA): '
    ),
    'hehaddrhlpfx': (
        'https://www-user.tu-chemnitz.de/~heha/basteln/Konsumg%%C3%%BCter/DDR-Halbleiter/#%s',
        'Henrik Haftmann, GDR-Semiconductor (LIST): '
    ),
    'rtloc': (
        'http://www.robotrontechnik.de/html/standorte/%s',
        'Robotron Technique, Locations: '
    ),
    'rtstd': (
        'http://www.robotrontechnik.de/html/standards/%s',
        'Robotron Technique, Standards: '
    ),
    'rtsw': (
        'http://www.robotrontechnik.de/html/software/%s',
        'Robotron Technique, Software: '
    ),
    'rtcpt': (
        'http://www.robotrontechnik.de/html/computer/%s',
        'Robotron Technique, Computer: '
    ),
    'rtpnt': (
        'http://www.robotrontechnik.de/html/drucker/%s',
        'Robotron Technique, Printer: '
    ),
    'rtnet': (
        'http://www.robotrontechnik.de/html/netzwerke/netzwerk.htm#%s',
        'Robotron Technique, Networks: '
    ),
    'rtk1520': (
        'http://www.robotrontechnik.de/html/komponenten/k1520pla.htm#%s',
        'Robotron Technique, K1520: '
    ),
    'rtcon': (
        'http://www.robotrontechnik.de/html/komponenten/stecker.htm#%s',
        'Robotron Technique, Connectors: '
    ),
    'rtfdd': (
        'http://www.robotrontechnik.de/html/komponenten/fs.htm#%s',
        'Robotron Technique, Floppy Disk Drives: '
    ),
    'rtemr': (
        'http://www.robotrontechnik.de/html/komponenten/emr.htm#%s',
        'Robotron Technique, The Single-Chip Microcontroller: '
    ),
    'rtic': (
        'http://www.robotrontechnik.de/html/komponenten/ic.htm#%s',
        'Robotron Technique, Integrated Circuits: '
    ),
    'rtkbd': (
        'http://www.robotrontechnik.de/html/zubehoer/tastaturen.htm#%s',
        'Robotron Technique, Keyboards: '
    ),
    'tglcate': (
        'http://www.wak-gmbh.de/index.php?id=542&tgl-nummer=%s',
        'TGL Catalog (EWN): '
    ),
    'tglbarc': (
        'https://www.bbr-server.de/bauarchivddr/archiv/tglarchiv/%s',
        'TGL Archive (BBSR): '
    ),
    'udbevglddrhl': (
        'http://www.elektron-bbs.de/elektronik/tabellen/ddr/%s.htm',
        'Udo Bertholdt, Vgl. GDR-Semiconductor: '
    ),
    'vopofetch': (
        'http://hc-ddr.hucki.net/wiki/lib/exe/fetch.php/%s',
        'Volker Pohlers, GDR-HC Download: '
    ),
    '__vopofetch': (
        'http://www.homecomputer-ddr.de.vu/wiki/lib/exe/fetch.php/%s',
        'Volker Pohlers, GDR-HC Download: '
    ),
    'vopowiki': (
        'http://hc-ddr.hucki.net/wiki/doku.php/%s',
        'Volker Pohlers, GDR-HC Wiki: '
    ),
    '__vopowiki': (
        'http://www.homecomputer-ddr.de.vu/wiki/doku.php/%s',
        'Volker Pohlers, GDR-HC Wiki: '
    ),
    'pesarnet': (
        'http://www.robotron-net.de/%s',
        'Peter Salomon, Robotron Net.: '
    ),
    'itwinfo': (
        'http://www.itwissen.info/definition/lexikon/%s',
        'German ITwissen.info: '
    ),
    'wikide': (
        'http://de.wikipedia.org/wiki/%s',
        'German Wikipedia: '
    ),
    'wikien': (
        'http://en.wikipedia.org/wiki/%s',
        'English Wikipedia: '
    ),
}
