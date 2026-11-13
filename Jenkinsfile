pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Compilar') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m compileall app main.py
                '''
            }
        }

        stage('Pruebas') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }

    post {
        success { echo 'Pipeline exitoso: el codigo se integro correctamente.' }
        failure { echo 'Pipeline fallido: revisar los errores en los logs.' }
    }
}
