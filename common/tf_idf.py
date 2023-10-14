# coding = utf-8
# pip install scikit-learn
# pip install beautifulsoup4
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
import warnings
import re
warnings.filterwarnings('ignore')

stop_words = []
with open('common/stopword.txt', 'r') as f:
    while True:
        word = f.readline().strip()
        if word:
            stop_words.append(word)
        else: 
            break

def get_tf_idf_sort_list(html_str):
    try:
        soup = BeautifulSoup(html_str, 'html.parser')
        text = soup.get_text()
        text = re.sub(r'\d', ' ', text)
        res_list = []

        vectorizer = TfidfVectorizer(stop_words=stop_words)
        tfidf = vectorizer.fit_transform([text])

        feature_names = vectorizer.get_feature_names_out()
        tfidf_values = tfidf.toarray()[0]

        sorted_indices = sorted(range(len(tfidf_values)), key=lambda i: tfidf_values[i], reverse=True)

        return_num = 5
        for index in sorted_indices:
            if return_num <= 0:
                break
            return_num -= 1
            feature_name = feature_names[index]
            tfidf_value = tfidf_values[index]
            res_list.append((feature_name, tfidf_value))
            # print(feature_name, tfidf_value)
        return res_list
    except Exception as e:
        e_info = f"exception, {e.__traceback__.tb_frame.f_globals['__file__']}, line: {e.__traceback__.tb_lineno}\n{str(e)}\n"
        if 'perhaps the documents only contain stop words' not in e_info:
            print(e_info)
        return None