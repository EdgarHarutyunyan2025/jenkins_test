pipeline {
    agent { image "python:latest" }
    stages {
        stage("pylint test") {
            steps{
                echo "======= start ======="
                sh """ls -la
                      cat *.py"""

            }
        }
    }
}

