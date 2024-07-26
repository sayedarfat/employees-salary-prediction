import pandas as pd

def preprocess_data(data_path):
    # Load the data
    data = pd.read_csv(data_path)
    
    # Example preprocessing steps
    data['City'] = data['City'].apply(lambda x: 1 if x == 'metro' else 0)
    # Additional preprocessing steps...
    
    return data

if __name__ == "__main__":
    data = preprocess_data('../data/ML_case_study.csv')
    data.to_csv('../data/preprocessed_data.csv', index=False)
