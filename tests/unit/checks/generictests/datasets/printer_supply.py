# yapf: disable


checkname = 'printer_supply'


info = [['Toner Cartridge OKI DATA CORP', '100', '30', 'class', 'black'],
        ['Toner Cartridge OKI DATA CORP', '100', '10', 'class', 'cyan'],
        ['Toner Cartridge OKI DATA CORP', '100', '10', 'class', 'magenta'],
        ['Toner Cartridge OKI DATA CORP', '100', '40', 'class', 'yellow'],
        ['Image Drum Unit OKI DATA CORP', '20000', '409', 'class', ''],
        ['Image Drum Unit OKI DATA CORP', '20000', '7969', 'class', ''],
        ['Image Drum Unit OKI DATA CORP', '20000', '11597', 'class', ''],
        ['Image Drum Unit OKI DATA CORP', '20000', '4621', 'class', ''],
        ['Belt Unit OKI DATA CORP', '60000', '47371', 'class', ''],
        ['Fuser Unit OKI DATA CORP', '60000', '26174', 'class', ''],
        ['Waste Toner box OKI DATA CORP', '1', '-2', 'class', '']]


discovery = {'': [('Belt Unit OKI DATA CORP', {}),
                  ('Black Image Drum Unit OKI DATA CORP', {}),
                  ('Black Toner Cartridge OKI DATA CORP', {}),
                  ('Cyan Image Drum Unit OKI DATA CORP', {}),
                  ('Cyan Toner Cartridge OKI DATA CORP', {}),
                  ('Fuser Unit OKI DATA CORP', {}),
                  ('Magenta Image Drum Unit OKI DATA CORP', {}),
                  ('Magenta Toner Cartridge OKI DATA CORP', {}),
                  ('Waste Toner box OKI DATA CORP', {}),
                  ('Yellow Image Drum Unit OKI DATA CORP', {}),
                  ('Yellow Toner Cartridge OKI DATA CORP', {})]}


checks = {'': [('Belt Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0,
                  'Remaining: 79%',
                  [('pages', 47371, 12000.0, 6000.0, 0, 60000)])]),
               ('Black Image Drum Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(2,
                  'Remaining: 2% (warn/crit at 20%/10%)',
                  [('pages', 409, 4000.0, 2000.0, 0, 20000)])]),
               ('Black Toner Cartridge OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0, 'Remaining: 30%', [('pages', 30, 20.0, 10.0, 0, 100)])]),
               ('Cyan Image Drum Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0, 'Remaining: 40%', [('pages', 7969, 4000.0, 2000.0, 0, 20000)])]),
               ('Cyan Toner Cartridge OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(2,
                  'Remaining: 10% (warn/crit at 20%/10%)',
                  [('pages', 10, 20.0, 10.0, 0, 100)])]),
               ('Fuser Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0,
                  'Remaining: 44%',
                  [('pages', 26174, 12000.0, 6000.0, 0, 60000)])]),
               ('Magenta Image Drum Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0, 'Remaining: 58%', [('pages', 11597, 4000.0, 2000.0, 0, 20000)])]),
               ('Magenta Toner Cartridge OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(2,
                  'Remaining: 10% (warn/crit at 20%/10%)',
                  [('pages', 10, 20.0, 10.0, 0, 100)])]),
               ('Waste Toner box OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(3, ' Unknown level', [])]),
               ('Yellow Image Drum Unit OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0, 'Remaining: 23%', [('pages', 4621, 4000.0, 2000.0, 0, 20000)])]),
               ('Yellow Toner Cartridge OKI DATA CORP',
                {'levels': (20.0, 10.0)},
                [(0, 'Remaining: 40%', [('pages', 40, 20.0, 10.0, 0, 100)])])]}