import glob as glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

##EXTRACTING THE DATA FROM VARIOUS FILES (CONTAINING DIFFERENT FILE FORMATS):

#reading only csv file and convert it into single dataframe

csv_files=glob.glob("/Users/Sangeetha/Desktop/source/*.csv")

df=pd.DataFrame()
for csv_file in csv_files:
    with open("my_log.txt", "a") as log_file:
        log_file.write(str(datetime.now()) + ":Extracting csv_files.\n")
    temp_df=pd.read_csv(csv_file)
    df= pd.concat([df,temp_df])


#reading json file and joining in single dataframe
json_files=glob.glob("/Users/Sangeetha/Desktop/source/*.json")

for json_file in json_files:
    with open("my_log.txt", "a") as log_file:
        log_file.write(str(datetime.now()) + ":Extracting JSON_files.\n")

    tmp_df=pd.read_json(json_file,lines=True)
    df = pd.concat([df,tmp_df])


# reading and parsing xml files and combining with single dataframe
xml_files=glob.glob("/Users/Sangeetha/Desktop/source/*.xml")

books_list = []

#parsing the xml file using parse() function in elementtree module
for xml_file in xml_files:
    with open("my_log.txt", "a") as log_file:
        log_file.write(str(datetime.now()) + ":Extracting XML_files.\n")
    tree = ET.parse(xml_file)
    root = tree.getroot()
#need to extract the data from the XML file by iterating over the XML tree, accessing the tags and text of each element
    for book_elem in root.findall('.//person'):
        book_dict = {}
        for child_elem in book_elem:
            book_dict[child_elem.tag] = child_elem.text
        books_list.append(book_dict)

temp2_df=pd.DataFrame(books_list)
df = pd.concat([df,temp2_df])

with open("my_log.txt", "a") as log_file:
    log_file.write(str(datetime.now())+":extracted all the files from source folder.\n")


##TRANSFORMING THE COLUMN VALUES INTO REQUIRED FORMAT:

# Step 1: Select the column
height_column = df['height']
weight_col=df['weight']

# Step 2: Apply a function to each value
def in_cm(x):
    # print(type(x))
    y=(int(float(x))*2.54)
    return round(y,1)


new_column = height_column.apply(in_cm)
with open("my_log.txt", "a") as log_file:
    log_file.write(str(datetime.now())+":transforming the height col from inch to cm.\n")

#step:3: apply function to change weight column:
def in_kgs(z):
    k=(int(float(z))*0.45)
    return round(k,1)
new2_column=weight_col.apply(in_kgs)
with open("my_log.txt", "a") as log_file:
    log_file.write(str(datetime.now())+"transforming weight col from lbs to kgs.\n")

# Step 3: Assign the new values back to the column
df['height'] = new_column
df['weight'] = new2_column

with open("my_log.txt", "a") as log_file:
    log_file.write(str(datetime.now())+":all files are transformed.\n")

# converting dataframe to csv file (loading)

df.to_csv('transformed_data.csv', index=False)
with open("my_log.txt", "a") as log_file:
    log_file.write(str(datetime.now())+":df is converted to csv file.\n")






