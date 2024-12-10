pipeline {
    agent {
        docker {
            image "python:latest"
            args "--user root"
        }

    triggers {
        githubPush()
        }
    stages {
        stage('Git clone') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: 'main']],
                    extensions: [cleanBeforeCheckout()],
                    userRemoteConfigs: [[
                        credentialsId: 'github-ssh-key', 
                        url: 'git@github.com:EdgarHarutyunyan2025/jenkins_test.git'
                    ]]
                ])
            }
        }
        stage("pylint test") {
            steps{
                sh "ls -la"
                sh "pip install pylint"
                sh "pylint app.py --fail-under=8"
            }
        }
        stage("Archive Artifact") {
            steps{
                archiveArtifacts artifacts: "*"
            }
        }
    }
}

