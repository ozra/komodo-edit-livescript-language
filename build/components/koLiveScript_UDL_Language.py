# Registers the LiveScript language in Komodo.

import logging
from koUDLLanguageBase import KoUDLLanguage

log = logging.getLogger("koLiveScriptLanguage")
#log.setLevel(logging.DEBUG)

def registerLanguage(registry):
    log.debug("Registering language LiveScript")
    registry.registerLanguage(KoLiveScriptLanguage())

class KoLiveScriptLanguage(KoUDLLanguage):

    # ------------ Komodo Registration Information ------------ #

    name = "LiveScript"
    lexresLangName = "LiveScript"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_categories_ = [("komodo-language", name)]
    _reg_clsid_ = "35bceda0-a65d-41c6-964e-30cabae779a4"
    defaultExtension = '.ls'

    # ------------ Commenting Controls ------------ #

    commentDelimiterInfo = {
        "line": [
                '#'    # Hash-style one line comments
                ],
        "block": [
                ('/*', '*/')   # C-style block comments
                ],
    }

    # ------------ Indentation Controls ------------ #

    # To support automatic indenting and dedenting after "{([" and "})]"
    supportsSmartIndent = "python"
    # Other smart indenting types are:
    #   'text', 'python', 'XML' and 'keyword'

    # Indent/dedent after these words.
    _indenting_statements = ['case', '->', '!->', '~>', '!~>', 'if', 'for', 'while']
    _dedenting_statements = ['return', 'break', 'continue']

    # ------------ Sub-language Controls ------------ #

    #Check: Update 'lang_from_udl_family' as appropriate for your
    #      lexer definition. There are four UDL language families:
    #           M (markup), i.e. HTML or XML
    #           CSL (client-side language), e.g. JavaScript
    #           SSL (server-side language), e.g. Perl, PHP, Python
    #           TPL (template language), e.g. RHTML, Django, Smarty
    #      'lang_from_udl_family' maps each UDL family code (M,
    #      CSL, ...) to the sub-language name in your language.
    #      Some examples:
    #        lang_from_udl_family = {   # A PHP file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'PHP',           #   PHP
    #           'CSL': 'JavaScript',    #   JavaScript
    #        }
    #        lang_from_udl_family = {   # An RHTML file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'Ruby',          #   Ruby
    #           'CSL': 'JavaScript',    #   JavaScript
    #           'TPL': 'RHTML',         #   RHTML template code
    #        }
    #        lang_from_udl_family = {   # A plain XML can just contain
    #           'M': 'XML',             #   XML
    #        }
    lang_from_udl_family = {'SSL': 'LiveScript'}
