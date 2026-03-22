## Table of Contents
- [Introduction](#introduction)
- [README Instructions](#readme-instructions)
- [Current Setup (START HERE)](#current-setup)
- [--> TO-DO <--](#---to-do---)
- [<-- COMPLETED -->](#---completed---)

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


**Dataset:** https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means?tab=overview (YOU DO NOT NEED TO DOWNLOAD THIS)

**Rubric:** https://umd.instructure.com/courses/1398412/assignments/7539599

## README Instructions

**Please** update this README with each and every push to the remote git repository so that everyone is able to stay up to date on the current state of the project.

Noteable sections to update include but are not limited to:
- [Current Setup](#current-setup)
- [--> TO-DO <--](#---to-do---)
- [<-- COMPLETED -->](#---completed---)

## Current Setup

Please read and examine **ALL** files. **Important** files are highlighted <font color='lightgreen'>green</font>. Update as more files are added.

**Files:**
- <font color='lightgreen'>*README.md*</font> - You're reading it.
- <font color='lightgreen'>*data_cleaning.ipynb*</font> - Notebook that performs basic data cleaning.
- *subset_selection.ipynb* - Notebook that extracts desired data subset to analyze from main dataset.
- <font color='lightgreen'>*city_weather.csv*</font> - Main dataset to analyze and work with. DO NOT UPDATE this dataset in any additional notebook files.
- *cities.csv* - Mapping major cities and locations to their individual latitudes and longitudes (rounded to the nearest 0.25 degrees).
- *sql_database_setup.py* - Utility file that creates SQL database from an original large dataset.
- *grib_to_csv.py* - Utility file that converts GRIB (gridded weather) files to readable CSV.

---

# --> TO-DO <--

**Instructions:** For each task below please write your name(s) to inform one another about who is working on what. Once a task is completed move it to [<-- COMPLETED -->](#---completed---) and add any additional information. If you need a specific task done, add it to this list so everyone remains informed.

---

# <-- COMPLETED -->

**Instructions:** Move tasks here from [--> TO-DO <--](#---to-do---) when completed. Adding additional information regarding its completion is preferred (COMMENT YOUR CODE). Record date of completion, members involved, and any other relevant information. Do not remove completed tasks from here.