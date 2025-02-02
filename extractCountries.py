import pandas as pd
import re

news_file = 'news_excerpts_parsed.xlsx'
wikileaks_file = 'wikileaks_parsed.xlsx'
news_data = pd.read_excel(news_file)
wikileaks_data = pd.read_excel(wikileaks_file)

country_dict = {
    "Afghanistan": "AFG", "Albania": "ALB", "Algeria": "DZA", "Andorra": "AND", "Angola": "AGO", "Argentina": "ARG",
    "Armenia": "ARM", "Australia": "AUS", "Austria": "AUT", "Azerbaijan": "AZE", "Bahamas": "BHS", "Bahrain": "BHR",
    "Bangladesh": "BGD", "Barbados": "BRB", "Belarus": "BLR", "Belgium": "BEL", "Belize": "BLZ", "Benin": "BEN",
    "Bhutan": "BTN", "Bolivia": "BOL", "Botswana": "BWA", "Brazil": "BRA", "Brunei": "BRN", "Bulgaria": "BGR",
    "Burkina Faso": "BFA", "Burundi": "BDI", "Cambodia": "KHM", "Cameroon": "CMR", "Canada": "CAN",
    "Central African Republic": "CAF", "Chad": "TCD", "Chile": "CHL", "China": "CHN", "Colombia": "COL",
    "Comoros": "COM", "Congo": "COG", "Costa Rica": "CRI", "Croatia": "HRV", "Cuba": "CUB", "Cyprus": "CYP",
    "Czech Republic": "CZE", "Denmark": "DNK", "Djibouti": "DJI", "Dominica": "DMA", "Dominican Republic": "DOM",
    "Ecuador": "ECU", "Egypt": "EGY", "El Salvador": "SLV", "Equatorial Guinea": "GNQ", "Eritrea": "ERI",
    "Estonia": "EST", "Eswatini": "SWZ", "Ethiopia": "ETH", "Fiji": "FJI", "Finland": "FIN", "France": "FRA",
    "Gabon": "GAB", "Gambia": "GMB", "Georgia": "GEO", "Germany": "DEU", "Ghana": "GHA", "Greece": "GRC",
    "Grenada": "GRD", "Guatemala": "GTM", "Guinea": "GIN", "Guinea-Bissau": "GNB", "Guyana": "GUY",
    "Haiti": "HTI", "Honduras": "HND", "Hungary": "HUN", "Iceland": "ISL", "India": "IND", "Indonesia": "IDN",
    "Iran": "IRN", "Iraq": "IRQ", "Ireland": "IRL", "Israel": "ISR", "Italy": "ITA", "Jamaica": "JAM",
    "Japan": "JPN", "Jordan": "JOR", "Kazakhstan": "KAZ", "Kenya": "KEN", "Kiribati": "KIR", "Kuwait": "KWT",
    "Kyrgyzstan": "KGZ", "Laos": "LAO", "Latvia": "LVA", "Lebanon": "LBN", "Lesotho": "LSO", "Liberia": "LBR",
    "Libya": "LBY", "Liechtenstein": "LIE", "Lithuania": "LTU", "Luxembourg": "LUX", "Madagascar": "MDG",
    "Malawi": "MWI", "Malaysia": "MYS", "Maldives": "MDV", "Mali": "MLI", "Malta": "MLT", "Marshall Islands": "MHL",
    "Mauritania": "MRT", "Mauritius": "MUS", "Mexico": "MEX", "Micronesia": "FSM", "Moldova": "MDA",
    "Monaco": "MCO", "Mongolia": "MNG", "Montenegro": "MNE", "Morocco": "MAR", "Mozambique": "MOZ",
    "Myanmar": "MMR", "Namibia": "NAM", "Nauru": "NRU", "Nepal": "NPL", "Netherlands": "NLD",
    "New Zealand": "NZL", "Nicaragua": "NIC", "Niger": "NER", "Nigeria": "NGA", "North Korea": "PRK",
    "North Macedonia": "MKD", "Norway": "NOR", "Oman": "OMN", "Pakistan": "PAK", "Palau": "PLW",
    "Panama": "PAN", "Papua New Guinea": "PNG", "Paraguay": "PRY", "Peru": "PER", "Philippines": "PHL",
    "Poland": "POL", "Portugal": "PRT", "Qatar": "QAT", "Romania": "ROU", "Russia": "RUS", "Rwanda": "RWA",
    "Singapore": "SGP", "South Africa": "ZAF", "Spain": "ESP", "Sweden": "SWE", "Switzerland": "CHE",
    "United Kingdom": "GBR", "United States": "USA"
}

countries_set = set(country_dict.keys())

def extract_countries(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))  
    words = text.split()
    found_countries = sorted(set(word for word in words if word in countries_set))
    return [f"{country} ({country_dict[country]})" for country in found_countries] if found_countries else None

news_data["Identified_Countries"] = news_data["Text"].apply(extract_countries)
wikileaks_data["Identified_Countries"] = wikileaks_data["Text"].apply(extract_countries)

news_data = news_data.dropna(subset=["Identified_Countries"])
wikileaks_data = wikileaks_data.dropna(subset=["Identified_Countries"])

news_expanded = news_data.explode("Identified_Countries").reset_index()[["index", "Identified_Countries"]]
wikileaks_expanded = wikileaks_data.explode("Identified_Countries").reset_index()[["index", "Identified_Countries"]]

news_expanded.rename(columns={"index": "Article_Index"}, inplace=True)
wikileaks_expanded.rename(columns={"index": "Article_Index"}, inplace=True)

news_expanded.to_excel("news_identified_countries.xlsx", index=False)
wikileaks_expanded.to_excel("wikileaks_identified_countries.xlsx", index=False)

print("Country matches saved with each country in a separate row but same article index.")
