<<<<<<< HEAD
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
=======
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("census_data.csv")

    # 1. How many people of each race are represented?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Advanced education (>50K)
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = round(
        (df[advanced_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Without advanced education (>50K)
    lower_edu_rich = round(
        (df[~advanced_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich among those who work minimum hours
    rich_percentage = round(
        (df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest percentage of rich
    country_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # 9. Top occupation in India for those earning >50K
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Percentage with advanced education earning >50K:", higher_edu_rich)
        print("Percentage without advanced education earning >50K:", lower_edu_rich)
        print("Min work hours:", min_work_hours)
        print("Percentage earning >50K among those who work min hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == "__main__":
    calculate_demographic_data()
>>>>>>> 51027a3 (Update demographic_data_analyzer.py)
