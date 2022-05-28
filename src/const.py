DIR = '/content/' # work directory
PATH_TEST_DIR = DIR+'test/'
PATH_TEST_LABELS =  DIR+'test.tsv'
PATH_TRAIN_DIR =  DIR+'train/'
PATH_TRAIN_LABELS =  DIR+'train.tsv'
PREDICT_PATH = "/content/test/"
CHECKPOINT_PATH = DIR
WEIGHTS_PATH = None

ALPHABET = ['PAD', 'SOS', ' ', '!', '"', '%', '(', ')', ',', '-', '.', '/',\
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?',\
            '[', ']', '«', '»', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',\
            'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',\
            'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е',\
            'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',\
            'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',\
            'ё', 'EOS']