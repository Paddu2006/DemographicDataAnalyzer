import pandas as pd

def calculate_demographic_data():
    # Load the data
    df = pd.read_csv('census_data.csv')
    
    # Race count
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['gender'] == 'Male']['age'].mean(), 1)
    
    # Percentage with Bachelors
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )
    
    # Advanced education >50K
    advanced = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_advanced_education = round(
        (advanced['income'] == '>50K').mean() * 100, 1
    )
    
    # Lower education >50K
    lower = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_lower_education = round(
        (lower['income'] == '>50K').mean() * 100, 1
    )
    
    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()
    
    # % earning >50K among min workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['income'] == '>50K').mean() * 100, 1
    )
    
    # Country with highest % earning >50K
    country_income = (df[df['income'] == '>50K']['native-country'].value_counts() /
                      df['native-country'].value_counts()) * 100
    highest_earning_country = country_income.idxmax()
    highest_earning_country_percentage = round(country_income.max(), 1)
    
    # Top occupation in India for >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['income'] == '>50K')]['occupation'].mode()[0]
    
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_advanced_education': percentage_advanced_education,
        'percentage_lower_education': percentage_lower_education,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
