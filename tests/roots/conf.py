# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../samples'))
sys.path.insert(0, os.path.abspath('../samples/an_example_pypi_project'))

os.environ["TEST_FIXTURES_ROOTS"] = os.path.abspath('.')

needs_sphinx = '1.2'
needs_extensions = {
    'publishing.withsphinx':                    '0.0',  # NOQA
    'sphinx.ext.autodoc':                       '1.2',  # NOQA
    'sphinx.ext.autosummary':                   '1.2',  # NOQA
    'sphinx.ext.coverage':                      '1.2',  # NOQA
    'sphinx.ext.extlinks':                      '1.2',  # NOQA
    'sphinx.ext.doctest':                       '1.2',  # NOQA
    'sphinx.ext.ifconfig':                      '1.2',  # NOQA
    'sphinx.ext.mathjax':                       '1.2',  # NOQA
    'sphinx.ext.todo':                          '1.2',  # NOQA
#   'sphinxarg.ext':                            '0.1',  # NOQA
#   'sphinxcontrib.ansi':                       '0.6',  # NOQA
#   'sphinxcontrib.autoprogram':                '0.1',  # NOQA
#   'sphinxcontrib.bibtex':                     '0.3',  # NOQA
    'sphinxcontrib.blockdiag':                  '1.5',  # NOQA
#   'sphinxcontrib.email':                      '0.3',  # NOQA
#   'sphinxcontrib.embedly':                    '0.2',  # NOQA
#   'sphinxcontrib.inlinesyntaxhighlight':      '0.2',  # NOQA
#   'sphinxcontrib.programoutput':              '0.8',  # NOQA
#   'sphinxcontrib.spelling':                   '2.2',  # NOQA
#   'sphinxcontrib.tikz':                       '0.4',  # NOQA
}

extensions = ['publishing.withsphinx']
master_doc = 'index'
latex_documents = [(master_doc, 'index.tex', 'project', 'author', 'manual')]
man_pages = [(master_doc, 'index', 'project', 'author', 7)]
texinfo_documents = [(master_doc, 'index', 'project', 'author', 'misc', 'description', 'miscellaneous')]
devhelp_basename = master_doc
epub_basename = master_doc
epub_title = 'project'
epub_author = 'author'
htmlhelp_basename = master_doc
qthelp_basename = master_doc

# FIXME: avoid local copy of DejaVuSans core font
blockdiag_fontpath = os.path.abspath('./_static/DejaVuSans.ttf')

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


def setup(app):
    app.add_config_value('confval1', False, None)
    app.add_config_value('confval2', False, None)
