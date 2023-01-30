pipeline {
    agent any

    stages {
        stage('Build') {
            environment {
                my_sudo_pass = credentials('SUDO_PASS')               
            }
            steps {
                sh 'docker --version'
                sh 'echo $my_sudo_pass | sudo -S docker build --tag flask-app .'
                sh 'echo $my_sudo_pass | sudo -S docker tag flask-app:latest maiale/repo:flask-app'
                sh 'echo $my_sudo_pass | sudo docker push maiale/repo:flask-app'
            }
        }
    }
}

