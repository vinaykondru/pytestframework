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
                python -m venv venv
                source venv/bin/activate
                python -m pip install --upgrade pip --no-cache-dir
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
