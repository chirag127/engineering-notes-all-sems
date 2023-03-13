### Google App Engine for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Google App Engine (GAE) is a platform-as-a-service (PaaS) product that provides web app developers and enterprises with access to Google's scalable hosting and tier 1 internet service.
- GAE requires that applications be written in Java, Python, Go, PHP, or Node.js, store data in Google Cloud Datastore, Google Cloud SQL, or Google Cloud Storage, and use the Google query language .
- GAE is a fully managed, serverless platform that uses in-built services to run your apps, such as load balancing, health checking, logging, debugging, monitoring, and security .
- GAE supports two types of environments: standard and flexible. The standard environment runs your app in a sandboxed environment with pre-defined runtime libraries and a fixed amount of resources. The flexible environment runs your app in a Docker container on Google Compute Engine, allowing you to customize the runtime and the resources.
- GAE allows you to deploy multiple versions of your app, each running on a different URL, and to migrate traffic between them gradually. You can also create different services within your app, each with its own version, scaling, and configuration.
- GAE is mostly used to run web applications that can scale dynamically as demand changes over time, because of Google's vast computing infrastructure. Some examples of apps that use GAE are Snapchat, Khan Academy, and Spotify .

#### Advantages of Google App Engine

- You don't have to worry about managing servers, operating systems, patches, or updates, as GAE handles them for you automatically .
- You can leverage Google's expertise and experience in building and running reliable, secure, and fast web applications .
- You can benefit from the integration with other Google Cloud products and services, such as Cloud Functions, Cloud Pub/Sub, Cloud Vision API, and Cloud Natural Language API .
- You can take advantage of the free tier and the pay-per-use pricing model, which only charges you for the resources you actually use .
- You can easily scale your app up or down, depending on the traffic and load, without any downtime or performance degradation .

#### Disadvantages of Google App Engine

- You have to follow the restrictions and limitations of the GAE environment, such as the supported languages, libraries, frameworks, and APIs .
- You have to deal with the vendor lock-in, as migrating your app from GAE to another platform may require significant changes in your code and architecture .
- You have to monitor and optimize your app's resource consumption, as exceeding the free quota or the budget may result in unexpected costs or service interruptions .
- You have to trust Google with your data and privacy, as GAE may collect and store your app's logs, metrics, and user information .

#### Mnemonics and learning tricks for Google App Engine

- To remember the supported languages in GAE, you can use the acronym **JPGPN**, which stands for **J**ava, **P**ython, **G**o, **P**HP, and **N**ode.js.
- To remember the difference between the standard and flexible environments in GAE, you can use the analogy of a **sandwich**. The standard environment is like a pre-made sandwich that you can buy from a store, which has a fixed set of ingredients and a fixed price. The flexible environment is like a custom-made sandwich that you can order from a restaurant, which allows you to choose the ingredients and the size, but also costs more and takes longer to prepare.
- To remember the benefits of GAE, you can use the acronym **RISFS**, which stands for **R**eliability, **I**ntegration, **S**calability, **F**ree tier, and **S**erverless.