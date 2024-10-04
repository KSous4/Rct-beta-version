
class ImageGetter:

    def __init__(self) -> None:
       pass

    con_parser_crz = {
            '01':'apsp',
            '02':'alsp',
            '03':'aflp',
            '04':'arbp',
            '05':'afdp',
            '06':'vptp'
        }
    
    @staticmethod
    def parse_link(id: str) -> dict:
                 
        con = ImageGetter.con_parser_crz.get(id[:3])
        if id [3:5] == '51':
            praca = f'{id[3:5]}s'
        else:
            praca = id[3:5]


        options ={'opt1':f'https://imagens.arteris.com.br/Pictures/{id[9:17]}/{id[:9]}/020102SAU202410031004008790-F01.jpg',
                  'opt2':f'https://{con}{praca}.arteris.com.br/Pictures/{id[9:17]}/{id[:9]}/010116NAU202410032025060700-F01.jpg'}
        

        
        return options
