# International Morse Code dictionary "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 , . ? / - ( ) ' " & ; _ + = @"
INTERNATIONAL_MORSE_CODE_DICT = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    # Numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    # Symbols
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', "'": '.----.', '"': '.-..-.', '&': '.-...', ';': '-.-.-.', 
    '_': '..--.-', '+': '.-.-.', '=': '-...-', '@': '.--.-.'
}

# American Morse Code dictionary "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 , . ? / - ( ) ' " & ; _ + = @"
AMERICAN_MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '.. .', 'D': '-..', 'E': '.', 
    'F': '.-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '-.-.', 
    'K': '-.-', 'L': '...', 'M': '--', 'N': '-.', 'O': '. .', 
    'P': '.....', 'Q': '..-.', 'R': '. . .', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '.-..', 'Y': '.. ..', 
    'Z': '... .',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    
    '.': '.. ..', ',': '.-.-', ':': '---...', ';': '-.-.-.', 
    '?': '.. .. ..', '!': '-.-.--', '-': '-....-', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', '=': '-...-', 
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-', 
    '@': '.--.-.', "'": '.----.'
}

# Wabun Morse Code dictionary
WABUN_MORSE_CODE_DICT = {
    # Katakana
    'ア': '.-',  'イ': '..',   'ウ': '..-',  'エ': '.-..-', 'オ': '.-..',  
    'カ': '-.-..', 'キ': '-.-..-', 'ク': '...-',  'ケ': '-.--', 'コ': '----',  
    'サ': '-.-.-', 'シ': '--.-.', 'ス': '---.-', 'セ': '.---', 'ソ': '---.',  
    'タ': '-.',  'チ': '..-.', 'ツ': '.--.', 'テ': '.-.--', 'ト': '..-..',  
    'ナ': '.-.',  'ニ': '-.-.', 'ヌ': '....', 'ネ': '--.-', 'ノ': '..--',  
    'ハ': '-...', 'ヒ': '--..-', 'フ': '--..', 'ヘ': '.-..', 'ホ': '-..',  
    'マ': '-..-', 'ミ': '..-.-', 'ム': '-',    'メ': '-...-', 'モ': '-..-.',  
    'ヤ': '.--',  'ユ': '-..--', 'ヨ': '--',  
    'ラ': '...',  'リ': '--.',  'ル': '-.--.', 'レ': '---',  'ロ': '.-.-',  
    'ワ': '-.-',  'ヲ': '.---', 'ン': '.-.-.',  
    'ガ': '-.-.. ..', 'ギ': '-.-..- ..', 'グ': '...- ..', 'ゲ': '-.-- ..', 'ゴ': '---- ..',  
    'ザ': '-.-.- ..', 'ジ': '--.-. ..', 'ズ': '---.- ..', 'ゼ': '.--- ..', 'ゾ': '---. ..',  
    'ダ': '-. ..', 'ヂ': '..-. ..', 'ヅ': '.--. ..', 'デ': '.-.-- ..', 'ド': '..-.. ..',  
    'バ': '-... ..', 'ビ': '--..- ..', 'ブ': '--.. ..', 'ベ': '.-.. ..', 'ボ': '-.. ..',  
    'パ': '-... -.', 'ピ': '--..- -.', 'プ': '--.. -.', 'ペ': '.-.. -.', 'ポ': '-.. -.',  

    # Small Tsu (Silent but doubles next consonant)
    'ッ': '',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',  
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',  

    # Symbols
    '。': '.-.-',  # Japanese period
    '、': '--..--',  # Japanese comma
    '.': '.-.-.-', ',': '--..--', ':': '---...', ';': '-.-.-.',  
    '?': '..--..', '!': '-.-.--', '-': '-....-', '/': '-..-.',  
    '(': '-.--.', ')': '-.--.-', '&': '.-...', '=': '-...-',  
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',  
    '@': '.--.-.', "'": '.----.'  
}
