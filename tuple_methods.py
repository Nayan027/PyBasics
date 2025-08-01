'''Method/Function	            Example (MLOps-use)	                       Output
---------------------------------------------------------------------------------------------
count()	                       metrics.count('fail')	      Occurrences of 'fail' in metric tuple

index()	                      metrics.index('recall')	           First index of 'recall'

len()	                          len(input_shape)	                Number of dimensions

min(), max()	                  max(val_losses)	                   Best/worst value

sum()	                         sum(batch_sizes)	                       Aggregate

Slicing	                         run_metrics[:2]	                    Subset as tuple

Concatenation	                 tuple1 + tuple2	                     Combined tuple

Membership	                 'accuracy' in metric_tuple	              Boolean (True/False)

Packing/Unpacking	            (a, b, c) = tup	                       Parallel assignment

Tuples are essential in MLOps for representing immutable, ordered collections such as parameter sets, 
fixed pipeline steps, or record schemas, ensuring security and consistency in code and data structures.'''