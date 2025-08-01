'''Method/Function           	        Example (MLOps Use)                            	Output / Effect
----------------------------------------------------------------------------------------------------------------------
get()	                        params.get('lr', 0.01)	                     Value for 'lr' or default if missing

items()	                     for k, v in metrics.items(): ...	            Key–value iteration (e.g., report logs)

keys()	                          list(config.keys())	                           List of all config keys

values()                     	list(results.values())	                           List of all result values

update()	                  base_config.update(overrides)                  	Merges/overrides configuration

pop()	                          params.pop('epochs')	                      Removes & returns value for 'epochs'

popitem()	                    last = params.popitem()	                      Removes & returns last key–value pair

setdefault()	            logs.setdefault('error', []).append(msg)	       Initializes key with default if absent

clear()                         	metrics.clear()	                             Removes all entries from dictionary

copy()	                         backup = scores.copy()	                             Shallow copy for safe edits

fromkeys()                 	dict.fromkeys(steps, 'pending')                  	New dict from keys with init value

len()	                              len(config)	                                 Number of key–value pairs

Membership	                    'accuracy' in result_dict	                 Check if key exists (returns True/False)


These methods and functions make managing dynamic configurations, aggregating metrics, 
and orchestrating tasks or log reporting much simpler and more robust in any MLOps workflow.'''