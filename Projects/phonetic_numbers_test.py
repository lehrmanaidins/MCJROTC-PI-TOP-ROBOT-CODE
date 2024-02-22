
'''
    Phonetic Numbers Test
    
    File: phonetic_numbers_test.py
    Author: Aidin Lehrman
    Version: 02-21-2024 20:21
'''

def main() -> None:
    nums_str: list[str] = [
        'Zero',
        'Wun',
        'Too',
        'Tree',
        'Fower',
        'Fife',
        'Six',
        'Seven',
        'Ait',
        'Niner',
    ]
    nums_int: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print('+-----------+-------------+')
    print('|  Numeral  |  Spoken As  |')
    print('+-----------+-------------+')
    
    for i in range(10):
        print(f'|  {nums_int[i]:^7}  |  {nums_str[i]:^9}  |')
    
    print('+-----------+-------------+')
    
if __name__ == '__main__':
    main()