pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    export TESTING=1
                    export FLASK_SECRET_KEY="test-secret-key-for-jenkins"
                    python3 -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask_mysql:latest .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag flask_mysql:latest ivanovich1106/hr_management_ivan:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-cred',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ivanovich1106/hr_management_ivan:latest
                    '''
                }
            }
        }
    }

    post {

        success {
            emailext(
                to: 'ivantravassosdbce@gmail.com',
                subject: "✅ ${env.JOB_NAME} #${env.BUILD_NUMBER} - SUCCESS",
                body: """
Build successful!

Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}

Docker image:
ivanovich1106/hr_management_ivan:latest

Build URL:
${env.BUILD_URL}
"""
            )
        }

        failure {
            emailext(
                to: 'ivantravassosdbce@gmail.com',
                subject: "❌ ${env.JOB_NAME} #${env.BUILD_NUMBER} - FAILED",
                body: """
Build FAILED!

Job: ${env.JOB_NAME}
Build: #${env.BUILD_NUMBER}

Please check the Jenkins console output.

Build URL:
${env.BUILD_URL}
"""
            )
        }
    }
}