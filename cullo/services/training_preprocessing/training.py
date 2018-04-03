import re
import pandas as pd



def func(row):
    """
    The method takes intent as an inout and represent it in numerical form
    :param row:
    :return:
    """
    if row['intent'] == 'atis_flight' :
        return 0
    else:
        return 1


def train_data():
    """
    This method reads the text file and retrieves the required data from the text file, and returns DataFrame
    """
    msg_list = []
    intent_list = []
    with open("C:\\Users\\prabah\\PycharmProjects\\cullo\\cullo\\services\\training_preprocessing\\train_atis.txt", "r") as txt_file:
        for line in txt_file:
            found = re.search('BOS(.+?)EOS', line)
            if found:
                msg = found.group(1)
                msg_list.append(msg)

            intent_list.append(line.split()[-1])

    atis_dict = {'msg': msg_list, 'intent': intent_list}

    df = pd.DataFrame(atis_dict)

    final_df = df.loc[df['intent'].isin(['atis_flight', 'atis_airfare'])]

        # final_df['intent_value'] = intent_vector_list
    final_df['intent_value'] = final_df.apply(func, axis=1)
    return final_df
