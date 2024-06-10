import os
from dotenv import load_dotenv
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

load_dotenv()
nltk.download('stopwords')

##fonction 1

def connect_to_google_sheets(spreadsheet_name):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        json_keyfile_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
        client = gspread.authorize(credentials)

        spreadsheet = client.open(spreadsheet_name)
        
        return spreadsheet
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Feuille de calcul '{spreadsheet_name}' non trouvée.")
        raise
    except ValueError as e:
        print(e)
        raise

## fonction 2

def pre_processing(txt):
    txt = txt.lower()
    txt = re.sub(r'[^\w\s]', '', txt)
    txt = re.sub(r'\d+', '', txt)
    stop_words = set(stopwords.words('french'))
    txt = ' '.join([word for word in txt.split() if word not in stop_words])
    txt = txt.strip()

    return txt

def generate_ngrams(txt,n):
    words = txt.split()
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    return ngrams

def analyze_ngrams(data, n,top_n=10):
    bigrams = []
    for text in data['texte_preprocessed']:
        bigrams.extend(generate_ngrams(text, n))
    ngrams_freq = Counter(bigrams)

    most_common_ngrams = ngrams_freq.most_common(top_n)

    print(f"Les {top_n} {n}-grams les plus fréquents sont :")
    for ngram, count in most_common_ngrams:
        print(f"{ngram} : {count}")

    ngrams, counts = zip(*most_common_ngrams)

    plt.figure(figsize=(12, 6))
    plt.bar(ngrams, counts,width = 0.4)
    plt.xlabel(f'{n}-grams', fontsize=14)
    plt.ylabel('Fréquence', fontsize=14)
    plt.xticks(rotation=45)
    plt.title(f'Top {top_n} {n}-grams les plus fréquents', fontsize=16)
    plt.tight_layout()
    plt.show()

    text = ' '.join(ngrams)
    wordcloud = WordCloud(background_color='white', width=800, height=400).generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f'Nuage de mots des {top_n} {n}-grams les plus fréquents', fontsize=16)
    plt.show()

    return most_common_ngrams

## fonction 3

def dataframe_to_sheet(spreadsheet_name,sheet_name,df):
    try:
        spreadsheet = connect_to_google_sheets(spreadsheet_name)
        sheet = spreadsheet.worksheet(sheet_name)
            
        sheet.clear()
        data = [df.columns.values.tolist()] + df.values.tolist()

        sheet.update(range_name='A1',values= data)
        print("Les données ont été mises à jour avec succès dans Google Sheets.")

    except gspread.exceptions.WorksheetNotFound:
        print(f"Feuille '{sheet_name}' non trouvée.")
        raise
    except Exception as e:
        print(f"Erreur lors de la mise à jour des données : {e}")
        raise




def example1(spreadsheet_name,sheet_name):
    data = pd.read_csv('data/data_science_phrases.csv')
    data['texte_preprocessed'] = data['texte'].apply(pre_processing)
    most_common_ngrams=analyze_ngrams(data,2,15)
    df = pd.DataFrame(most_common_ngrams, columns=['Ngrams', 'Fréquence'])
    dataframe_to_sheet(spreadsheet_name,sheet_name,df)

def example2(spreadsheet_name,sheet_name):
    data = pd.read_csv('data/news_headline.csv')
    data['texte_preprocessed'] = data['texte'].apply(pre_processing)

    df_positive_sentiment = data[data['sentiment']=="positive"]
    df_negative_sentiment = data[data['sentiment']=="negative"]
    df_neutral_sentiment = data[data['sentiment']=="neutral"]

    most_common_ngrams_positive=analyze_ngrams(df_positive_sentiment,2,15)
    most_common_ngrams_positive = pd.DataFrame(most_common_ngrams_positive,columns=['Ngrams 1', 'Fréquence dans les titres positifs'])

    most_common_ngrams_negative=analyze_ngrams(df_negative_sentiment,2,15)
    most_common_ngrams_negative = pd.DataFrame(most_common_ngrams_negative,columns=['Ngrams 2', 'Fréquence dans les titres négatifs'])

    most_common_ngrams_neutral=analyze_ngrams(df_neutral_sentiment,2,15)
    most_common_ngrams_neutral = pd.DataFrame(most_common_ngrams_neutral,columns=['Ngrams 3', 'Fréquence dans les titres neutres'])

    merged_df = pd.concat([most_common_ngrams_positive, most_common_ngrams_negative, most_common_ngrams_neutral], axis=1)

    dataframe_to_sheet(spreadsheet_name,sheet_name,merged_df)


   

example1("data_science_phrases","Sheet1")
#example2("data_science_phrases","Sheet1")