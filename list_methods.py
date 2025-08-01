'''Here are practical examples of the most frequently used list methods in 
the context of MLOps projects, with explanations for their typical use:'''

'''
1. append()

Adding new parsed data or results to a list during batch processing.'''

metrics = []
metrics.append(0.95)  # metrics: [0.95]


'''
2. extend()
Adding multiple new log or feature values at once.'''

results = [0.8, 0.9]
results.extend([0.85, 0.97])  # results: [0.8, 0.9, 0.85, 0.97]


'''
3. insert()
Inserting a header or metadata at a specific index.'''

pipeline_steps = ['scale', 'train']
pipeline_steps.insert(0, 'validate')  # ['validate', 'scale', 'train']


'''
4. remove()
Removing unwanted or deprecated labels/configs.'''

log_levels = ['info', 'debug', 'error']
log_levels.remove('debug')  # ['info', 'error']


'''
5. pop()
Extracting the most recent error or task message.'''

errors = ['disk', 'gpu', 'ram']
last_error = errors.pop()  # 'ram', errors: ['disk', 'gpu']


'''
6. clear()
Resetting intermediate data between pipeline runs.'''

temp_results = [0.1, 0.2]
temp_results.clear()  # []


'''
7. index()
Finding the position of a label or config in a list.'''

statuses = ['queued', 'running', 'done']
i = statuses.index('running')  # 1


'''
8. count()
Counting specific event types (e.g., failed tasks).'''

statuses = ['ok', 'fail', 'ok', 'fail']
num_fails = statuses.count('fail')  # 2


'''
9. sort()
Sorting model results, scores, or configuration keys.'''

scores = [0.88, 0.96, 0.72]
scores.sort()  # [0.72, 0.88, 0.96]


'''
10. reverse()
Reverse the processing order of a batch or set of logs.'''

steps = ['preprocess', 'train', 'evaluate']
steps.reverse()  # ['evaluate', 'train', 'preprocess']


'''
11. copy()
Creating a snapshot of log or result lists before mutating.'''

metrics = [0.9, 0.8]
backup = metrics.copy()


'''
12. len()
Measuring number of batches, logs, or items processed.'''

batch = [1, 2, 3, 4]
num_items = len(batch)  # 4