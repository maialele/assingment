pipeline {
    agent any

    stages {
        stage('Remove Artifacts') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "docker rm --force flask-app"
                }
            }
        }
        stage('Build') {
            environment {
                my_docker_pass = credentials('DOCKER_PASS')
            }
            steps {
                sh 'docker build --tag flask-app .'
                sh 'docker tag flask-app:latest maiale/repo:flask-app'
                sh 'echo $my_docker_pass | docker login --username maiale --password-stdin'
                sh 'docker push maiale/repo:flask-app'
            }
        }
         stage('Deploy') {
             steps {
                 sh 'docker run --privileged -d -p 5000:5000  -v /var/run/docker.sock:/var/run/docker.sock --name flask-app maiale/repo:flask-app'
             }
         }
    }
}

