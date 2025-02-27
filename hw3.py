from typing import List
import data
from data import CountyDemographics
import county_demographics


#Part 1
def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population["2014 Population"] for county in counties)

#Part 2
def filter_by_state(county_list: List[data.CountyDemographics], state: str) -> List[data.CountyDemographics]:

    filtered_counties = [county for county in county_list if county.state == state]

    return filtered_counties

#Part 3
def population_by_education(county_list: List[data.CountyDemographics], education_key: str) -> float:

    total_population = 0

    for county in county_list:
        if education_key in county.education:
            education_percentage = county.education[education_key]
            population = county.population['2014 Population']
            total_population += (education_percentage / 100) * population

    return total_population


def population_by_ethnicity(county_list: List[data.CountyDemographics], ethnicity_key: str) -> float:

    total_population = 0

    for county in county_list:
        if ethnicity_key in county.ethnicities:
            ethnicity_percentage = county.ethnicities[ethnicity_key]
            population = county.population['2014 Population']
            total_population += (ethnicity_percentage / 100) * population

    return total_population


def population_below_poverty_level(county_list: List[data.CountyDemographics]) -> float:

    total_population = 0

    for county in county_list:
        poverty_percentage = county.income['Persons Below Poverty Level']
        population = county.population['2014 Population']
        total_population += (poverty_percentage / 100) * population

    return total_population


#Part 4

def percent_by_education(county_list: list, education_key: str) -> float:
    total_population = sum(county.population for county in county_list)
    total_education_population = population_by_education(county_list, education_key)

    if total_population == 0:
        return 0

    return (total_education_population / total_population) * 100


def percent_by_ethnicity(county_list: list, ethnicity_key: str) -> float:
    total_population = sum(county.population for county in county_list)
    total_ethnicity_population = population_by_ethnicity(county_list, ethnicity_key)

    if total_population == 0:
        return 0

    return (total_ethnicity_population / total_population) * 100


def percent_below_poverty_level(county_list: list) -> float:
    total_population = sum(county.population for county in county_list)
    total_below_poverty = population_below_poverty_level(county_list)

    if total_population == 0:
        return 0

    return (total_below_poverty / total_population) * 100

#Part 5

def education_greater_than(county_list: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if key in county.education and county.education[key] > threshold:
            result.append(county)
    return result

def education_less_than(county_list: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if key in county.education and county.education[key] < threshold:
            result.append(county)
    return result

def ethnicity_greater_than(county_list: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if key in county.ethnicity and county.ethnicity[key] > threshold:
            result.append(county)
    return result

def ethnicity_less_than(county_list: List[CountyDemographics], key: str, threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if key in county.ethnicity and county.ethnicity[key] < threshold:
            result.append(county)
    return result

def below_poverty_level_greater_than(county_list: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if 'Persons Below Poverty Level' in county.income and county.income['Persons Below Poverty Level'] > threshold:
            result.append(county)
    return result

def below_poverty_level_less_than(county_list: List[CountyDemographics], threshold: float) -> List[CountyDemographics]:
    result = []
    for county in county_list:
        if 'Persons Below Poverty Level' in county.income and county.income['Persons Below Poverty Level'] < threshold:
            result.append(county)
    return result