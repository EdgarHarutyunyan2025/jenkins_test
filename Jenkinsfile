pipeline {
    agent {
        docker { 
            image "python:latest" 
	    args '--user root'
		}
    	  }
    stages {
        stage('Test') {
            steps {
                sh "ls -la" 
                sh "python app.py"
                sh "pip install flake8"
                sh "flake8 app.py"
            }
        }
    }
}
