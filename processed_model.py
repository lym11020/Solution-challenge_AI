import pandas as pd

file_path = '/mnt/data/drug_deaths.csv'
data = pd.read_csv(file_path)

data_info = data.info()
data_head = data.head()

modeling_columns = ['Sex', 'Race', 'Heroin', 'AnyOpioid', 'Fentanyl', 'Cocaine', 'Benzodiazepine', 'Ethanol', 
                    'Oxycodone', 'Methadone', 'Fentanyl_Analogue', 'Amphet', 'Tramad', 'Hydrocodone', 'Oxymorphone']
data_modeling = data[modeling_columns]

fentanyl_values = data_modeling['Fentanyl'].unique()

data_modeling['Fentanyl'] = data_modeling['Fentanyl'].apply(lambda x: 1 if x != '0' else 0)

data_modeling['Sex'].fillna('Unknown', inplace=True)
data_modeling['Race'].fillna('Unknown', inplace=True)

data_encoded = pd.get_dummies(data_modeling, columns=['Sex', 'Race'])

data_encoded.head()

output_file_path = '/mnt/data/drug_deaths_processed.csv'
data_encoded.to_csv(output_file_path, index=False)

output_file_path

processed_file_path = '/mnt/data/drug_deaths_processed.csv'
data_processed = pd.read_csv(processed_file_path)

data_processed.head()

data_processed['AnyOpioid'] = pd.to_numeric(data_processed['AnyOpioid'], errors='coerce').fillna(0).astype(int)

drug_columns = ['Heroin', 'AnyOpioid', 'Fentanyl', 'Cocaine', 'Benzodiazepine', 'Ethanol', 
                'Oxycodone', 'Methadone', 'Fentanyl_Analogue', 'Amphet', 'Tramad', 'Hydrocodone', 'Oxymorphone']
data_processed['TotalDrugsUsed'] = data_processed[drug_columns].sum(axis=1)


def assign_risk_level(row):
    if row['TotalDrugsUsed'] > 1:
        return 'HighRisk'  
    elif row['TotalDrugsUsed'] == 1:
        
        if row['Fentanyl'] == 1 or row['Heroin'] == 1:
            return 'MediumRisk'  
        else:
            return 'LowRisk'
    else:
        return 'LowRisk'  

data_processed['RiskLevel'] = data_processed.apply(assign_risk_level, axis=1)

risk_level_distribution = data_processed['RiskLevel'].value_counts()

risk_level_distribution

output_file_path_with_risk = '/mnt/data/drug_deaths_with_risk_level.csv'
data_processed.to_csv(output_file_path_with_risk, index=False)

output_file_path_with_risk

data_needed_from_original = data_original[['Age', 'Sex', 'Race']].copy()

data_final = pd.concat([data_processed.drop(columns=['TotalDrugsUsed', 'RiskLevel']), data_needed_from_original], axis=1)

data_final['RiskLevel'] = data_final.apply(assign_risk_level, axis=1)

data_final.head()

data_final['TotalDrugsUsed'] = data_final[drug_columns].sum(axis=1)

def assign_risk_level_updated(row):
    if row['TotalDrugsUsed'] > 1:
        return 'HighRisk'  
    elif row['TotalDrugsUsed'] == 1:
        
        if row['Fentanyl'] == 1 or row['Heroin'] == 1:
            return 'MediumRisk'  
        else:
            return 'LowRisk'  
    else:
        return 'LowRisk'   

data_final['RiskLevel'] = data_final.apply(assign_risk_level_updated, axis=1)

data_final.head()

final_output_file_path = '/mnt/data/drug_deaths_final_with_risk_age_sex_race.csv'
data_final.to_csv(final_output_file_path, index=False)

