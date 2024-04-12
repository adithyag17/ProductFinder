pipeline {
    agent any
    triggers {
        cron('H H * * 1') // This schedules the pipeline to run every Monday at 00:00. Adjust the cron expression as needed.
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/adithyag17/ProductFinder'
            }
        }
        stage('Build and Run Containers') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
