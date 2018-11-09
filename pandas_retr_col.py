# https://blog.csdn.net/zm714981790/article/details/51304506
import pandas as pd
submissions = pd.read_csv("funding-successful-projects-on-kickstarter/train.csv")
submissions.columns = ["project_id","name","desc","goal","keywords","disable_communication","country","currency","deadline","state_changed_at","created_at","launched_at","backers_count","final_status"]
submissions = submissions.dropna()

tokenized_keywords = []
for item in submissions["currency"]:
    tokenized_keywords.append(item.split("-"))

# print(tokenized_keywords)

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for item in tokenized_keywords:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)

import numpy as np
unique_tokens = []
single_tokens = []
for tokens in clean_tokenized:
    for token in tokens:
        if token not in single_tokens:
            single_tokens.append(token)
        elif token in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)

file=open('data_currency.txt','w')
file.write(str(unique_tokens));
file.close()
# counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)
#
# for i, item in enumerate(clean_tokenized):
#     for token in item:
#         if token in unique_tokens:
#             counts.iloc[i][token] += 1
#
# print(len(unique_tokens))
#
# word_counts = counts.sum(axis=0)
# counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]
# # print(counts)
# numpy.savetxt("result.txt", counts);
