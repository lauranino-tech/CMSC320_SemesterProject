# Background

## Table of Contents

- [Background](#background)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [README Instructions](#readme-instructions)
  - [Current Setup](#current-setup)
- [--\> TO-DO \<--](#---to-do---)
  - [Task 2.2 - Data Exploration 1](#task-22---data-exploration-1)
  - [Task 2.3 - Data Exploration 2](#task-23---data-exploration-2)
  - [Task 2.4 - Data Exploration 3 (Hypothesis Testing)](#task-24---data-exploration-3-hypothesis-testing)
  - [Task 2.5 - Project Checkpoint 2](#task-25---project-checkpoint-2)
- [\<-- COMPLETED --\>](#---completed---)
  - [Task 2.1 - Data Cleaning](#task-21---data-cleaning)
  - [Task 2.0 - Convert Dataset to CSV](#task-20---convert-dataset-to-csv)
  - [Task 1.1 - Project Checkpoint 1](#task-11---project-checkpoint-1)
  - [Task 1.0 - Download Dataset](#task-10---download-dataset)

## Introduction

**Title:** CMSC320_SemesterProject

**Team Members:**

- Max Dustin
- Seth Calhoon
- Laura Gutirrez
- Aaryashree Sapkota
- Spencer Feldmann

**Description:** This is a group project for **CMSC320: Introduction to Data Science** for the **Spring 2026** semester. The project aims to analyze a subset of the ERA5 global weather dataset in numerous locations around the globe using the data science pipeline.

**Important Deadlines**

- <font color='grey'>February 26, 2026 - First Checkpoint Due (COMPLETED)</font>
- <font color='orange'>March 31, 2026 - Second Checkpoint Due (UPCOMING)</font>
- May 8, 2026 - Final Checkpoint Due

**Dataset Link:** https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means?tab=overview (YOU DO NOT NEED TO DOWNLOAD THIS)

**Chosen Subset:** Monthly averaged weather data in select cities at 12:00 noon from 2021 to 2025.

**Rubric:** https://umd.instructure.com/courses/1398412/assignments/7539599

## README Instructions

**Please** update this README with each and every push to the remote git repository so that everyone is able to stay up to date on the current state of the project.

## Current Setup

Please read and examine **ALL** files. **Important** files are highlighted <font color='lightgreen'>green</font>. Update as more files are added.

**Files:**

- <font color='lightgreen'>_README.md_</font> - You're reading it.
- <font color='lightgreen'>_data_exploration.ipynb_</font> - Notebook that performs basic data exploration.
- _data_cleaning.ipynb_ - Notebook that performs basic data cleaning.
- _subset_selection.ipynb_ - Notebook that extracts desired data subset to analyze from main dataset.
- <font color='lightgreen'>_weather.csv_</font> - Main cleaned dataset to analyze and work with. DO NOT UPDATE this dataset.
- _cities.csv_ - Mapping major cities and locations to their individual latitudes and longitudes (rounded to the nearest 0.25 degrees).
- _sql_database_setup.py_ - Utility file that creates SQL database from an original large dataset.
- _grib_to_csv.py_ - Utility file that converts GRIB (gridded weather) files to readable CSV.

The cleaned dataset is stored in _weather.csv_, please do not update this dataset, if you decide to create another CSV file based on this dataset, name it something else to avoid confusion or accidental overwriting.

**Important**: We will be using a small subset of the full dataset. Please do not download the dataset as it is far too large and time intensive to handle, instead _weather.csv_ contains the subset we will be using after it has already been cleaned.

**Clarification:** There are a lot of variables in the dataset, each in different units. **Explanation of columns** and their units/meanings can be found on the dataset website after scrolling down; linked in [Introduction](#introduction).

**Note:** There are mentions of a SQL database throughout the early parts of the project. You do not need to go through the process of setting it up. All the data you need is in _weather.csv_. Please do not run any of the non-highlighted files.

---

# --> TO-DO <--

**Instructions:** For each task below please write your name(s) to inform one another about who is working on what. Once a task is completed move it to [<-- COMPLETED -->](#---completed---) and add any additional information. If you need a specific task done, add it to this list so everyone remains informed.

## Task 2.2 - Data Exploration 1

    Members: (ENTER NAME(S) HERE)
    Status: Not Started

**Task:** Perform data exploration using a unique statistical method. Incorporate at least one plot.

**PLEASE CONSULT RUBRIC**

**Files:**

- _data_exploration.ipynb_ - Use this notebook to perform the data exploration task. The notebook is divided into three sections for each data exploration task.

**Progress:**

- LIST PROGRESS HERE

## Task 2.3 - Data Exploration 2

    Members: Seth C.
    Status: In Progress

**Task:** Perform data exploration using a unique statistical method. Incorporate at least one plot.

**PLEASE CONSULT RUBRIC**

**Files:**

- _data_exploration.ipynb_ - Use this notebook to perform the data exploration task. The notebook is divided into three sections for each data exploration task.

**Progress:**

- LIST PROGRESS HERE

## Task 2.4 - Data Exploration 3 (Hypothesis Testing)

    Members: Aaryan S.
    Status: In progress

**Task:** Perform data exploration using a hypothesis testing method. Incorporate at least one plot.

**PLEASE CONSULT RUBRIC**

**Files:**

- _data_exploration.ipynb_ - Use this notebook to perform the data exploration task. The notebook is divided into three sections for each data exploration task.

**Progress:**

- Finished coding most of it, might need to check over once
- Working on conclusion, should be done by tomorrow

## Task 2.5 - Project Checkpoint 2

    Members: Max D
    Status: Not Started

Prerequisite: [Task 2.2](#task-22---data-exploration-1), [Task 2.3](#task-23---data-exploration-2), [Task 2.4](#task-24---data-exploration-3-hypothesis-testing)

**Task:** Complete and submit Project Checkpoint 2.

---

# <-- COMPLETED -->

**Instructions:** Move tasks here from [--> TO-DO <--](#---to-do---) when completed. Adding additional information regarding its completion is preferred (COMMENT YOUR CODE). Record date of completion, members involved, and any other relevant information. Do not remove completed tasks from here.

## Task 2.1 - Data Cleaning

    Worked-On: Max D
    Completed: 03/22/2026

**Task:** Clean the provided dataset, ensuring that data types are correct and that missing data is accounted for.

**Result:** Cleaned the dataset and produced a CSV file contained said cleaned dataset.

**Files:**

- _data_cleaning.ipynb_ - Cleans dataset by combining rows with the same data, converting data into proper data types, and exporting the newly cleaned set as a CSV file.
- _weather.csv_ - Cleaned dataset file. This should be used for all data exploration.

## Task 2.0 - Convert Dataset to CSV

    Worked-On: Max D
    Completed: 03/21/2026

**Task:** Convert the downloaded GRIB dataset to CSV while selecting a subset to use that is small.

**Result:** Selected a subset of the original dataset to use for the rest of the project. In the process the GRIB file was added to a SQL database, queryed to produce a smaller dataset, and then converted to a CSV.

**Files:**

- _grib_to_csv.py_ - Converts GRIB file into a CSV. The resulting CSV is of a far larger file size than the GRIB.
- _sql_database_setup.py_ - Setup SQL database using sqlite3 as the Database Management System. Stores large CSV data as table.
- _subset_selection.ipynb_ - Using the SQL database, queries the dataset by selecting all rows that contain data from a list of latitude and longitude values. Then stores smaller subset as a new table in the database.
- _cities.csv_ - List of 30 cities/locations around the world with their corresponding latitude and longitude. To be used by _subset_selection.ipynb_ to gather subset.

## Task 1.1 - Project Checkpoint 1

    Worked-On: Max D
    Completed: 02/23/2026

**Task:** Complete and submit Project Checkpoint 1.

**Result:** Submitted on Gradescope.

## Task 1.0 - Download Dataset

    Worked-On: Max D
    Completed: 02/23/2026

**Task:** Download the dataset from the Climate Data Store.

**Result:** Downloaded dataset using the following API call:

    dataset = "reanalysis-era5-single-levels-monthly-means"
    request = {
    "product_type": ["monthly_averaged_reanalysis_by_hour_of_day"],
    "variable": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "2m_dewpoint_temperature",
        "2m_temperature",
        "surface_pressure",
        "total_precipitation",
        "evaporation",
        "runoff",
        "soil_temperature_level_1",
        "soil_type",
        "snowfall",
        "snow_depth"
    ],
    "year": [
        "2021", "2022", "2023",
        "2024", "2025"
    ],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "time": ["12:00"],
    "data_format": "grib",
    "download_format": "unarchived"
    }
