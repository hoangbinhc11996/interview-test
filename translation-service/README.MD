### 
### 1. Build project
Before build project we need to configure it, open application.properties file to update credential of sql database
Build the project
```bash
cd <project>/
mvn clean package -DskipTests
```
### 2. Deployment
execute following commands to deploy jar file to azure app instance
```bash
# create spring app
az spring app create \
    --resource-group <name-of-resource-group> \
    --service <service-instance-name> \
    --name <application-name> \
    --assign-endpoint true

az spring app deploy \
    --resource-group <name-of-resource-group> \
    --service <service-instance-name> \
    --name <application-name> \
    --artifact-path target/<jar-file>.jar
```

### 3. Test endpoint

there are two parameters are page and size that needed to send requests, the default value of page is 0, size is 10
change it and run following command
```bash
curl https://primary:ZszgFuUVAeM7arBdrf73nOxT9fe2lhw8agXE5IVqrAPnue8rG6dvcN2OaHdtPN8U@testazurespringapp.test.azuremicroservices.io/testapp/default/api/sentences?page=10
```