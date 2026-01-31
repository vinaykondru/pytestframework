pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            reuseNode true
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vinaykondru/pytestframework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt

                '''
            }
        }

        stage('Run Automation Tests') {
            steps {
                sh '''
                pytest tests/ --html=report.html
                '''
            }
        }
    }


}
