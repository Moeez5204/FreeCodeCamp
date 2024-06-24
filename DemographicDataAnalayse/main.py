import pandas as pd

file = 'adult.data.csv'
df = pd.read_csv(file)


race_counts = df['race'].value_counts()
print("Number of people by race:")
print(race_counts)

men_average_age = df[df['sex'] == 'Male']['age'].mean()
print(f"The average age of men is {men_average_age:.1f} years")

bachelors_percentage = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
print(f"The percentage of people with a Bachelor's degree is {bachelors_percentage:.3f}%")

higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_above_50k_percentage = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
print(f"The percentage of people with advanced education and earning more than 50K is {higher_education_above_50k_percentage:.3f}%")

non_higher_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
non_higher_education_above_50k_percentage = (non_higher_education[non_higher_education['salary'] == '>50K'].shape[0] / non_higher_education.shape[0]) * 100
print(f"The percentage of people without advanced education and earning more than 50K is {non_higher_education_above_50k_percentage:.3f}%")

min_hours_per_week = df['hours-per-week'].min()
print(f"The minimum number of hours a person works per week is: {min_hours_per_week}")


country_high_income = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
highest_percentage_country = country_high_income.idxmax()
highest_percentage_value = country_high_income.max()
print(f"The country with the highest percentage of people earning >50K is {highest_percentage_country} with {highest_percentage_value:.2f}%")


high_income_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
most_popular_occupation_india = high_income_india['occupation'].mode()[0]
print(f"The most popular occupation for those earning >50K in India is: {most_popular_occupation_india}")