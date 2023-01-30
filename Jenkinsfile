pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker --version'
                sh 'sudo docker build --tag flask-app .'
            }
        }
    }
}

