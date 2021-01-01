import argparse
import twitch
import pandas as pd
import numpy as np
import re
import neologdn
import emoji
import os

class GetClass():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('client_id', help='clien-id')
        self.parser.add_argument('client_secret_id', help='clien-secret-id')
        self.parser.add_argument('video_id', help='video-id')
        self.comments, self.emoticons = self.get_comment()
        self.df = self.preprocessing()
        self.export_df()
    
    def get_comment(self):
        args = self.parser.parse_args()
        helix = twitch.Helix(args.client_id, args.client_secret_id)
        comments, emoticons = [], []

        for comment in helix.video(args.video_id).comments:
            for i in range(len(comment.message.fragments)):
                # get comment
                if comment.message.fragments[i].text != "":
                    comments.append(comment.message.fragments[i].text)
                else:
                    # TODO: Not work
                    comments.append(None)
                
                # get emoticon id
                if comment.message.fragments[i].emoticon is not None:
                    emoticons.append(comment.message.fragments[i].emoticon.emoticon_id)
                else:
                    emoticons.append("No_id")
        
        return comments, emoticons
    
    def preprocessing(self):
        df = pd.DataFrame({"comment": self.comments, "emoticon_id": self.emoticons})
        
        tmp = []
        for line in df["comment"]:
            line = neologdn.normalize(line)
            line = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', line)
            line = re.sub(r'[!-/:-@[-`{-~]', r' ', line)
            line = re.sub(r'\d+', '0', line)
            line = ''.join(['' if c in emoji.UNICODE_EMOJI else c for c in line])
            tmp.append(line)

        df["comment"] = tmp
        del tmp
        df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
        df.dropna(inplace=True)
        return df

    def export_df(self):
        os.makedirs('./data', exist_ok=True)
        self.df.to_csv('./data/comment_data.csv', index=False)

if __name__ == '__main__':
    GetClass()