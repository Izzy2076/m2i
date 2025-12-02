```bash
sed -i 's/\r$//' mapper.py reducer.py partitionner.py combiner.py
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="demo03-python" \
-D mapreduce.job.reduces=2 \
-files mapper.py,reducer.py,combiner.py,partitionner.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-combiner "python3 combiner.py" \
-partitioner "python3 partitionner.py" \
-input /input/demo03 \
-output /output/demo03
```