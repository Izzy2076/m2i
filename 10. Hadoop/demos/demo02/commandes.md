1. Correction problèmes d'encodage (Windows => Linux) :

```bash
sed -i 's/\r$//' mapper.py reducer.py
```

- Supprime les caractères de retour chariot Windows
- Nécessaire si les scripts ont été créés sur Windows

2. Exécution du job mapreduce avec hadoop streaming

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="wordcount-python" \
-D mapreduce.job.reduces=2 \
-files mapper.py,reducer.py \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-input /input/wordcount \
-output /output/wordcount
```

- hadoop jar .... : Lance le JAR hadoop streaming pour exécuter des scripts non-JAVA.
- -D mapreduce.job.name="wordcount-python" : Nom du job pour l'identifier
- -D mapreduce.job.reduces=2 : utilise 2 tâches 
- -files mapper.py, reducer.py : copie les scripts sur tous les noeuds
- -output /output/wordcount : répertoire de sortie (ne doit pas exister)
