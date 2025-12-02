```bash

hdfs dfs -rm -r -f /output/severity_by_state


sed -i 's/\r$//' mapper/05_mapper_severity_by_state.py combiner/05_combiner_severity.py reducer/05_reducer_average.py partitioner/05_partitioner_state.py


hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.reduces=3 \
  -files mapper/05_mapper_severity_by_state.py,combiner/05_combiner_severity.py,reducer/05_reducer_average.py,partitioner/05_partitioner_state.py \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
  -mapper "python3 ./mapper/05_mapper_severity_by_state.py" \
  -combiner "python3 ./combiner/05_combiner_severity.py" \
  -reducer "python3 ./reducer/05_reducer_average.py" \
  -partitioner "python3 ./patitioner/05_partitioner_state.py" \
  -input /input/us_accidents/US_Accidents_March23.csv \
  -output /output/severity_by_state

hdfs dfs -cat /output/severity_by_state/part-*


```
