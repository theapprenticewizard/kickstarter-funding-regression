import pandas as pd

'''
Step 1: extract the training data
'''

training_df = pd.read_csv('../ks-projects-201612.csv', encoding='cp437')
print(training_df.columns.values)
print(training_df.shape)
print(training_df.head())

test_df = pd.read_csv('../ks-projects-201801.csv')
print(test_df.columns.values)
print(test_df.shape)
print(test_df.head())

y_training = training_df['pledged ']
print(y_training.values)

# print("Average amount pledged in usd: " + "${:,.2f}".format(y_training.mean()))

y_test = test_df['usd pledged']
print("Average amount pledged in usd: " + "${:,.2f}".format(y_test.mean()))

'''
Step 2: comine training and test df
'''
