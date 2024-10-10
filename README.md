# ETL-workflow
The project is to extract data from CSV, JSON, and XML formats, transform it, and load the transformed data into a structured format.
APPROACHES:
Step 1: Gather Data Files:
Downloaded dataset which contains datasets of multiple data formats.
Extracted the downloaded source file.

Step 2: Import Libraries and Set Paths:
Imported necessary libraries in PYCHARM like:
import glob as glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
Set paths for log file and to save transformed data in csv file

Step 3:Define functions for each step of  ETL as follows:
Extract Data:
Three different functions to extract data from CSV, JSON, and XML files respectively.
A master function will call the relevant function based on the file type and combine the extracted data into a single DataFrame.
Transform Data:
The transformation process involves converting:
Heights from inches to metres.
Weight from pounds to kilograms.
This step ensures the data is in the desired format for further analysis or storage.
Load Data:
The transformed data is saved to a CSV file, which can later be loaded into a relational database or used for further processing.
Logging:
Throughout the ETL process, each phase (Extraction, Transformation, Loading) is logged with a timestamp to ensure traceability and monitoring.
Logs are saved in a text file for auditing or troubleshooting purposes

