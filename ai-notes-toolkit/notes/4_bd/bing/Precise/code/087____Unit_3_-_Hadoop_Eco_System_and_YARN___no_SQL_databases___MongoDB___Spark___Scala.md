## Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

```scala
// Hadoop Eco System and YARN
import org.apache.hadoop.yarn.api.records.ApplicationId
import org.apache.hadoop.yarn.client.api.YarnClient
import org.apache.hadoop.yarn.conf.YarnConfiguration

val conf = new YarnConfiguration()
val yarnClient = YarnClient.createYarnClient()
yarnClient.init(conf)
yarnClient.start()

val app = yarnClient.createApplication()
val appId: ApplicationId = app.getNewApplicationResponse().getApplicationId()

// no SQL databases
import com.mongodb.casbah.Imports._

val mongoClient = MongoClient("localhost", 27017)
val db = mongoClient("mydb")
val coll = db("test")

val doc = MongoDBObject("name" -> "MongoDB", "type" -> "database", "count" -> 1, "info" -> MongoDBObject("x" -> 203, "y" -> 102))
coll.insert(doc)

// Spark
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

val conf = new SparkConf().setAppName("MyApp").setMaster("local")
val sc = new SparkContext(conf)

val data = Array(1, 2, 3, 4, 5)
val distData = sc.parallelize(data)

// Scala
val x = 1
val y = 2
val z = x + y
println(z)
```