pipeline {
    agent any

    stages {
        
        stage('Remove Artifacts') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh "docker rm --force flask-app"
                    sh "docker rm --force nginx-proxy"
                }
            }
        }
        
        stage('Build active containers website image') {
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
        
         stage('Deploy active containers website') {
             steps {
                 sh 'docker run --privileged -d -p 5000:5000  -v /var/run/docker.sock:/var/run/docker.sock --name flask-app maiale/repo:flask-app'
             }
         }
        
         stage('Build NGINX image') {
             steps {
                sh 'docker build --tag nginx-proxy nginx/'
                sh 'docker tag nginx-proxy:latest maiale/repo:nginx-proxy'
                sh 'docker push maiale/repo:nginx-proxy'
             }
         }
        
         stage('Deploy NGINX server') {
             steps {
                 sh 'docker run -d -p 802:802 --name nginx-proxy maiale/repo:nginx-proxy'
             }
         }
        
    }
}

