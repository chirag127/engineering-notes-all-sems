# Google App Engine

- Google App Engine (GAE) is a platform-as-a-service (PaaS) product that provides web app developers and enterprises with access to Google's scalable hosting and tier 1 internet service.
- GAE requires that applications be written in Java or Python, store data in Google Bigtable and use the Google query language.
- GAE is a fully managed cloud computing platform that uses in-built services to run your apps .
- GAE supports popular development languages such as Java, Python, Go, PHP, and Node.js, and provides a range of developer tools.
- GAE is a serverless platform, meaning that you do not need to provision or manage any servers, and you only pay for the resources you use.
- GAE consists of the following components:
  - App: The top-level container that includes the service, version, and instance resources that make up your app.
  - Service: A group of related versions of your app that perform a specific function, such as a frontend or a backend.
  - Version: A specific iteration of your app's code that is deployed to a service.
  - Instance: A virtual machine that runs your app's code for a given version and service.
- GAE offers two environments for deploying your app: standard and flexible.
  - Standard environment: Provides a preconfigured runtime environment with automatic scaling, load balancing, logging, and health checks.
  - Flexible environment: Provides a custom runtime environment that runs on Google Compute Engine VMs, with manual or automatic scaling, and access to advanced Google Cloud services.