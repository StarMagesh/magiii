pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/StarMagesh/magiii.git'
            }
        }
        stage('Build & Unit Test') {
            steps {
                // This runs your Logic AND/OR/NOT tests
                sh 'mvn clean test'
            }
        }
        stage('Docker Build') {
            steps {
                // This creates the container image
                sh 'docker build -t magiii-app:latest .'
            }
        }
    }
}
