pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps{
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
