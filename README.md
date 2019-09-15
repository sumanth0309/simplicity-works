
Apache Spark – Initial Steps

Python Installation
	•Please download Python package from Python official site (prefer to download version above 3.0).
	•Add environment variable PYTHON_HOME and point it to python installation location.
	•Test the installation by hitting python command in command prompt.
	•As you are using Python to develop Spark jobs. To write spark jobs we need PySpark libraries to write spark jobs in python(pip install 	pySpark)
	
Apache Spark Installation
	•Download Pre – built Hadoop Apache Spark from here (prefer to download version above 2.4).
	•Add environment variable SPARK_HOME and point it to lib folder of downloaded distribution.
	•Spark needs Hadoop installed to run on top of it .So instead of Haddop installation , You can mimic the installation by following 		 below steps
	•Download winutils.exe binary from https://github.com/steveloughran/winutils repository.
	•Create a folder structure Hadoop/bin in your system and place winutils.exe inside it.
	•Add environment variable HADOOP_HOME  and point it to Hadoop/bin folder
	•To test the installation hit spark-shell command in the command promt.You should see spark-shell ready to write scala code.
	
Running Word Count Program
	•To start working with spark. You can run a basic data analysis program “WordCount”using Spark.
	•Open command prompt and run command : spark-submit WordCount.py
	•If you face any issue related to finding file path .Adjust the code in wordCount.py 
		linesRdd = sc.textFile("relativeFilePath\Book.txt")

