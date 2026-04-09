# Use an OpenJDK image to run the app
FROM openjdk:17-jdk-slim

# Copy the built JAR file from the target folder
COPY target/baseline-ci-app-1.0-SNAPSHOT.jar app.jar

# Run the application
ENTRYPOINT ["java", "-jar", "/app.jar"]
