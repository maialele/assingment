pipeline {
    agent any

    stages {
        stage('Build') {
            environment {
                my_docker_pass = credentials('DOCKER_PASS')               
            }
            steps {
                sh 'docker build --tag flask-app .'
                sh 'docker tag flask-app:latest maiale/repo:flask-app'
                sh 'docker login'
                sh 'docker push maiale/repo:flask-app'
            }
        }
    }
}

