import pandas as pd
import re
import spacy

news_file = 'news_excerpts_parsed.xlsx'
wikileaks_file = 'wikileaks_parsed.xlsx'
news_data = pd.read_excel(news_file)
wikileaks_data = pd.read_excel(wikileaks_file)

stop_words = set([
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", 
    "has", "he", "in", "is", "it", "its", "of", "on", "that", 
    "the", "to", "was", "were", "will", "with", "this", "which", 
    "or", "but", "if", "while", "then", "up", "out", "over", "just"
])

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text)).lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

news_data['Cleaned_Text'] = news_data['Text'].apply(clean_text)
wikileaks_data['Cleaned_Text'] = wikileaks_data['Text'].apply(clean_text)

nlp = spacy.load("en_core_web_sm")

def extract_specific_entities(text, entity_type):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_type]
    return entities

def remove_duplicate_entities(entities):
    normalized = {entity.replace(" ", "").lower(): entity for entity in entities}
    return list(normalized.values())

news_data['Persons'] = news_data['Cleaned_Text'].apply(lambda x: remove_duplicate_entities(extract_specific_entities(x, 'PERSON')))
news_data['Organizations'] = news_data['Cleaned_Text'].apply(lambda x: remove_duplicate_entities(extract_specific_entities(x, 'ORG')))

wikileaks_data['Persons'] = wikileaks_data['Cleaned_Text'].apply(lambda x: remove_duplicate_entities(extract_specific_entities(x, 'PERSON')))
wikileaks_data['Organizations'] = wikileaks_data['Cleaned_Text'].apply(lambda x: remove_duplicate_entities(extract_specific_entities(x, 'ORG')))

def expand_entities(data, entity_column):
    expanded_df = data[[entity_column]].explode(entity_column).dropna().reset_index()
    expanded_df.rename(columns={'index': 'Article_Index', entity_column: 'Entity'}, inplace=True)
    return expanded_df

news_persons_expanded = expand_entities(news_data, 'Persons')
news_orgs_expanded = expand_entities(news_data, 'Organizations')

wikileaks_persons_expanded = expand_entities(wikileaks_data, 'Persons')
wikileaks_orgs_expanded = expand_entities(wikileaks_data, 'Organizations')

news_persons_expanded.to_excel("news_extracted_persons.xlsx", index=False)
news_orgs_expanded.to_excel("news_extracted_organizations.xlsx", index=False)

wikileaks_persons_expanded.to_excel("wikileaks_extracted_persons.xlsx", index=False)
wikileaks_orgs_expanded.to_excel("wikileaks_extracted_organizations.xlsx", index=False)

print("Persons and Organizations extracted and saved in separate Excel files.")
