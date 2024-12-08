pipeline {
    agent {
        docker { image "python:latest" }
    }
    stages {
        stage('Test') {
            steps {
                sh "ls -la" 
                sh "python app.py"
                sh 'pip install pylint'
            }
        }
    }
}
