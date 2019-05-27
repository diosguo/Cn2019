import pandas as pd


def pre():
    with open('data/train_old.csv','r') as f:
        with open('data/train.csv','w') as fo:
            for line in f:
                line.replace('\r','')
                fo.write(line)
pre()


# test_df = pd.read_csv('data/20190527_test.csv')
# train_df = pd.read_csv('data/train.csv')
# train_df = train_df.dropna()
# print(train_df.info())