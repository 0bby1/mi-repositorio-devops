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
                sh 'docker build -t mi-app ./app'
            }
        }

        stage('Stop contenedor anterior') {
            steps {
                sh 'docker stop mi-contenedor || true'
                sh 'docker rm mi-contenedor || true'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker run -d -p 5001:5000 --name mi-contenedor mi-app'
            }
        }
    }
}
