# school_data.py
# AUTHOR NAME: Abdul Wasay
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc.
# You may import any modules from the standard Python library.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# You may add your own additional classes, functions, variables, etc.


class Stats:
    def __init__(self, enrollment_array, school_names, school_year, school_grades, year_to_index, name_to_index, code_to_name, name_to_code):
        self.data = enrollment_array
        self.school = school_names
        self.year = school_year
        self.grades = school_grades
        self.year_to_index = year_to_index
        self.name_to_index = name_to_index
        self.code_to_index = code_to_name
        self.name_to_code = name_to_code

    def getSchoolData(self, user_input):

        if (user_input in self.code_to_index):
            school_name = self.code_to_index[user_input]
            print("School Name: ", school_name, ", School Code: ", user_input)
        else:
            school_name = user_input
            print("School Name: ", user_input, ", School Code: ",
                  self.name_to_code[school_name])

        school_index = self.name_to_index[school_name]
        school_data = self.data[school_index]

        # Grade-wise means
        print("Mean enrollment for Grade 10: ", int(
            np.floor(np.mean(school_data[:, 0]))))
        print("Mean enrollment for Grade 11: ", int(
            np.floor(np.mean(school_data[:, 1]))))
        print("Mean enrollment for Grade 12: ", int(
            np.floor(np.mean(school_data[:, 2]))))

        # Highest and lowest values
        print("Highest enrollment for a single grade: ", int(np.max(school_data)))
        print("Lowest enrollment for a single grade: ", int(np.min(school_data)))

        # Yearly totals
        print("Total enrollment for 2013: ", int(np.sum(school_data[0])))
        print("Total enrollment for 2014: ", int(np.sum(school_data[1])))
        print("Total enrollment for 2015: ", int(np.sum(school_data[2])))
        print("Total enrollment for 2016: ", int(np.sum(school_data[3])))
        print("Total enrollment for 2017: ", int(np.sum(school_data[4])))
        print("Total enrollment for 2018: ", int(np.sum(school_data[5])))
        print("Total enrollment for 2019: ", int(np.sum(school_data[6])))
        print("Total enrollment for 2020: ", int(np.sum(school_data[7])))
        print("Total enrollment for 2021: ", int(np.sum(school_data[8])))
        print("Total enrollment for 2022: ", int(np.sum(school_data[9])))

        # Overall totals and mean
        print("Total 10 year enrollment: ", int(np.sum(school_data)))
        print("Mean total enrollment over 10 years: ",
              int(np.floor(np.sum(school_data)/10)))

        # Check for large class sizes
        over_500 = school_data[school_data > 500]
        if (over_500.size == 0):
            print("No enrollment over 500.")
        else:
            print("For all enrollments over 500, the median was ",
                  int(np.median(over_500)))

    def generalStats(self):
        print("Mean enrollment in 2013: ", int(
            np.floor(np.mean(self.data[:, 0, :]))))
        print("Mean enrollment in 2022: ", int(
            np.floor(np.mean(self.data[:, 9, :]))))
        print("Total graduating class of 2022: ",
              int(np.sum(self.data[:, 9, 2])))
        print("Highest enrollment for a single grade: ", int(np.max(self.data)))
        print("Lowest enrollment for a single grade: ", int(np.min(self.data)))


def main():
    # Main driver function for terminal-based school statistics application
    print("ENSF 692 School Enrollment Statistics")

    # Load raw CSV data as string array
    raw_data = np.genfromtxt('Assignment3Data.csv',
                             delimiter=',', dtype=str, skip_header=1)

    # Extract unique school names and years
    school_names = np.unique(raw_data[:, 1])
    school_year = np.unique(raw_data[:, 0])
    school_year.astype(int)
    school_grades = ['Grade 10', 'Grade 11', 'Grade 12']

    # Initialize 3D array: [schools, years, grades]
    enrollment_array = np.zeros(
        (len(school_names), len(school_year), len(school_grades)))

    # Create dictionaries for index lookups
    year_to_index = {year: idx for idx, year in enumerate(school_year)}
    name_to_index = {name: idx for idx, name in enumerate(school_names)}
    school_codes = {}
    code_to_name = {}
    name_to_code = {}

    # Populate array and mapping dictionaries
    for row in raw_data:
        school_index = name_to_index[row[1]]

        year_index = year_to_index[row[0]]

        enrollment_array[school_index, year_index,
                         0] = float(row[3]) if row[3] != "NaN" else 0
        enrollment_array[school_index, year_index,
                         1] = float(row[4]) if row[4] != "NaN" else 0
        enrollment_array[school_index, year_index,
                         2] = float(row[5]) if row[5] != "NaN" else 0
        # school_codes[row[1]] = school_codes
        code_to_name[row[2]] = row[1]
        name_to_code[row[1]] = row[2]

    # Instantiate stats class
    enrollment_stats = Stats(enrollment_array, school_names,
                             school_year, school_grades, year_to_index, name_to_index, code_to_name, name_to_code)

    # Print Stage 1 requirements here
    print("Shape of full data array: ",
          enrollment_array.shape)
    print("Dimensions of full data array: ", enrollment_array.ndim)

    # Prompt for user input
    user_input = input("Please enter a high school name or code: ")

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    enrollment_stats.getSchoolData(user_input)

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    enrollment_stats.generalStats()


if __name__ == '__main__':
    main()
