 Here is the formal content in Markdown format without any emojis or external links for the topic "Installing Spark for the notes of the Unit 9 - Spark in the subject of Big Data":

### Installing Spark

1. Download Spark from https://spark.apache.org/downloads.html. Select a package type (pre-built for Hadoop 2.7 or later, or source code to build yourself). For this tutorial, download the pre-built for Hadoop 2.7 or later.

2. Unzip the downloaded package into a directory. This will become your SPARK_HOME.
    * For example, unzip to /usr/local/spark.

3. (Optional) Set the SPARK_HOME environment variable to point to the directory you unzipped Spark into. This is not required, but makes running Spark programs easier. You'll need to add SPARK_HOME/bin to your PATH as well.
    * For example, in Bash or a bash-compatible shell:
    export SPARK_HOME=/usr/local/spark
    export PATH=$SPARK_HOME/bin:$PATH

4. Ensure Java 8 (or higher) is installed and available on your PATH. Spark requires Java 8 to run.

5. (Optional) Install PySpark (the Python API for Spark). Do this by following the instructions in the Spark README to download pip and setup.py and running python setup.py install in the Python directory within the Spark directory. This allows you to write Spark applications in Python.

That's it - you now have Spark installed and ready to run applications. You can verify your installation by running Spark's interactive shell (in Scala or Python).