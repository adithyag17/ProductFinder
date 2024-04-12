pipeline {
    agent any

    triggers {
        cron('0 0 * * 0') // Runs every Sunday at midnight (0 0 * * 0)
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/adithyag17/ProductFinder'
                // Replace 'main' with your branch name if it's different
                // Replace 'your-git-credentials-id' with the ID of your Jenkins Git credentials
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
