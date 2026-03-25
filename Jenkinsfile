pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rakeshthagilla/leap-app"
    }

    stages {

         

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh '''
                echo "Rakesh@1571" | docker login -u  rakeshthagilla --password-stdin
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run rakeshthagilla/leap-app 2024'
            }
        }
    }
}
