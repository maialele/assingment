pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                sh 'git clone "https://github.com/maialele/assingment.git"'
                cd assingment
            }
        }
        stage('Build') {
            steps {
                sh 'docker --version'
                sh 'docker build --tag flask-app .'
            }
        }
    }
}

