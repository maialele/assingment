pipeline {
    agent any

    stages {
        stage('Build') {
            environment {
                my_docker_pass = credentials('DOCKER_PASS')
                my_sudo_pass = credentials('SUDO_PASS')
            }
            steps {
                sh 'docker rm flask-app'
                sh 'docker build --tag flask-app .'
                sh 'docker tag flask-app:latest maiale/repo:flask-app'
                sh 'echo $my_docker_pass | docker login --username maiale --password-stdin'
                sh 'docker push maiale/repo:flask-app'
                sh 'echo $my_sudo_pass | sudo -S docker ps >> active_containers'
                sh 'docker run -d -p 5000:5000 --name flask-app maiale/repo:flask-app'
                sh 'echo $my_sudo_pass | sudo -S cp active_containers flask-app:/'
            }
        }
    }
}

