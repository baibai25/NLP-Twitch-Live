import argparse, os
from polyglot.detect import Detector
import pandas as pd
import matplotlib.pyplot as plt

class Lang_Detector():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('data', help='Dataset path')
        self.df = self.load_data()
        self.detect_lang()
    
    def load_data(self):
        args = self.parser.parse_args()
        df = pd.read_csv(args.data)
        return df

    def detect_lang(self):
        comment_df = self.df[self.df['emoticon_id'] == 'No_id']
        comment_df = comment_df['comment'].astype(str)

        result = []
        for line in comment_df:
            lang = Detector(line, quiet=True).language.code
            result.append([line, lang])
        self.save(result)
    
    def save(self, result):
        os.makedirs('./result', exist_ok=True)

        # Emotes
        emoticon_df = self.df[self.df['emoticon_id'] != 'No_id']
        plt.figure(figsize=(10, 5), dpi=100)
        plt.tight_layout()
        plt.title('Top 20 Emotes')
        emoticon_df['comment'].value_counts()[:20].plot(kind="bar")
        plt.savefig('./result/emotes.png')

        # Comments
        result_df = pd.DataFrame(result)
        plt.figure(figsize=(6, 5), dpi=100)
        plt.tight_layout()
        plt.title('Top 5 Languages')
        result_df[result_df.columns[1]].value_counts()[:5].plot(kind="bar")
        plt.savefig('./result/lang.png')

if __name__ == '__main__':
    Lang_Detector()
