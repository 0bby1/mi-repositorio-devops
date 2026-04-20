pipeline {
    agent any

    stages {

        stage('Clonar código') {
            steps {
                git 'https://github.com/0bby1/mi-repositorio-devops.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t flask-app ./app'
            }
        }

        stage('Stop contenedor anterior') {
            steps {
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5001:5000 --name flask-container flask-app'
            }
        }
    }
}
