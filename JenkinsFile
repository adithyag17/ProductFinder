pipeline {
    agent any

    triggers {
        cron('H H * * 1') // This schedules the pipeline to run every Monday at 00:00. Adjust the cron expression as needed.
    }

    stages {
        stage('Checkout SCM'){
            steps {
                git branch: 'main', url: 'https://github.com/adithyag17/ProductFinder'
                // Replace 'main' with your branch name if it's different
                // Replace 'your-git-credentials-id' with the ID of your Jenkins Git credentials if needed
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
