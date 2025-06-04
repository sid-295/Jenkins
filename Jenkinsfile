pipeline {
    agent any

    stages {
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/sid-295/Jenkins.git", branch: "main"
            }
        }

        stage("Build") {
            steps {
                echo "Building the Docker image"
                sh "docker build -t cyber295/my-node-app ."
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "Pushing to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh "docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASS"
                    sh "docker push cyber295/my-node-app:latest"
                }
            }
        }

        stage("Deploy") {
            steps {
                echo "Deploying the application"
                sh "docker-compose down && docker-compose up -d"
                
            }
        }
    }
}
