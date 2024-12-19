pipeline {
    stages {
        stage("pylint test") {
            steps{
                sh "ls -la"
                sh "pip install pylint"
                sh "pylint app.py --fail-under=8"
            }
        }
    }
}

