'''                 string methods
Method	                                Common Uses in MLOps
-----------------------------     --------------------------------------
split(), rsplit()	                    Parsing data, logs, configs

join()	                            Reconstructing or serializing data

replace()                     	    Data cleaning, text normalization

strip(), lstrip(), rstrip()	            Whitespace/character cleanup

lower(), upper(), casefold()          	Consistent text formatting

startswith(), endswith()	               Filename/log filtering

find(), index()	                  Substring searching (keys, delimiters)

count()                             	Occurrence counting/statistics

isalpha(), isdigit(), 
isalnum(), isspace()	                        Validation

format(), f-string	                   Dynamic message/log generation

splitlines()	                         Multi-line text processing

removeprefix(), removesuffix()	          Cleaning file/field names                          '''



'''Here are practical examples of each frequently used string method in 
an MLOps context, with brief explanations for when they’re useful:

1. split(), rsplit()

Splitting CSV rows, logs, or configuration lines:'''

log_line = "2025-08-01,INFO,Job completed"
fields = log_line.split(",")  # ['2025-08-01', 'INFO', 'Job completed']

path = "my/data/output_file.csv"
filename = path.rsplit("/", 1)[-1]  # 'output_file.csv'


'''
2. join()

Generating configuration strings or file paths.'''

fields = ['2025-08-01', 'INFO', 'Job completed']
csv_line = ",".join(fields)  # '2025-08-01,INFO,Job completed'


'''
3. replace()
Standardizing delimiters or cleaning dirty data.'''

config_str = "path\\to\\data\\file"
config_str = config_str.replace("\\", "/")  # 'path/to/data/file'


'''
4. strip(), lstrip(), rstrip()

Trimming whitespace from user-inputted configuration or data fields.'''

user_input = "   completed   "
cleaned_status = user_input.strip()  # 'completed'


'''
5. lower(), upper(), casefold()

Normalizing class labels or user inputs for matching.'''

label = "Cat"
label = label.lower()  # 'cat'


'''
6. startswith(), endswith()

Filtering only CSV files for data ingestion.'''

filename = "data_2025.csv"
if filename.endswith('.csv'):
    # Process the file
    pass


'''
7. find(), index()

Locating tokens or delimiters in logs/configs.'''

config_line = "learning_rate=0.01"
eq_pos = config_line.find("=")  # 13
key = config_line[:eq_pos]  # 'learning_rate'


'''
8. count()

Basic metric: count how many ERRORs in logs.'''

log_block = "INFO\nERROR\nINFO\nERROR"
num_errors = log_block.count("ERROR")  # 2


'''
9. isalpha(), isdigit(), isalnum(), isspace()

Input validation for fields in a YAML/JSON config.'''

field = "12345"
if field.isdigit():
    # Valid numeric field
    pass

token = "statusOK"
if token.isalnum():
    # Valid
    pass


'''
10. format(), f-strings

Structured log message formatting, config templating.'''

job_id = 42
status = "finished"
log_msg = f"Job {job_id}: {status}"  # 'Job 42: finished'

log_msg = "Job {}: {}".format(job_id, status)  # 'Job 42: finished'


'''
11. splitlines()

Processing multi-line log output or bulk data.'''

logs = "INFO\nERROR\nINFO"
lines = logs.splitlines()  # ['INFO', 'ERROR', 'INFO']


'''
12. removeprefix(), removesuffix()

Cleaning up paths, filenames, or labels for consistency ( 3.9+).'''

log_name = "INFO_log.txt"
base = log_name.removeprefix("INFO_")  # 'log.txt'
dataset_file = "data_sample.csv"
name = dataset_file.removesuffix(".csv")  # 'data_sample'