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
                sh "pip install pylint"
                sh "pylint app.py --fail-under=8"
            }
        }
    }
}
