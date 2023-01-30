pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker --version'
                sh 'docker build --tag flask-app .'
            }
        }
    }
}

